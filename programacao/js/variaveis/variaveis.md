---
title: "Variáveis, Constantes e Escopos"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---


Em JavaScript, temos a disposição três formas de declarar variáveis: `var`, `let`, e `const`.

- **`var`**:  As variáveis declaradas com `var` têm escopo de função ou escopo global, o que significa que podem ser acessadas de dentro da função em que foram declaradas ou globalmente dentro do script. Mesmo declaradas no meio ou no final do escopo da função, elas são automaticamente postas no início pelo interpretador.

- **`let`**: As variáveis declaradas com `let` têm escopo de bloco, o que significa que são acessíveis apenas dentro do bloco em que foram declaradas.

- **`const`**: Variáveis declaradas com `const` também têm escopo de bloco e são usadas para declarar valores constantes que não podem ser alterados após a inicialização.



```javascript

var x = 10;
console.log(x);


let y = 20;
console.log(y); 


const z = 30;//não posso mudar o valor de z a partir deste momento
console.log(z); 
```

## Escopos

O escopo em JavaScript define onde as variáveis são acessíveis. Existem dois tipos principais de escopos: escopo global e escopo local.

- **Escopo Global**: As variáveis globais são acessíveis em qualquer lugar do script.

- **Escopo Local**: As variáveis locais são acessíveis apenas dentro da função ou bloco em que foram declaradas.



```javascript
// Escopo global: podemos acessar a partir de qualquer ponto do código
var valor_global = 100;

function myFunction() {
  // Escopo local: restrito a esta função
  var valor_local = 200;
  console.log(valor_global); // Acesso à variável global
  console.log(valor_local); // Acesso à variável local
}

console.log(valor_local)//ERRO: variável não existe neste escopo
```