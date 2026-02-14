```shell
npm install jsonwebtoken @types/jsonwebtoken bcryptjs @types/bcryptjs
```

Crie um endpoint de login para gerar o token


```typescript
import { Router, Request, Response } from "express";
import jwt from "jsonwebtoken";
import bcrypt from "bcryptjs";
// ...import seu modelo de usuário...

const router = Router();

router.post("/login", async (req: Request, res: Response) => {
    const { cpf_cnpj, senha } = req.body;
    // Busque o usuário no banco de dados
    const usuario = await UsuarioRepository.findOneBy({ cpf_cnpj });
    if (!usuario) return res.status(401).json({ error: "Usuário não encontrado" });

    // Verifique a senha
    const senhaValida = await bcrypt.compare(senha, usuario.senha);
    if (!senhaValida) return res.status(401).json({ error: "Senha inválida" });

    // Gere o token JWT
    const token = jwt.sign(
        { id: usuario.id, cpf_cnpj: usuario.cpf_cnpj },
        process.env.JWT_SECRET as string,
        { expiresIn: "1h" }
    );
    res.json({ token });
});

export default router;
```
3. Crie um middleware para proteger rotas

```typescript
import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

export function autenticarJWT(req: Request, res: Response, next: NextFunction) {
    const authHeader = req.headers.authorization;
    if (!authHeader) return res.status(401).json({ error: "Token não informado" });

    const token = authHeader.split(" ")[1];
    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET as string);
        (req as any).usuario = payload;
        next();
    } catch {
        return res.status(401).json({ error: "Token inválido" });
    }
}

```


4. Proteja suas rotas

```typescript
// ...existing code...
import authRoutes from "./routes/auth";
import { autenticarJWT } from "./middleware/auth";

app.use("/auth", authRoutes);

// Exemplo de rota protegida
app.get("/usuarios", autenticarJWT, async (req, res) => {
    // ...código para retornar usuários...
});
// ...existing code...
```

ou aplicar ao router
```typescript
import { Router } from "express";
import { autenticarJWT } from "../middleware/auth";

const router = Router();

// Aplica o middleware a todas as rotas deste router
router.use(autenticarJWT);

router.get("/", async (req, res) => {
    // ...código para retornar usuários...
});

export default router;

```
