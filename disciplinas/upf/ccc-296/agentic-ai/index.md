# Sistema Multiagente com LangChain + Llama (local) + RAG + Tools + MCP (mínimo)

Aqui vamos descrever um caminho **simples** para construir que envolve a construção de um sistema multiagente, executando **modelo local (família LLaMA)**, com **RAG** (base vetorial + embeddings), **tools acionáveis**, **interface via terminal** e uma integração **mínima com MCP**.

Uma **LLM** (*Large Language Model*) é um modelo de linguagem que gera texto e consegue seguir instruções. Um **agente** é uma aplicação que usa uma LLM para decidir *o que fazer* e, quando necessário, **chama ferramentas** (*tools*) para obter dados ou executar ações. Um sistema **multiagente** é um conjunto de dois ou mais agentes com papéis diferentes (por exemplo: supervisor, recuperador, executor) cooperando para resolver tarefas.

**RAG** (*Retrieval-Augmented Generation*) é uma técnica em que a resposta é gerada com apoio de informações recuperadas de uma base (por exemplo, uma base vetorial). **MCP** (*Model Context Protocol*) é um padrão para expor e consumir ferramentas e recursos de forma interoperável entre clientes e servidores.

A implementação irá consideradar as seguintes tecnologias:

- **LangChain** para prompts, cadeias e ferramentas[@langchain_docs].
- **LangGraph** para orquestrar múltiplos agentes (supervisor + especialistas)[@langgraph_docs].
- **Ollama** para rodar um modelo Llama local (forma mais simples na prática)[@ollama][@touvron2023llama2].
- **Chroma** como armazenamento vetorial local[@chromadb].
- **MCP Python SDK** para expor tools via um servidor padronizado[@mcp_python_sdk].

---

## Visão geral da arquitetura

Uma **arquitetura em camadas** separa responsabilidades para facilitar manutenção e testes. **Vector store** (base vetorial) é um banco otimizado para buscar “textos parecidos” a partir de vetores numéricos; aqui, o **Chroma** cumpre esse papel. **Embeddings** são vetores que representam o significado de um texto. **CLI** (*Command-Line Interface*) é a interface de terminal usada para executar a aplicação.

A aplicação terá três camadas.

1. Uma camada **LLM local** (Ollama) que serve o modelo Llama e, opcionalmente, embeddings.
2. Uma camada **conhecimento** (RAG): carregamento de documentos, chunking, embeddings e base vetorial.
3. Uma camada **multiagente** (LangGraph): um supervisor decide qual agente chamar; agentes chamam tools (RAG, leitura de arquivos, cálculos etc.).

```mermaid
flowchart TD
  U[Usuário no terminal] -->|pergunta| CLI[CLI Python]

  CLI --> SUP[Agente Supervisor (LLM)]

  SUP -->|rota: RAG| AR[Agente Recuperador (LLM)]
  SUP -->|rota: executar| AE[Agente Executor (LLM)]
  SUP -->|rota: responder| AF[Agente Finalizador (LLM)]

  AR -->|tool| RAG[Tool: buscar na base vetorial]
  AE -->|tool| CALC[Tool: calcular expressão]
  AE -->|tool| FILE[Tool: ler arquivo (restrito)]

  RAG --> VS[(Chroma: vetores)]
  VS --> EMB[Embeddings]
  EMB --> OLLAMA[(Ollama: Llama + Embeddings)]

  FILE --> FS[(Arquivos locais)]

  %% MCP como servidor opcional de tools
  AE -. opcional .-> MCP[Servidor MCP (tools)]
  MCP -. stdio/http .-> CLI
```

A decisão de “quem faz o quê” segue o que normalmente é esperado em um trabalho multiagente:

- O **Supervisor** decide a estratégia e roteia.
- O **Recuperador** é especializado em “buscar evidências” na base.
- O **Executor** é especializado em “agir”: chamar ferramentas.
- O **Finalizador** sintetiza a resposta final com base nos resultados.

---

## Pré-requisitos

**Ollama** é um runtime local que baixa e executa modelos e expõe uma API local. Um **modelo de embeddings** (por exemplo, `nomic-embed-text`) é um modelo especializado em transformar texto em vetores. Um **ambiente virtual** (`.venv`) isola dependências do projeto para evitar conflitos entre bibliotecas.

### Instalar e preparar o Ollama

O objetivo é rodar um modelo local do tipo Llama.

1. Instalação do Ollama conforme o sistema operacional (ver documentação) [@ollama].
2. Em seguida, baixar um modelo Llama e um modelo de embeddings.

Exemplo (pode variar conforme os nomes disponíveis no Ollama):

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

Para verificar se o Ollama está respondendo:

```bash
ollama run llama3.1:8b "Olá!"
```

### Criar ambiente Python do projeto

O tutorial usa Python e dependências do ecossistema LangChain.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Instalação das bibliotecas:

```bash
pip install -U \
    langchain langchain-community langchain-core \
    langchain-ollama \
    langchain-chroma \
    langchain-text-splitters \
    langgraph \
    chromadb \
  pydantic \
  rich
```

Para a parte de MCP (se for utilizada):

```bash
pip install -U "mcp[cli]"
```

---

## Integração: Llama local com LangChain (Ollama)

Um **wrapper** é uma “camada de adaptação” que permite chamar um serviço externo com uma API mais conveniente; aqui, `ChatOllama` encapsula chamadas ao Ollama. O método `invoke(...)` executa uma chamada de modelo e retorna uma resposta. **Temperatura** é um parâmetro que controla aleatoriedade: valores menores tendem a respostas mais estáveis e determinísticas.

A forma mais simples é usar o wrapper do Ollama disponibilizado na comunidade LangChain.

### Exemplo mínimo de chat

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.2,
)

resp = llm.invoke("Explique, em 2 frases, o que é RAG.")
print(resp.content)
```

Ao longo do tutorial, o mesmo `ChatOllama` será reutilizado para:

- roteamento (supervisor),
- agentes especialistas,
- síntese final.

---

## Vetorização (embeddings + Chroma)

**Vetorização** é o processo de transformar documentos em embeddings e armazená-los em uma base vetorial. **Chunking** é a divisão de um documento em pedaços menores (*chunks*) para melhorar a busca e caber no contexto do modelo. Um **text splitter** é o componente que define como os chunks serão criados (tamanho e sobreposição).

Nesta etapa, a aplicação cria uma base vetorial a partir de documentos locais. O fluxo típico é:

1. carregar arquivos,
2. dividir em “pedaços” (chunks),
3. calcular embeddings,
4. persistir no Chroma.

### Carregar documentos e fazer chunking

O exemplo abaixo considera uma pasta `knowledge_base/` contendo PDFs, Markdown ou TXT. Para manter simples, o exemplo assume TXT/Markdown.

```python
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

kb_dir = Path("knowledge_base")
kb_dir.mkdir(exist_ok=True)

loader = DirectoryLoader(
    str(kb_dir),
    glob="**/*.md",
    loader_cls=TextLoader,
    show_progress=True,
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
)

chunks = splitter.split_documents(docs)
print(f"Docs: {len(docs)} | Chunks: {len(chunks)}")
```

Observação: para PDF, o projeto pode usar loaders específicos, mas isso adiciona dependências. O caminho simples é começar com Markdown e TXT.

### Embeddings com Ollama e persistência no Chroma

O exemplo usa `nomic-embed-text`, que é muito comum no Ollama e funciona bem para protótipos.

```python
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=".chroma",
)

vectorstore.persist()
print("Base vetorial criada em .chroma")
```

---

## RAG (recuperação + geração)

Um **retriever** é o componente que consulta a base vetorial e devolve os trechos mais relevantes para uma pergunta. O parâmetro `k` define quantos trechos serão recuperados. O **contexto** é o conjunto desses trechos anexados ao prompt para que a LLM responda “com base em evidência”, reduzindo alucinações.

Existem várias formas de implementar RAG em LangChain. O caminho simples é:

- usar o `retriever` do Chroma para buscar os chunks relevantes;
- passar os chunks para um prompt de resposta.

### 5.1) Recuperação semântica

```python
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

llm = ChatOllama(model="llama3.1:8b", temperature=0.2)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory=".chroma",
    embedding_function=embeddings,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

query = "O que é MCP e para que serve?"
docs = retriever.get_relevant_documents(query)

for i, d in enumerate(docs, start=1):
    print("\n---")
    print(f"Trecho {i} | fonte: {d.metadata}")
    print(d.page_content[:300])
```

### Geração com contexto recuperado (RAG básico)

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "A tarefa é responder usando APENAS o contexto fornecido. "
        "Se o contexto não contiver a resposta, a saída deve dizer que não há evidência suficiente.",
    ),
    ("human", "Pergunta: {question}\n\nContexto:\n{context}"),
])

context = "\n\n".join([d.page_content for d in docs])

resp = llm.invoke(prompt.format_messages(question=query, context=context))
print(resp.content)
```

Esse padrão vira uma **tool** reutilizável no passo seguinte.

---

## Criando Tools (ações que agentes podem chamar)

Uma **tool** é uma função que o agente pode chamar durante a execução (por exemplo: buscar na base, ler arquivo, calcular). **Tool calling** é o mecanismo em que a LLM escolhe *quando* e *com quais argumentos* chamar uma tool. **Efeitos colaterais** são alterações fora do processo (escrever arquivos, fazer requisições, apagar dados); em protótipos didáticos, é comum começar por tools sem efeitos colaterais.

A ideia é transformar capacidades em funções com assinatura clara. Em LangChain, uma opção direta é usar o decorador `@tool`.

A seguir estão três tools que cobrem os requisitos típicos do trabalho:

- `buscar_base`: RAG/retrieval (sem efeitos colaterais).
- `calcular`: execução de um cálculo simples com validação.
- `ler_arquivo`: leitura restrita de arquivo local (segurança mínima).

### Tools em Python

```python
import ast
from pathlib import Path

from langchain_core.tools import tool


def _safe_eval_arithmetic(expr: str) -> float:
    """Avalia apenas expressões aritméticas simples usando AST."""

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Constant,
        ast.Mod,
        ast.FloorDiv,
        ast.Load,
        ast.Call,  # opcional (pode remover para ficar mais restrito)
        ast.Name,
    )

    allowed_names = {
        "abs": abs,
        "round": round,
    }

    tree = ast.parse(expr, mode="eval")

    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError(f"Operação não permitida: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id not in allowed_names:
            raise ValueError(f"Nome não permitido: {node.id}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in allowed_names:
                raise ValueError("Chamada de função não permitida")

    code = compile(tree, "<expr>", "eval")
    return float(eval(code, {"__builtins__": {}}, allowed_names))


@tool
def calcular(expressao: str) -> str:
    """Calcula uma expressão aritmética simples (ex.: "(2+3)*4")."""
    try:
        value = _safe_eval_arithmetic(expressao)
        return str(value)
    except Exception as e:
        return f"ERRO: {e}"


@tool
def ler_arquivo(caminho: str) -> str:
    """Lê um arquivo local (restrito à pasta knowledge_base/)."""
    base = Path("knowledge_base").resolve()
    target = (Path(caminho)).resolve()

    if base not in target.parents and target != base:
        return "ERRO: caminho fora da pasta knowledge_base/"

    if not target.exists() or not target.is_file():
        return "ERRO: arquivo não encontrado"

    return target.read_text(encoding="utf-8")[:5000]
```

A tool `buscar_base` depende do vectorstore. O padrão mais simples é fechá-la via closure (função que “captura” o retriever).

```python
from langchain_core.tools import tool


def make_buscar_base_tool(retriever):
    @tool
    def buscar_base(pergunta: str) -> str:
        """Busca trechos relevantes na base vetorial e retorna contexto."""
        docs = retriever.get_relevant_documents(pergunta)
        return "\n\n".join([d.page_content for d in docs])

    return buscar_base
```

---

## Criando agentes (ReAct) e uma estrutura multiagente com LangGraph

**ReAct** (*Reason + Act*) é um padrão de agente em que a LLM alterna entre raciocinar (“qual o próximo passo?”) e agir (chamar tools) até chegar a um resultado. **LangGraph** organiza a execução como um **grafo**: cada **nó** é uma etapa (supervisor, recuperador, executor) e as **arestas** definem a ordem e o roteamento. O **estado** é um objeto (por exemplo, `Estado`) onde a aplicação acumula informação entre nós.

### Por que LangGraph aqui?

LangChain possui agentes “prontos” em vários estilos, mas uma arquitetura multiagente fica mais clara e controlável quando a orquestração é explícita. LangGraph [@langgraph_docs] faz isso com um grafo simples de nós.

### Definindo agentes especialistas

O caminho simples é usar dois agentes ReAct, cada um com um conjunto pequeno de tools.

- Agente Recuperador: só faz busca (RAG) e devolve evidências.
- Agente Executor: faz ações locais (ler arquivo e calcular).

```python
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1:8b", temperature=0.2)

# buscar_base é criado a partir do retriever no passo 6
agente_recuperador = create_react_agent(llm, tools=[buscar_base])
agente_executor = create_react_agent(llm, tools=[ler_arquivo, calcular])
```

### Supervisor: roteando a tarefa para o agente adequado

O supervisor pode ser implementado como uma decisão LLM que devolve uma rota. O exemplo abaixo retorna apenas uma das opções: `recuperar`, `executar`, `finalizar`.

```python
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate


class Rota(BaseModel):
    acao: str = Field(description="Uma das opções: recuperar, executar, finalizar")


roteador_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é um supervisor de agentes. "
        "Escolha a ação mais apropriada para responder à pergunta. "
        "Use: recuperar quando precisar buscar base vetorial; executar quando precisar de ferramentas locais; "
        "finalizar quando já houver informação suficiente para responder."
    ),
    ("human", "Pergunta do usuário: {pergunta}\n\nResumo do estado atual:\n{estado}"),
])


def decidir_rota(llm, pergunta: str, estado: str) -> str:
    msg = roteador_prompt.format_messages(pergunta=pergunta, estado=estado)
    # Forma simples: pedir uma palavra; em produção, preferir saída estruturada.
    resp = llm.invoke(msg).content.lower()

    if "execut" in resp:
        return "executar"
    if "final" in resp:
        return "finalizar"
    return "recuperar"
```

### 7.4) Construindo o grafo multiagente

O grafo a seguir executa um ciclo curto:

1. supervisor decide,
2. chama recuperador ou executor,
3. acumula resultados,
4. finaliza quando a rota for `finalizar`.

```python
from typing import TypedDict

from langgraph.graph import StateGraph, END


class Estado(TypedDict):
    pergunta: str
    evidencias: str
    acoes: str


def node_supervisor(state: Estado) -> dict:
    estado_txt = f"Evidencias: {state.get('evidencias','')[:300]}\nAcoes: {state.get('acoes','')[:300]}"
    rota = decidir_rota(llm, state["pergunta"], estado_txt)
    return {"_rota": rota}


def node_recuperador(state: Estado) -> dict:
    result = agente_recuperador.invoke({
        "messages": [
            (
                "system",
                "Você é um agente RECUPERADOR. "
                "Sua tarefa é chamar buscar_base para obter trechos relevantes e devolver um resumo curto "
                "com as evidências mais importantes.",
            ),
            ("user", state["pergunta"]),
        ]
    })
    # create_react_agent retorna estado com messages; aqui, simplifica pegando o último
    texto = result["messages"][-1].content
    return {"evidencias": (state.get("evidencias", "") + "\n" + texto).strip()}


def node_executor(state: Estado) -> dict:
    result = agente_executor.invoke({
        "messages": [
            (
                "system",
                "Você é um agente EXECUTOR. "
                "Quando precisar de dados locais, use ler_arquivo. "
                "Quando precisar de contas, use calcular. "
                "Devolva o resultado de forma objetiva.",
            ),
            ("user", state["pergunta"]),
        ]
    })
    texto = result["messages"][-1].content
    return {"acoes": (state.get("acoes", "") + "\n" + texto).strip()}


def node_finalizador(state: Estado) -> dict:
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "A tarefa é responder de forma clara e completa. "
            "Use evidências e resultados de tools quando existirem."
        ),
        ("human", "Pergunta: {pergunta}\n\nEvidências:\n{evidencias}\n\nAções:\n{acoes}"),
    ])

    msg = prompt.format_messages(
        pergunta=state["pergunta"],
        evidencias=state.get("evidencias", ""),
        acoes=state.get("acoes", ""),
    )

    resp = llm.invoke(msg).content
    return {"resposta": resp}


graph = StateGraph(Estado)

graph.add_node("supervisor", node_supervisor)
graph.add_node("recuperador", node_recuperador)
graph.add_node("executor", node_executor)
graph.add_node("final", node_finalizador)

graph.set_entry_point("supervisor")


def roteamento(state):
    return state.get("_rota", "recuperar")


graph.add_conditional_edges(
    "supervisor",
    roteamento,
    {
        "recuperar": "recuperador",
        "executar": "executor",
        "finalizar": "final",
    },
)

graph.add_edge("recuperador", "supervisor")
graph.add_edge("executor", "supervisor")
graph.add_edge("final", END)

app = graph.compile()
```

Para executar:

```python
state = {"pergunta": "Explique MCP e dê um exemplo de tool.", "evidencias": "", "acoes": ""}
result = app.invoke(state)
print(result["resposta"])
```

Essa estrutura já cumpre o núcleo do requisito “multiagente”: mais de um agente LLM, com papéis distintos e coordenação.

---

## Interface via terminal (CLI)

A maneira mais simples de demonstrar via terminal é criar um módulo `cli.py` com `argparse`. Um esqueleto mínimo:

```python
import argparse


def main():
    parser = argparse.ArgumentParser(description="Demo multiagente com RAG")
    parser.add_argument("--pergunta", required=True)
    args = parser.parse_args()

    state = {"pergunta": args.pergunta, "evidencias": "", "acoes": ""}
    out = app.invoke(state)

    print("\n=== RESPOSTA ===\n")
    print(out["resposta"])


if __name__ == "__main__":
    main()
```

Uso:

```bash
python cli.py --pergunta "Resuma os pontos obrigatórios do trabalho e sugira uma divisão de agentes."
```

---

## MCP (mínimo): expondo tools via um servidor padronizado

No **MCP**, um **servidor** expõe tools (e, em geral, também recursos e prompts) e um **cliente** descobre e chama essas tools. O transporte **stdio** significa que a comunicação ocorre via entrada/saída padrão (processo filho), o que é prático para protótipos. A chamada de tool normalmente segue um estilo de **RPC** (chamada remota de procedimento), em que o cliente envia o nome da tool e argumentos estruturados e recebe a resposta.

O trabalho pede MCP. O objetivo aqui é mostrar o uso mais direto: criar um **servidor MCP** que expõe tools e um **cliente** que chama essas tools. O projeto também pode “embrulhar” essas chamadas como tools do LangChain.

### Servidor MCP simples (stdio)

O MCP Python SDK oferece `FastMCP` [@mcp_python_sdk]. Um servidor mínimo:

```python
# server_mcp.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ToolsLocais", json_response=True)


@mcp.tool()
def ping() -> str:
    """Tool de teste."""
    return "pong"


@mcp.tool()
def soma(a: int, b: int) -> int:
    """Soma dois inteiros."""
    return a + b


if __name__ == "__main__":
    mcp.run()
```

Para rodar:

```bash
python server_mcp.py
```

### Cliente MCP chamando tools (stdio)

```python
# client_mcp.py
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server_mcp.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print([t.name for t in tools.tools])

            r1 = await session.call_tool("ping", arguments={})
            print("ping =>", r1.structuredContent)

            r2 = await session.call_tool("soma", arguments={"a": 2, "b": 3})
            print("soma =>", r2.structuredContent)


if __name__ == "__main__":
    asyncio.run(main())
```

### Transformando MCP em tool do LangChain

A integração mais simples é tratar “chamar tool MCP X” como uma função Python e expor essa função como tool do LangChain. Assim, um agente ReAct pode decidir chamar `mcp_soma` ou `mcp_ping`.

Em um protótipo didático, basta:

1. manter uma sessão MCP aberta,
2. criar wrappers Python síncronos (ou `async` + adaptador),
3. expor wrappers como tools.

---
