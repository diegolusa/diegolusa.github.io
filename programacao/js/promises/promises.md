---
title: "Promises"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---



Promises são uma abstração em JavaScript para representar operações assíncronas, permitindo que o código trabalhe com resultados de operações que podem ainda não estar disponíveis. Elas ajudam a evitar o famoso "callback hell" e a escrever código mais legível e manejável.  

### Conceitos Básicos

Uma promise é um objeto que representa a eventual conclusão (ou falha) de uma operação assíncrona e seu valor resultante. Uma promise pode estar em um dos três estados:

- **Pending (Pendente)**: Estado inicial, que não foi realizada nem rejeitada.
- **Fulfilled (Realizada)**: A operação foi concluída com sucesso.
- **Rejected (Rejeitada)**: A operação falhou.


Para criar uma promise, utilizamos o construtor `Promise` que aceita uma função de executor com dois parâmetros: `resolve` e `reject`.

```javascript
const minhaPromise = new Promise((resolve, reject) => {
  // Operação assíncrona
  let sucesso = true;

  if (sucesso) {
    resolve("Operação realizada com sucesso!");
  } else {
    reject("Operação falhou.");
  }
});
```

Já para tratar do resultado de uma promise, usamos os métodos `then`, `catch` e `finally`.

- `then`

O método `then` é utilizado para lidar com o sucesso da promise.

```javascript
minhaPromise.then((valor) => {
  console.log(valor); // "Operação realizada com sucesso!"
});
```

- `catch`

O método `catch` é usado para lidar com a falha da promise.

```javascript
minhaPromise.catch((erro) => {
  console.log(erro); // "Operação falhou."
});
```

- `finally`

O método `finally` é chamado quando a promise é concluída, independente de ser realizada ou rejeitada.

```javascript
minhaPromise.finally(() => {
  console.log("Operação concluída."); // Será executado sempre
});
```



## Função `fetch`

A função `fetch` permite fazer requisições HTTP assíncronas para acessar e manipular recursos pela rede. Ela retorna uma `Promise` que resolve com a resposta da requisição, facilitando o trabalho com dados de APIs, servidores e outros recursos web [@dofetch2024].


### Sintaxe

```javascript
fetch(url, [options])
```

- `url` (obrigatório): O recurso que deseja buscar.
- `options` (opcional): Um objeto contendo qualquer um dos seguintes parâmetros:

Alguns dos possível valores para `options` são:

- **method**: O método HTTP a ser usado (e.g., `GET`, `POST`, `PUT`, `DELETE`). O padrão é `GET`.
- **headers**: Um objeto contendo cabeçalhos HTTP a serem enviados com a requisição.
- **body**: O corpo da requisição. Pode ser uma string, um objeto, um `FormData`, etc.
- **mode**: O modo da requisição (e.g., `cors`, `no-cors`, `same-origin`).
- **credentials**: Indica se os cookies devem ser enviados com a requisição (`omit`, `same-origin`, `include`).
- **cache**: O modo de cache (e.g., `default`, `no-store`, `reload`, `no-cache`, `force-cache`, `only-if-cached`).
- **redirect**: O modo de redirecionamento (`follow`, `error`, `manual`).
- **referrer**: Referrer da requisição (`client`, URL, ou vazio).
 

### Exemplos de Uso

#### Requisição Simples (GET)

```javascript
fetch('https://api.exemplo.com/dados')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
```

#### Requisição com Parâmetros (POST)

```javascript
fetch('https://api.exemplo.com/dados', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    chave: 'valor'
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
```

### Tratamento da Resposta

O objeto `Response` retornado pela `fetch` possui diversos métodos para processar os dados da resposta:

- **text()**: Retorna uma `Promise` que resolve com o corpo da resposta como uma string.
- **json()**: Retorna uma `Promise` que resolve com o corpo da resposta como um objeto JSON.
- **blob()**: Retorna uma `Promise` que resolve com o corpo da resposta como um Blob.
- **formData()**: Retorna uma `Promise` que resolve com o corpo da resposta como um FormData.
- **arrayBuffer()**: Retorna uma `Promise` que resolve com o corpo da resposta como um ArrayBuffer.

#### Exemplo: Processar Resposta JSON

```javascript
fetch('https://api.exemplo.com/dados')
  .then(response => {
    if (!response.ok) {
      throw new Error('Erro na rede: ' + response.statusText);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
```

!!! info "Dica"
    Podemos utilizar o serviço [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) para consumir uma API e testar nosso código com Promises.



