# Guia Prático: Integrando **TypeORM** com **PostgreSQL** em um projeto Node.js/TypeScript existente

> **Objetivo**: incorporar o TypeORM a um projeto existente (Node.js + TypeScript) usando PostgreSQL, com configuração via `dotenv`, migrações, repositórios, seed de dados e boas práticas de organização.

---

## 1) Pré‑requisitos

- Node.js LTS (18+ recomendado) e npm ou pnpm/yarn.
- PostgreSQL instalado e com um banco criado (ex.: `app_db`).
- Projeto Node.js **já iniciado** (com `package.json`) e preferencialmente TypeScript.
- Credenciais de banco: host, porta, usuário, senha e nome do database.

> Se ainda não usa TypeScript, instale e inicialize rapidamente:
```bash
npm i -D typescript ts-node @types/node
npx tsc --init
```
No `tsconfig.json`, habilite (recomendado):
```jsonc
{
  "target": "ES2020",
  "module": "CommonJS",
  "rootDir": "src",
  "outDir": "dist",
  "esModuleInterop": true,
  "experimentalDecorators": true,
  "emitDecoratorMetadata": true,
  "strict": true,
  "skipLibCheck": true
}
```

> **Observação**: `emitDecoratorMetadata` depende do pacote `reflect-metadata` (ver adiante).

---

## 2) Instalar dependências

```bash
npm i typeorm reflect-metadata pg
npm i -D ts-node ts-node-dev @types/node
```

- `typeorm`: ORM principal
- `reflect-metadata`: requerido para decorators
- `pg`: driver PostgreSQL
- `ts-node-dev` (ou `nodemon`): para rodar em dev com TS

No início do seu entrypoint (ex.: `src/index.ts`), importe o `reflect-metadata` **antes** de usar qualquer decorator:
```ts
import "reflect-metadata";
```

---

## 3) Variáveis de ambiente

Instale `dotenv` (opcional, mas recomendado):
```bash
npm i dotenv
```

Crie um arquivo `.env` na raiz:
```env
# Banco
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=app_db

# App
NODE_ENV=development
```

Carregue `.env` no começo do seu entrypoint **ou** na configuração do DataSource:
```ts
import "reflect-metadata";
import * as dotenv from "dotenv";
dotenv.config();
```

---

## 4) Estrutura de pastas sugerida

```
.
├─ src/
│  ├─ data/
│  │  ├─ datasource.ts
│  │  ├─ migrations/
│  │  └─ seeds/
│  ├─ entities/
│  │  └─ User.ts
│  ├─ repositories/
│  │  └─ UserRepository.ts
│  ├─ services/
│  ├─ routes/
│  ├─ index.ts
│  └─ app.ts
├─ ormconfig.ts (opcional – hoje recomenda-se DataSource programático)
├─ .env
├─ tsconfig.json
└─ package.json
```

---

## 5) Criar o **DataSource** do TypeORM (recomendado)

Arquivo `src/data/datasource.ts`:
```ts
import "reflect-metadata";
import { DataSource } from "typeorm";
import * as dotenv from "dotenv";
dotenv.config();

export const AppDataSource = new DataSource({
  type: "postgres",
  host: process.env.DB_HOST,
  port: Number(process.env.DB_PORT) || 5432,
  username: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME,
  synchronize: false, // use migrações em produção!
  logging: process.env.NODE_ENV !== "production",
  entities: [__dirname + "/../entities/*.{ts,js}"],
  migrations: [__dirname + "/migrations/*.{ts,js}"],
  subscribers: [],
});
```

> **`synchronize` falso em prod**: evita alterações automáticas destrutivas. Use **migrações**.

No `src/index.ts` (bootstrap da aplicação):
```ts
import "reflect-metadata";
import * as dotenv from "dotenv";
dotenv.config();

import { AppDataSource } from "./data/datasource";
import { startServer } from "./app";

AppDataSource.initialize()
  .then(async () => {
    console.log("📦 DataSource inicializado.");
    await startServer();
  })
  .catch((err) => {
    console.error("Erro ao inicializar DataSource:", err);
    process.exit(1);
  });
```

Exemplo simplificado de `src/app.ts`:
```ts
import express from "express";

export async function startServer() {
  const app = express();
  app.use(express.json());

  app.get("/health", (_req, res) => res.json({ ok: true }));

  const port = process.env.PORT || 3000;
  return new Promise<void>((resolve) => {
    app.listen(port, () => {
      console.log(`🚀 Server on http://localhost:${port}`);
      resolve();
    });
  });
}
```

---

## 6) Definir uma entidade

`src/entities/User.ts`:
```ts
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, Index, Unique } from "typeorm";

@Entity({ name: "users" })
@Unique(["email"])
export class User {
  @PrimaryGeneratedColumn("uuid")
  id!: string;

  @Column({ length: 120 })
  name!: string;

  @Index()
  @Column({ length: 180 })
  email!: string;

  @Column({ select: false }) // evita retornar o hash por padrão
  passwordHash!: string;

  @CreateDateColumn({ type: "timestamp with time zone" })
  createdAt!: Date;

  @UpdateDateColumn({ type: "timestamp with time zone" })
  updatedAt!: Date;
}
```

---

## 7) Criar e rodar migrações

### 7.1) Script CLI do TypeORM (ts-node)
Adicione scripts no `package.json`:
```jsonc
{
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts",
    "typeorm": "ts-node ./node_modules/typeorm/cli.js",
    "migration:generate": "npm run typeorm -- migration:generate src/data/migrations/InitSchema -d src/data/datasource.ts",
    "migration:run": "npm run typeorm -- migration:run -d src/data/datasource.ts",
    "migration:revert": "npm run typeorm -- migration:revert -d src/data/datasource.ts"
  }
}
```

> O parâmetro `-d` indica o arquivo `DataSource`.

### 7.2) Gerar a primeira migração
```bash
npm run migration:generate
```
Isso criará um arquivo em `src/data/migrations/XXXXXXXXXXXX-InitSchema.ts` com o SQL baseado nas entidades.

### 7.3) Rodar migrações
```bash
npm run migration:run
```
Para desfazer a última:
```bash
npm run migration:revert
```

---

## 8) Repositórios e consultas

### 8.1) Usando o repositório padrão
```ts
import { AppDataSource } from "../data/datasource";
import { User } from "../entities/User";

const userRepo = AppDataSource.getRepository(User);

export async function createUser(input: { name: string; email: string; passwordHash: string; }) {
  const user = userRepo.create(input);
  return await userRepo.save(user);
}

export async function getUserByEmail(email: string) {
  return await userRepo.findOne({ where: { email } });
}
```

### 8.2) Query Builder (joins, filtros complexos)
```ts
import { AppDataSource } from "../data/datasource";
import { User } from "../entities/User";

export async function searchUsers(term: string) {
  return AppDataSource.getRepository(User)
    .createQueryBuilder("u")
    .where("u.name ILIKE :term OR u.email ILIKE :term", { term: `%${term}%` })
    .orderBy("u.createdAt", "DESC")
    .getMany();
}
```

---

## 9) Transações

```ts
import { AppDataSource } from "../data/datasource";
import { User } from "../entities/User";

export async function createUserTransactional(input: { name: string; email: string; passwordHash: string; }) {
  return AppDataSource.transaction(async (manager) => {
    const repo = manager.getRepository(User);
    const user = repo.create(input);
    const saved = await repo.save(user);

    // faça outras operações atômicas aqui…

    return saved;
  });
}
```

> Para **isolamento** ou **locking**, utilize `queryRunner` e comandos específicos quando necessário.

---

## 10) Seeds (dados iniciais)

`src/data/seeds/seed.ts`:
```ts
import "reflect-metadata";
import * as dotenv from "dotenv";
dotenv.config();

import { AppDataSource } from "../datasource";
import { User } from "../../entities/User";
import { randomUUID } from "crypto";

async function run() {
  await AppDataSource.initialize();
  const repo = AppDataSource.getRepository(User);

  const exists = await repo.count();
  if (exists === 0) {
    await repo.insert([
      { id: randomUUID(), name: "Admin", email: "admin@example.com", passwordHash: "HASH" },
      { id: randomUUID(), name: "Diego", email: "diego@example.com", passwordHash: "HASH" }
    ]);
    console.log("✅ Seed inserido.");
  } else {
    console.log("ℹ️ Seed ignorado (tabela não vazia).");
  }

  await AppDataSource.destroy();
}

run().catch((e) => {
  console.error(e);
  process.exit(1);
});
```

No `package.json`:
```jsonc
{
  "scripts": {
    "seed": "ts-node src/data/seeds/seed.ts"
  }
}
```

---

## 11) Boas práticas e dicas

- **Desabilite `synchronize` em produção** e confie em **migrações versionadas**.
- **Versione** o diretório `migrations/` no Git.
- Separe **camadas**: `entities/`, `repositories/`, `services/`, `routes/`.
- **Selecione campos sensíveis** com cuidado (`select: false` para hashes/tokens).
- Ative **logs** em dev e monitore queries lentas.
- Para **paginação**, use `take`/`skip` ou paginação por cursor no QueryBuilder.
- Em **NestJS**, use o `@nestjs/typeorm` e a injeção de repositórios via `forRootAsync`/`forFeature`.
- Em **testes**, prefira um banco isolado (ex.: Docker + `docker-compose`), e rode `migration:run` no setup.

---

## 12) Exemplo de docker-compose (opcional)

`docker-compose.yml`:
```yaml
version: "3.9"
services:
  db:
    image: postgres:16
    container_name: app_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: app_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 10
volumes:
  pgdata: {}
```

---

## 13) Scripts úteis no `package.json` (consolidado)

```jsonc
{
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts",
    "typeorm": "ts-node ./node_modules/typeorm/cli.js",
    "migration:generate": "npm run typeorm -- migration:generate src/data/migrations/InitSchema -d src/data/datasource.ts",
    "migration:run": "npm run typeorm -- migration:run -d src/data/datasource.ts",
    "migration:revert": "npm run typeorm -- migration:revert -d src/data/datasource.ts",
    "seed": "ts-node src/data/seeds/seed.ts",
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```

---

## 14) Referências e leituras recomendadas

- **TypeORM Docs**: https://typeorm.io
- **Patterns**: Repository, Data Mapper, Active Record (no próprio site do TypeORM)
- **PostgreSQL**: https://www.postgresql.org/docs/
- **Migrations** (TypeORM CLI): seção *Migrations* na documentação
- **NestJS + TypeORM** (se aplicável): https://docs.nestjs.com/techniques/database

---

### ✅ Resultado

Com esses passos você incorpora o **TypeORM** ao seu projeto existente, com um fluxo completo: **DataSource programático + entidades + migrações + repositórios + transações + seed** — pronto para desenvolvimento e produção.
