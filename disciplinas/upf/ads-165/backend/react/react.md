Instalar react e criar app

```typescript
npx create-react-app meu-front --template typescript
```

Instalar axios
```typescript
npm install axios
``` 


Exemplo de arquivo src/services/api.ts:

```typescript

export const api = axios.create({
  baseURL: "http://localhost:4000", // URL da sua API Express
});
```

4. Faça login e salve o token JWT
Exemplo de componente de login:

```typescript
import { useState } from "react";
import { api } from "./services/api";

function Login() {
  const [cpf_cnpj, setCpfCnpj] = useState("");
  const [senha, setSenha] = useState("");
  const [token, setToken] = useState("");

  const handleLogin = async () => {
    const resp = await api.post("/auth/login", { cpf_cnpj, senha });
    setToken(resp.data.token);
    localStorage.setItem("token", resp.data.token);
  };

  return (
    <div>
      <input value={cpf_cnpj} onChange={e => setCpfCnpj(e.target.value)} />
      <input type="password" value={senha} onChange={e => setSenha(e.target.value)} />
      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
}

export default Login;
 
```

Use o token para acessar rotas protegidas
Exemplo de requisição autenticada:

```typescript
const token = localStorage.getItem("token");
const resp = await api.get("/usuarios", {
  headers: { Authorization: `Bearer ${token}` }
});
```

Link show para desenvolvimento para web.


https://www.cloudflare.com/pt-br/learning/ssl/what-is-a-session-key/