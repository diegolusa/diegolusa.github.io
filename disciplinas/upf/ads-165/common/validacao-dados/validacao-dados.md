# Fundamentos e Boas Práticas de Validação de Dados com Zod

Validação de dados é o processo de **verificar se os valores recebidos por um sistema estão no formato e tipo esperado**, antes de serem utilizados. A validação pode ocorrer tanto na camada de backend quanto de frontend, a depender da arquitetura da aplicação.

Além de garantir a consistência dos dados, a validação é o primeiro filtro de segurança para proteger a aplicação de ataques clássicos, como *sql injection*, *Cross-Site Scripting*, **Command Injection** e **Denial of Service**.


No ecossistema JavaScript/TypeScript temos diversas bibliotecas para realizar a tarefa de validação. Talvez as bibliotecas [Zod](https://zod.dev/) e [Yup](https://github.com/jquense/yup) sejam as mais populares. Na sequência, iremos conhecer um pouco da biblioteca **Zod**.



## Explorando a biblioteca Zod

**Zod** é uma biblioteca TypeScript-first para **validação e tipagem de dados**. Com ela podemos realizar operações sofisticadas de validação de dados, como por exemplo:

- Criar **schemas** (modelos) que descrevem a forma e os tipos dos dados.  
- Validar dados em tempo de execução.  
- Inferir automaticamente tipos TypeScript a partir dos schemas.  


Como de praxe, o primeiro passo compreende instalar a biblioteca em nosso projeto.

```bash
npm install zod
```

A primeira etapa consiste em criar *schemas*, ou seja, abstrações da estrutura e regras de validação associadas a cada atributo/objeto.


---

## 3. 🔠 Criando seu primeiro schema

```ts
import { z } from "zod";

const usuarioSchema = z.object({
  nome: z.string(),
  idade: z.number(),
});

const usuario = {
  nome: "Maria",
  idade: 25,
};

usuarioSchema.parse(usuario); // ✅ Válido
```

Se o dado não corresponder ao schema, o Zod lançará um erro:

```ts
usuarioSchema.parse({ nome: "Maria", idade: "25" });
// ❌ Erro: idade deve ser um número
```

---

## 4. 🧱 Tipos básicos suportados

Zod oferece validação para os principais tipos nativos:

| Tipo | Exemplo |
|------|----------|
| `z.string()` | Texto simples |
| `z.number()` | Números inteiros ou decimais |
| `z.boolean()` | Verdadeiro/Falso |
| `z.date()` | Objetos Date |
| `z.array(schema)` | Arrays tipados |
| `z.enum([...])` | Valores limitados a um conjunto fixo |
| `z.object({...})` | Estruturas de objetos |
| `z.union([...])` | Aceita múltiplos tipos |

### Exemplo:
```ts
const produtoSchema = z.object({
  nome: z.string(),
  preco: z.number().positive(),
  categorias: z.array(z.string()),
  disponivel: z.boolean().default(true),
});
```

---

## 5. 🎯 Refinamentos e validações customizadas

Podemos adicionar **regras específicas** com `.refine()` ou `.min()`, `.max()`, `.email()`, etc.

```ts
const senhaSchema = z
  .string()
  .min(8, "A senha deve ter no mínimo 8 caracteres")
  .refine((senha) => /[A-Z]/.test(senha), "A senha deve ter uma letra maiúscula");
```

💡 **Boa prática:** usar mensagens claras para o usuário final.

---

## 6. 🔄 Validando dados externos (ex: APIs)

Em aplicações **Next.js ou Express**, Zod é excelente para validar dados vindos de requisições HTTP.

### Exemplo com Express:
```ts
import express from "express";
import { z } from "zod";

const app = express();
app.use(express.json());

const userSchema = z.object({
  nome: z.string(),
  email: z.string().email(),
  idade: z.number().int().min(18),
});

app.post("/users", (req, res) => {
  try {
    const data = userSchema.parse(req.body);
    res.json({ message: "Usuário válido!", data });
  } catch (error) {
    res.status(400).json(error);
  }
});

app.listen(3000, () => console.log("API rodando 🚀"));
```

---

## 7. 💬 Métodos de validação

| Método | Descrição |
|---------|-------------|
| `.parse(data)` | Valida e lança erro se inválido |
| `.safeParse(data)` | Retorna `{ success, data | error }` |
| `.refine(fn)` | Aplica regra customizada |
| `.optional()` | Campo opcional |
| `.nullable()` | Permite `null` |

### Exemplo com `safeParse`
```ts
const resultado = userSchema.safeParse({ nome: "Ana", idade: 16 });

if (!resultado.success) {
  console.log(resultado.error.format());
} else {
  console.log(resultado.data);
}
```

---

## 8. 🧠 Inferindo tipos com TypeScript

O Zod gera automaticamente o tipo correspondente ao schema:

```ts
const usuarioSchema = z.object({
  nome: z.string(),
  idade: z.number(),
});

type Usuario = z.infer<typeof usuarioSchema>;

const novoUsuario: Usuario = { nome: "Carlos", idade: 21 };
```

💡 Isso elimina a duplicação entre “modelo de validação” e “interface TypeScript”.

---

## 9. 🧩 Validação de formulários com React Hook Form

Zod se integra perfeitamente com **React Hook Form**, permitindo validação tipada no frontend.

```bash
npm install react-hook-form @hookform/resolvers
```

```tsx
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const formSchema = z.object({
  nome: z.string().min(3, "O nome é obrigatório"),
  email: z.string().email("E-mail inválido"),
});

type FormData = z.infer<typeof formSchema>;

export function Formulario() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
    resolver: zodResolver(formSchema),
  });

  function onSubmit(data: FormData) {
    console.log(data);
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("nome")} placeholder="Nome" />
      {errors.nome && <p>{errors.nome.message}</p>}

      <input {...register("email")} placeholder="E-mail" />
      {errors.email && <p>{errors.email.message}</p>}

      <button type="submit">Enviar</button>
    </form>
  );
}
```

---

## 10. ⚙️ Transformações de dados

Além de validar, o Zod pode **transformar valores** antes de retorná-los:

```ts
const schema = z.object({
  preco: z.string().transform((val) => parseFloat(val)),
});

const produto = schema.parse({ preco: "19.99" });
console.log(produto.preco); // number → 19.99
```

---

## 11. 🔐 Boas práticas de validação

| Boas práticas | Descrição |
|----------------|------------|
| ✅ **Validar na entrada** | Valide dados assim que chegam (ex: `req.body`, `query`, `params`). |
| 🚫 **Nunca confie no cliente** | Sempre valide no backend, mesmo que o frontend já valide. |
| 🧱 **Centralize schemas** | Crie uma pasta `/schemas` e compartilhe entre frontend e backend. |
| 🧩 **Reutilize schemas** | Evite duplicação — use o mesmo schema para criação e edição. |
| 🧠 **Combine com TypeScript** | Use `z.infer` para garantir tipagem consistente. |
| 🧰 **Trate erros claramente** | Retorne mensagens amigáveis para o usuário final. |

---

## 12. 💪 Exercícios práticos

1. Crie um schema `produtoSchema` com:
   - nome: string obrigatória  
   - preço: número positivo  
   - estoque: número inteiro opcional  
   - categoria: enum com valores "Eletrônicos", "Roupas", "Alimentos"  

2. Valide uma lista de produtos (array).  
3. Aplique validação em uma rota POST `/produtos` com Express.  
4. (Desafio) Transforme strings numéricas em números usando `.transform()`.

---

## 13. 📚 Recursos recomendados

- [Documentação oficial do Zod](https://zod.dev/)  
- [Integração com React Hook Form](https://react-hook-form.com/get-started#SchemaValidation)  
- [Zod vs Yup — Comparativo](https://dev.to/ghazalpak/zod-vs-yup-validation-in-typescript-2gaj)  
- [TypeScript Handbook – Tipagem avançada](https://www.typescriptlang.org/docs/)  

---

## ✅ Conclusão

Zod simplifica a validação de dados, tornando o código **mais seguro, previsível e tipado**.  
Com ele, evitamos erros em tempo de execução e melhoramos a **integração entre frontend e backend**.

> 🔑 Lembre-se: validar dados **é uma forma de segurança e qualidade de software**, não apenas um detalhe técnico.
