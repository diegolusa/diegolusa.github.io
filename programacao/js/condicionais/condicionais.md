---
title: "Desvio de Fluxo"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---




Assim como outras linguagens, em JavaScript, os comandos de desvio de fluxo permitem controlar a execução do código, permitindo que você tome decisões com base em condições específicas ou itere sobre coleções de dados. 

## Comando `if`

O comando `if...else` permite executar um bloco de código se uma condição especificada for verdadeira e outro bloco de código se a condição for falsa.

Observe a sintaxe do comando. Devemos colocar a condição entre `()` e os blocos devem ser especificados com `{}`.

```javascript
if (condição) {
  // Bloco de código a ser executado se a condição for verdadeira
} else {
  // Bloco de código a ser executado se a condição for falsa
}
```
Importante a comentar é que o bloco `else` é opcional na estrutura. E, havendo necessidade de testar mais de duas opções, podemos adicionar a estrutura `if ... else .. if `. Veja um exemplo incorporado em uma página HTML:

```javascript
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página com JavaScript</title>
</head>
<body>

<select id="opcoes">
  <option value="A">A</option>
  <option value="B">B</option>
  <option value="C">C</option>
</select>

<p></p>

<script>

    var lista = document.getElementById("opcoes");
    var p = document.querySelector("p")
    lista.addEventListener("change", onListaChange);

    function onListaChange(){
        let valor = lista.value
        if (valor==='A'){
            p.innerText = 'Voce escolheu A'
        }else if (valor==='B'){
            p.innerText = 'Voce escolheu B'
        } else {
            p.innerText = 'Voce escolheu C'
        }
    }
</script>

</body>
</html>
```

## Comando `switch...case`

O comando `switch...case` permite avaliar uma expressão e executar um bloco de código com base em valores correspondentes.

```javascript

let valor=parseInt(prompt("Informe um valor inteiro"))

switch (valor) {
  case 1:
    // Bloco de código a ser executado se a variável valor for igual a 1
    break;
  case 2:
    // Bloco de código a ser executado se a variável valor for igual a 2
    break;
  default:
    // Não sendo nenhum dos anteriores, executa este caso padrão
}
```

## Operador ternário

O operador ternário é uma forma simplificada de realizar um teste condicional que retorna um valor quando verdadeiro e outro, quando falso.

No exemplo a seguir, a variável `resultado` vai receber `Aprovado` ou `Tente novamente`, a depender do teste condicional `nota > 6`.

```javascript
const resultado = nota> 6 ? "Aprovado" : "Tente novamente";

```