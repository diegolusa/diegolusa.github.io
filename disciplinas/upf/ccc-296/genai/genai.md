---
title: "Inteligência Artificial Generativa"
tags:
 - Inteligência Artificial
 - Gen AI
date: 2025-01-01 08:00:00
---


A Inteligência Artificial Generativa (GenAI) refere-se a sistemas capazes de gerar conteúdo novo — como textos, imagens, músicas ou códigos — a partir de dados aprendidos durante o treinamento. Essa capacidade é resultado de avanços significativos em redes neurais profundas, especialmente em arquiteturas como os **Transformers**.

## Evolução Histórica das LLMs

A trajetória da Inteligência Artificial Generativa, especialmente no que diz respeito aos Large Language Models (LLMs), acompanha marcos fundamentais da história da IA e do Processamento de Linguagem Natural (PLN). Em 1956, durante a conferência de Dartmouth, o termo “Inteligência Artificial” foi cunhado, lançando as bases para pesquisas que, décadas depois, resultariam nos modelos generativos. Nos anos 1960, surgiram os primeiros sistemas de conversação baseados em regras, como o ELIZA, criado por Joseph Weizenbaum, que simulava um psicoterapeuta por meio de padrões textuais simples, sem real compreensão.

Com o passar das décadas, modelos estatísticos como n-gramas dominaram o PLN, até que, nos anos 2000, surgiram abordagens baseadas em aprendizado profundo. A década de 2010 trouxe avanços significativos. Em 2013, o Word2Vec, criado por pesquisadores do Google, introduziu a representação vetorial de palavras em espaços semânticos contínuos. Em 2014, a arquitetura Seq2Seq com redes recorrentes (RNNs) e memória de longo prazo (LSTM) revolucionou a tradução automática. No mesmo ano, Ian Goodfellow apresentou as Redes Generativas Adversariais (GANs), marcando o nascimento da IA generativa em imagens.

O verdadeiro divisor de águas ocorreu em 2017, com o artigo [Attention is All You Need](https://arxiv.org/abs/1706.03762), de Vaswani et al., que introduziu a arquitetura Transformer. Essa inovação eliminou a necessidade de redes recorrentes ao introduzir mecanismos de atenção capazes de processar entradas em paralelo, melhorando a escalabilidade e a eficiência dos modelos. No ano seguinte, em 2018, o BERT (Bidirectional Encoder Representations from Transformers), desenvolvido pelo Google, trouxe a capacidade de pré-treinamento bidirecional para entender o contexto completo de uma frase.

Em paralelo, a OpenAI desenvolvia sua linha de modelos GPT (Generative Pretrained Transformer). O GPT-1, com 117 milhões de parâmetros, foi lançado em 2018 como uma prova de conceito. Já o GPT-2, em 2019, com 1,5 bilhão de parâmetros, mostrou capacidades de geração de texto altamente coerente, mas inicialmente teve sua liberação restrita por preocupações com uso indevido. Em 2020, o lançamento do GPT-3, com 175 bilhões de parâmetros, tornou-se um marco: seu desempenho em múltiplas tarefas sem necessidade de re-treinamento (few-shot learning) consolidou a relevância das LLMs no mercado.

Nos anos seguintes, surgiram diversos outros modelos com enfoques distintos. A Meta lançou a série *LLaMA* (Large Language Model Meta AI), com versões open-source como o LLaMA 2 e, mais recentemente, o LLaMA 3. A Stability AI popularizou a geração de imagens com o Stable Diffusion. A *Anthropic* entrou no mercado com o modelo *Claude*, priorizando alinhamento ético. O Google DeepMind apresentou o *Gemini* como alternativa multimodal.

Ao longo de 2023 e 2024, observou-se uma consolidação do uso comercial dessas ferramentas, acompanhada pela busca por modelos mais eficientes, acessíveis e adaptáveis para execução local. Iniciativas como o *llama.cpp*, o *Ollama* e o *LM Studio* demonstram o movimento “local-first”, permitindo o uso de LLMs em computadores pessoais. Modelos como o Mistral e o Phi-3 mostraram que é possível alcançar alto desempenho com arquiteturas menores e treinamentos mais otimizados.

### Arquitetura Transformer

A arquitetura Transformer revolucionou o campo do processamento de linguagem natural ao propor uma alternativa mais eficiente às redes neurais recorrentes (RNNs) e às LSTMs. Sua principal inovação foi o mecanismo de atenção, que permite ao modelo “focar” seletivamente em diferentes partes da entrada para cada elemento da saída, independentemente da distância posicional. Isso tornou o processamento paralelo viável, possibilitando ganhos significativos em eficiência e escalabilidade.

Ao contrário das RNNs, que processam as palavras sequencialmente e enfrentam dificuldades com longas dependências, os Transformers operam sobre toda a sequência de entrada simultaneamente. A entrada textual é primeiro convertida em vetores por meio de embeddings e enriquecida com codificações posicionais, que informam ao modelo a ordem relativa dos tokens — algo que não é intrínseco à arquitetura.

Cada camada Transformer é composta por duas partes principais: o mecanismo de atenção multi-cabeças (multi-head attention) e uma rede feedforward densa. O mecanismo de atenção calcula, para cada palavra da sequência, um vetor de atenção com base em três componentes: queries (consultas), keys (chaves) e values (valores). Essa operação é feita múltiplas vezes em paralelo (as várias "cabeças"), permitindo ao modelo capturar diferentes tipos de relacionamentos semânticos e sintáticos.

As saídas das cabeças de atenção são combinadas e passadas por camadas de normalização e feedforward. O modelo completo é empilhado em várias camadas idênticas, cada uma refinando as representações intermediárias. Em modelos autoregressivos, como os da família GPT, o decodificador prevê o próximo token com base apenas nos anteriores, utilizando uma máscara para evitar olhar para frente na sequência. Já em modelos como BERT, a atenção é bidirecional, permitindo considerar o contexto à esquerda e à direita de cada palavra simultaneamente.

Essa estrutura mostrou-se extremamente versátil, sendo aplicada não apenas em texto, mas também em visão computacional, bioinformática e geração de imagens. É o coração de modelos como BERT, GPT-3, GPT-4, T5, LLaMA, entre outros.


!!! Note "The Illustrated Transformer"

    Acesse o endereço [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/) para conhecer os detalhes da arquitetura transformer





### Dados de Treinamento

Os modelos são treinados com datasets gigantescos extraídos de:

- **Web aberta** (Wikipedia, [Common Crawl](https://commoncrawl.org/))
- **Livros digitalizados**
- **Bases de código** (GitHub)
- **Redes sociais, fóruns, etc.**

> ❗ Atenção: boa parte desses dados pode conter **viéses culturais**, **conteúdo sensível** e **dados não licenciados**, gerando questões éticas e legais.

#### Tokenização

A tokenização é uma das primeiras e mais importantes etapas no processamento de texto por modelos de linguagem. Ela consiste em dividir um texto contínuo em unidades menores chamadas **tokens**, que podem representar palavras inteiras, subpalavras, caracteres ou até mesmo espaços e pontuações, dependendo do tipo de tokenizador utilizado. O objetivo é transformar a linguagem natural em uma sequência estruturada que possa ser compreendida matematicamente pelo modelo.

Modelos mais antigos utilizavam tokenização por palavras inteiras, o que gerava vocabulários grandes e ineficientes. Já os modelos modernos, como os Transformers, utilizam estratégias como **Byte Pair Encoding (BPE)**, **WordPiece** ou **SentencePiece**, que operam em nível de subpalavras. Isso reduz o tamanho do vocabulário e melhora a capacidade do modelo de lidar com palavras raras, compostas ou inexistentes no treinamento original (out-of-vocabulary).

Por exemplo, a palavra “cachorro” pode ser dividida em tokens como “ca”, “chor” e “ro”, ou ainda “cach”, “or” e “ro”, a depender do modelo. Essa decomposição permite que o modelo entenda morfologia e relacione palavras semelhantes com mais facilidade. Além disso, todos os tokens são associados a vetores numéricos por meio de embeddings, que capturam aspectos semânticos e sintáticos desses fragmentos.

Em seguida, o modelo adiciona informações de posição por meio das chamadas **positional encodings**, pois, diferentemente de redes recorrentes, os Transformers não processam os tokens em ordem sequencial — e, portanto, precisam saber onde cada token está na sequência.

Essa combinação entre tokenização eficiente, representação vetorial densa e codificação posicional é o que torna possível que LLMs generalizem padrões da linguagem em escala massiva.


#### Embeddings: Representações Vetoriais da Linguagem

Embeddings são representações numéricas densas que capturam características semânticas e sintáticas de palavras ou tokens em um espaço vetorial contínuo. Em vez de tratar palavras como símbolos isolados, os embeddings permitem que os modelos de linguagem entendam relações e similaridades entre termos.

A criação dos embeddings é feita por uma **camada de embedding** dentro do modelo, que funciona como uma tabela de consulta (lookup table). Cada token no vocabulário é associado a um vetor treinável, e durante o pré-processamento os índices dos tokens são usados para recuperar esses vetores. Esses vetores são ajustados continuamente durante o pré-treinamento do modelo via retropropagação, de modo que palavras com significados semelhantes assumem posições próximas no espaço vetorial.

Além dos embeddings de tokens, também são adicionados **embeddings posicionais**, que representam a posição de cada token na sequência. Isso é necessário porque a arquitetura Transformer, diferentemente das RNNs, não possui senso intrínseco de ordem sequencial. Existem diferentes formas de codificação posicional: senoidal (como proposto originalmente) ou vetores treináveis aprendidos junto com os embeddings de palavra.

Durante o processamento, os embeddings passam por várias camadas de atenção e feedforward, gerando representações transformadas que capturam relações de mais alto nível, como dependências gramaticais e significado contextual. Ao final do processo de decodificação (no caso de modelos generativos), essas representações vetoriais precisam ser convertidas de volta para texto.

Essa conversão ocorre por meio de uma **camada linear** que projeta o vetor de saída para o espaço do vocabulário, seguido de uma função de ativação, geralmente uma **softmax**, que atribui probabilidades a cada token possível. O token com maior probabilidade é então selecionado como a próxima palavra a ser gerada. Esse processo pode ocorrer iterativamente, um token por vez, até que um token de parada (como ``) seja produzido ou um limite de comprimento seja atingido.

Esse ciclo de **tokenização → embedding → processamento → decodificação → texto** é a base do funcionamento de modelos como GPT, T5 e BERT (com variações para tarefas específicas, como classificação ou geração).




### Custos Computacionais e Ambientais

A crescente adoção de modelos de linguagem de larga escala (LLMs) e outras formas de inteligência artificial generativa tem levantado preocupações globais sobre os custos computacionais e os impactos ambientais associados à sua criação e uso contínuo. Pesquisas recentes oferecem evidências quantitativas e qualitativas que ajudam a compreender a magnitude desses efeitos.

Um dos estudos mais citados é o de [Patterson et al. (2021)](https://arxiv.org/abs/2104.10350), que analisou o consumo energético de grandes modelos. Segundo os autores, o treinamento do GPT-3 consumiu aproximadamente 1.287 MWh de energia elétrica. Para efeito de comparação, isso é equivalente ao consumo anual de cerca de 120 residências nos Estados Unidos. A maior parte desse consumo está associada ao uso de GPU clusters de alta performance, como as NVIDIA A100, utilizadas em larga escala em data centers especializados.

O mesmo estudo estimou que as emissões de dióxido de carbono (CO₂) para treinar modelos como o GPT-3 podem variar entre 550 e 1.200 toneladas métricas, dependendo da fonte de energia. Isso equivale às emissões anuais de aproximadamente 270 carros movidos a gasolina.

Outro trabalho importante, de [Strubell et al. (2019)](https://arxiv.org/abs/1906.02243), indicou que o treinamento de um grande modelo Transformer pode emitir mais carbono do que cinco carros durante toda sua vida útil.

E é importante lembrar que o impacto ambiental não termina no treinamento. A inferência de modelos, especialmente em serviços amplamente utilizados como ChatGPT, consome energia continuamente. A [International Energy Agency (IEA)](https://www.iea.org/reports/electricity-2023) alertou que o crescimento da demanda por IA poderá dobrar o consumo de energia dos data centers até 2026.

!!! Note "Quanto custa treinar grandes modelos LLM"
    Um trabalho interessante sobre custos relacionados ao treinamento de LLMs é [The rising costs of training frontier AI models](https://arxiv.org/pdf/2405.21015) 
 
 

### Execução Local

Embora a maior parte dos modelos massivos de linguagem sejam oferecidos na forma de serviços, é possível executar localmente diversos modelos. Naturalmente quanto mais parâmetros o modelo tem, maior será a demanda por recursos computacionais da máquina (normalmente os recursos mínimos estão indicados na documentação). 

Aqui estão algumas opções para utilizar modelos de linguagem no ambiente local.

- **llama.cpp** – Executa LLaMA localmente via CPU.
- **Ollama** – Interface para rodar modelos como Mistral, LLaMA2, etc.
- **LM Studio** – Interface gráfica para uso local com quantização.



 ## Agentic AI


 A Agentic AI (ou IA Agente) refere-se a sistemas de inteligência artificial projetados para agir de forma proativa, autônoma e orientada por objetivos, frequentemente em ambientes dinâmicos e complexos. Em vez de apenas responder a um prompt isolado, esses sistemas decompõem problemas, escolhem ações, consultam ferramentas, verificam resultados intermediários e ajustam o próprio comportamento ao longo da execução. Em termos práticos, isso significa sair de um modelo puramente conversacional para um modelo operacional, no qual a IA participa de um fluxo de trabalho [@yao2022react].

 Em muitas arquiteturas agentic, o LLM funciona como o "cérebro" do sistema. Ele não executa diretamente todas as operações, mas interpreta o objetivo, decide o próximo passo e produz instruções para outros componentes. Esses componentes podem incluir mecanismos de busca, bancos vetoriais, APIs externas, interpretadores de código, sistemas de arquivos, planilhas, navegadores e módulos de memória. O LLM, portanto, assume um papel de coordenação cognitiva: raciocina sobre o problema e delega ações a ferramentas ou a outros agentes especializados.

 Essa distinção é importante. Um chatbot tradicional tende a transformar uma entrada em uma saída textual. Já um sistema agente precisa manter estado, avaliar contexto, considerar restrições e operar em várias etapas. Em um assistente acadêmico, por exemplo, a aplicação pode precisar: interpretar a pergunta do estudante, buscar referências, comparar fontes, organizar um plano de resposta, gerar a explicação e revisar o resultado final. Um único prompt raramente oferece robustez suficiente para isso.

 ### LLMs como "cérebros" do processamento

 Quando se diz que o LLM é o cérebro de um sistema, a ideia central não é que ele seja o único componente inteligente, mas que ele é o mecanismo de tomada de decisão de alto nível. Esse cérebro textual recebe um estado parcial do problema e produz algo como:

 - uma interpretação do objetivo;
 - uma hipótese sobre o que falta para concluir a tarefa;
 - uma decisão sobre qual ferramenta ou agente deve ser acionado;
 - uma síntese intermediária para alimentar a próxima etapa.

 Em uma arquitetura bem projetada, o LLM não deve ser usado para tudo. Operações determinísticas, como cálculos, validações formais, acesso a banco de dados, leitura de arquivos ou chamadas HTTP, costumam ser delegadas a ferramentas externas. Isso reduz alucinações e melhora a confiabilidade. O papel do LLM concentra-se em atividades como planejamento, classificação, interpretação semântica, transformação de linguagem e coordenação.

 Essa abordagem também favorece a modularidade. Se o modelo principal for trocado, as ferramentas podem permanecer as mesmas. Se uma ferramenta falhar, o cérebro pode escolher uma rota alternativa. Essa separação entre cognição linguística e execução operacional é uma das ideias centrais da engenharia de agentes contemporânea.

 ### Sistemas multiagentes com LLMs

 Um passo além do agente único é o sistema multiagente. Nesse cenário, em vez de um único LLM central lidar com tudo, a aplicação distribui o trabalho entre vários agentes especializados. Cada agente pode ter um papel bem definido, um conjunto reduzido de ferramentas e até um prompt de sistema diferente. Um agente pode ser responsável por pesquisar informações, outro por escrever, outro por validar coerência, e outro por supervisionar o fluxo geral.

 Essa organização segue um princípio próximo ao da divisão de trabalho. Em vez de pedir a um único modelo que seja pesquisador, planejador, executor e revisor ao mesmo tempo, o sistema cria papéis explícitos. Isso tende a melhorar controle, auditabilidade e manutenção. Frameworks como LangGraph e CrewAI popularizaram essa organização ao permitir a orquestração de agentes com estados, rotas e pontos de verificação [@langgraph_docs].

 Um sistema multiagente típico pode conter os seguintes papéis:

 - **Supervisor**: recebe a meta geral e decide qual agente atua a seguir.
 - **Pesquisador**: consulta bases externas, documentos ou sistemas RAG.
 - **Executor**: usa ferramentas para calcular, ler arquivos ou acionar APIs.
 - **Redator**: produz a resposta final em linguagem natural.
 - **Crítico/Avaliador**: verifica qualidade, cobertura e possíveis erros.

 A vantagem principal dessa decomposição é que o sistema passa a explicitar responsabilidades. Se a resposta final estiver incompleta, o problema pode estar no pesquisador. Se houver erro de roteamento, o supervisor é o ponto de inspeção. Em aplicações reais, esse desenho é valioso porque facilita observabilidade, testes e refinamento incremental.

 O diagrama a seguir representa uma arquitetura simplificada de sistema multiagente com LLMs:

 ```mermaid
 flowchart LR
     U[Usuario] --> S[Agente Supervisor\nLLM roteador]
     S --> P[Agente Pesquisador\nRAG e busca]
     S --> E[Agente Executor\nFerramentas e APIs]
     S --> R[Agente Redator\nSintese da resposta]
     P --> M[(Memoria e documentos)]
     E --> T[(Tools externas)]
     P --> S
     E --> S
     R --> S
     S --> F[Resposta final]
 ```

 Em termos conceituais, o LLM continua sendo o motor cognitivo de cada agente. O que muda é que o processamento deixa de ser monolítico e passa a ser distribuído entre unidades especializadas. Isso é especialmente útil em tarefas longas, ambíguas ou que exigem diferentes tipos de competência, como levantamento bibliográfico, análise de dados, escrita técnica e revisão de consistência.

 ### Reasoning em LLMs

 No contexto dos modelos de linguagem, o termo *reasoning* refere-se à capacidade de produzir respostas por meio de etapas intermediárias de inferência, e não apenas pela associação superficial entre padrões de texto. Em problemas simples, um LLM pode responder diretamente. Em problemas mais complexos, porém, a resposta costuma exigir decomposição, comparação de alternativas, verificação de restrições e combinação de fatos.

 É importante notar que o reasoning em LLMs não deve ser interpretado automaticamente como raciocínio humano no sentido filosófico forte. Do ponto de vista computacional, o que se observa é um comportamento emergente em que o modelo produz sequências textuais intermediárias que ajudam a chegar a uma solução. Essas sequências podem assumir a forma de planos, hipóteses, passos de cálculo, autoexplicações ou decisões sobre qual ferramenta usar.

 Em aplicações agentic, reasoning tem uma função prática decisiva. Antes de agir, o agente precisa responder perguntas como: o que falta saber, qual fonte consultar, vale a pena chamar uma ferramenta, o problema precisa ser quebrado em subtarefas, já há evidência suficiente para responder? O padrão ReAct formaliza exatamente essa alternância entre raciocinar e agir, articulando uma sequência de pensamento e execução [@yao2022react].

 O reasoning também pode aparecer em estratégias mais deliberativas, como geração de múltiplos caminhos de solução e escolha posterior do melhor. Trabalhos como *Self-Consistency* e *Tree of Thoughts* exploram esse tipo de aprofundamento ao mostrar que, em vez de seguir apenas uma única trilha de raciocínio, o modelo pode avaliar várias possibilidades antes de decidir [@wang2022selfconsistency; @yao2023tree].

 ### Chain of Thought

 A técnica de *Chain of Thought* (CoT) consiste em induzir o modelo a explicitar passos intermediários de raciocínio antes de apresentar a resposta final [@wei2022chain]. Na prática, isso significa orientar o modelo para decompor a tarefa em uma sequência de pequenas decisões. Em vez de responder apenas com o resultado, o sistema passa a estruturar algo próximo de um "passo a passo" textual.

 Essa estratégia é particularmente útil em problemas que envolvem lógica, matemática, planejamento, diagnóstico ou interpretação de várias restrições simultâneas. Ao externalizar etapas intermediárias, o modelo ganha mais espaço para organizar a solução e reduzir erros de salto lógico. Um exemplo conceitual seria:

 1. Identificar o que o problema pede.
 2. Separar os dados relevantes.
 3. Escolher uma estratégia de resolução.
 4. Executar cada passo.
 5. Conferir se o resultado atende ao enunciado.

 Em termos pedagógicos, Chain of Thought é valioso porque aproxima o funcionamento do sistema de um processo explicável. Os estudantes conseguem perceber que muitas tarefas não dependem apenas da resposta correta, mas da organização do percurso até ela. Isso também ajuda a compreender por que agentes baseados em LLM frequentemente mantêm estados intermediários, planos parciais e registros de decisão.

 Ainda assim, é importante fazer uma distinção. O conceito de CoT descreve uma técnica de prompting ou estruturação da inferência; ele não garante, por si só, que o raciocínio esteja correto. Um modelo pode produzir uma cadeia de passos plausível e ainda assim chegar a uma conclusão errada. Por isso, arquiteturas robustas normalmente combinam CoT com verificação externa, uso de ferramentas e mecanismos de revisão.

 Em muitos sistemas modernos, a cadeia de pensamento completa não é necessariamente exibida ao usuário final. Em aplicações de produção, é comum manter apenas resumos estruturados do raciocínio, logs de decisão ou evidências verificáveis, evitando exposição desnecessária de passos internos. O ponto central, do ponto de vista de engenharia, é que o sistema utilize etapas intermediárias para melhorar desempenho e controle.

 ### Relação entre CoT, ReAct e sistemas multiagentes

 É útil distinguir esses três conceitos:

 - **Chain of Thought**: enfatiza a decomposição textual do raciocínio.
 - **ReAct**: combina raciocínio com ações concretas sobre ferramentas e ambiente [@yao2022react].
 - **Sistemas multiagentes**: distribuem raciocínio e ação entre papéis especializados.

 Em outras palavras, Chain of Thought ajuda um agente a pensar melhor; ReAct ajuda o agente a pensar e agir; sistemas multiagentes ajudam a distribuir esse pensar e agir entre diferentes unidades. Essas ideias não competem entre si. Pelo contrário, costumam aparecer combinadas em arquiteturas reais.

 Considere, por exemplo, um sistema para produzir um relatório técnico. O supervisor pode usar reasoning para decidir a ordem das etapas. O pesquisador pode usar ReAct para consultar bases documentais e ferramentas. O redator pode usar Chain of Thought para organizar a explicação. Um agente avaliador pode verificar inconsistências antes da entrega final. O resultado é um fluxo com maior especialização e, em muitos casos, maior confiabilidade.

 Alguns exemplos conhecidos de ecossistemas e abordagens relacionados a esse campo incluem:

 - **Auto-GPT**: sistema baseado em GPT que busca executar metas em várias iterações.
 - **BabyAGI**: organiza tarefas em fila, com priorização e memória de trabalho.
 - **LangChain Agents**: abstrações para agentes com ferramentas e fluxos condicionais.
 - **CrewAI**: coordena múltiplos agentes colaborativos com papéis distintos.
 - **LangGraph**: permite definir fluxos de execução com memória, estados e reações a falhas [@langgraph_docs].

 Em síntese, a evolução de chatbots para agentes e, depois, para sistemas multiagentes marca uma mudança importante na IA generativa contemporânea. O foco deixa de estar apenas na geração de texto e passa a incluir coordenação, planejamento, uso de ferramentas, memória e colaboração entre componentes. É esse movimento que torna os LLMs úteis não apenas como geradores de linguagem, mas como núcleos de processamento em sistemas mais complexos.



## Model Context Protocol


O Model Context Protocol (MCP) é um protocolo emergente proposto para padronizar a maneira como modelos de linguagem e sistemas de IA generativa compartilham e mantêm contexto de interação entre múltiplas chamadas, sessões e até mesmo entre diferentes ferramentas ou agentes. Sua criação parte da necessidade crescente de dotar modelos de memória, rastreamento de estado e interoperabilidade em fluxos complexos de interação com usuários e sistemas.

Tradicionalmente, os modelos de linguagem funcionam como caixas pretas *stateless*, ou seja, a cada prompt recebido, o modelo responde sem conhecimento direto de interações anteriores (a não ser que o histórico seja embutido manualmente no prompt). Isso limita a continuidade e a personalização de aplicações mais avançadas, como assistentes autônomos, agentes multitarefa e workflows dinâmicos.

O MCP busca resolver esse desafio criando uma camada de abstração que separa o “contexto conversacional” do modelo da aplicação que o utiliza. Em vez de tratar cada prompt como isolado, o protocolo define regras e formatos para armazenar, referenciar e transportar elementos importantes do contexto, como:

- Histórico de interações
- Tarefas pendentes
- Ferramentas disponíveis para o agente
- Identidade e preferências do usuário
- Planos, metas ou objetivos do agente
- Memórias de longo prazo (armazenadas externamente)

Basicamente o objetivo do protocolo envolve quatro importantes aspectos do uso de grandes modelos de linguagem.

- **Persistência de contexto:** garantir que os modelos possam manter continuidade entre sessões.
- **Portabilidade**: permitir que diferentes sistemas ou agentes compartilhem estado de forma padronizada.
- **Modularidade**: tornar mais fácil substituir ou compor modelos e componentes de IA com interoperabilidade.
- Segurança e **rastreabilidade**: registrar decisões e transições de estado com maior controle.


!!! Important "Quais são as implicações éticas do uso da IA"
    Sugiro a leitura do artigo [The Malicious Use of AI](https://arxiv.org/abs/1802.07228)


