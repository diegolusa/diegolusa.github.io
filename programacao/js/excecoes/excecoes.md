---
title: "Tratamento de Exceções"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---

O tratamento de exceções é feito usando blocos `try...catch`. O bloco `try` corresponde ao conjunto de instruções que podem lançar exceções. Os blocos `catch`, por sua vez, permitem adicionar instruções a ser executadas caso o erro em questão seja lançado. Opcionalmente podemos colocar o bloco `finally` na estrutura, o qual executará em todos os cenários (com ou sem lançamento da exceção).

```javascript
try {
   var x = y / 0;
} catch (erro) {
  console.log("Ocorreu um erro: " + erro.message);
} finally {
  console.log("Este bloco sempre será executado.");
}
```

[Aqui](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) você pode encontrar a lista de exceções globais da linguagem JavaScript.