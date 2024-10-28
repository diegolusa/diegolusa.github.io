---
title: "Laços de Repetição"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---

Laços de repetição são estruturas de controle que permitem criar iterações, ou seja, repetição de instruções. No Javascript, as estruturas de repetição são o `for`, `while` e `do while`. Abaixo, seguem detalhes e exemplos destes diferentes laços de repetição.


## `for` loop

O comando `for` é usado para iterar sobre uma lista de itens por um número específico de vezes. Na estrutura do comando, temos `inicialização`, que especifica os valores iniciais das variáveis de controle. Em `condição`, colocamos um teste condicional para determinar a condição de parada do laço. Finalmente, `incremento` determina a alteração das variáveis de controle a cada iteração.

```javascript
for (inicialização; condição; incremento) {
  // Bloco de código a ser repetido
}
```



## `while` loop

O comando `while` executa um bloco de código enquanto uma condição especificada for verdadeira.

```javascript
while (condição) {
  // Bloco de código a ser repetido enquanto a condição for verdadeira
}
```

## `do...while` loop

O comando `do...while` é semelhante ao `while`, mas o bloco de código é executado pelo menos uma vez antes da verificação da condição.

```javascript
do {
  // Bloco de código a ser executado pelo menos uma vez
} while (condição);
```

## `break` e `continue`

`break` é usado para interromper a execução de um loop, enquanto `continue` é usado para pular para a próxima iteração do loop.

```javascript
for (var i = 0; i < 10; i++) {
  if (i === 5) {
    break; // Interrompe o loop quando i é igual a 5
  }
  if (i === 3) {
    continue; // Pula para a próxima iteração quando i é igual a 3
  }
  console.log(i);
}
```

Esses são os principais comandos de desvio de fluxo em JavaScript, usados para controlar a execução do código com base em condições específicas e iterar sobre coleções de dados.