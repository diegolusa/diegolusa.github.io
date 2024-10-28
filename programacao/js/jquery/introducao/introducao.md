# Introdução ao uso da última versão da biblioteca jQuery

## Introdução

jQuery é uma biblioteca JavaScript muito popular por ser rápida, pequena e rica em recursos. Basicamente seu uso torna a varredura e manipulação de documentos HTML, manipulação de eventos, animação e Ajax muito mais simples do que utilizar código JavaScript *vanilla*.

!!! info "Nota"
    *Vanilla* é um termo utilizado para indicar o uso de uma tecnologia de forma pura, básica. Nenhuma biblioteca ou framework não nativo é aplicado.

## Instalação

Para incluir a última versão do jQuery em um projeto, podemos utilizar um CDN (Content Delivery Network) ou baixar a biblioteca e incluí-la localmente. Quando utilizamos CDN, adicionamos à tag  `<head>` do documento uma tag `<script>`, informando no atributo *src* o endereço de [CDN da versão desejada](https://releases.jquery.com/jquery/). Caso opte por baixar a biblioteca localmente, o atributo `src` deve receber o caminho local.

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
````

## Uso

Ao adicionar o JQuery ao documento, temos a disposição um vasto conjunto de métodos úteis para manipulação do DOM da página. No exemplo que segue, o código está adicionando um *listener* de click ao botão, de modo que, ao executar o evento, o texto de todos os parágrafos do documento irão receber a informação *Você clicou no botão*

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Exemplo jQuery</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function(){
            $("button").click(function(){
                $("p").text("Você clicou no botão!");
            });
        });
    </script>
</head>
<body>
    <p>Texto original</p>
    <button>Clique aqui</button>
</body>
</html>
```


Perceba que a sintaxe do JQuery sempre considera o uso da função `$()`, conhecida como *função JQuery*. Como parâmetro, informa-se um seletor, cuja sintaxe e funcionamento é idêntico ao CSS.

Um dos benefícios do uso do JQuery é a manipulação do DOM. Vamos ver alguns exemplos:

- Adicionar um novo elemento como filho de outro

```javascript
$("body").append("<p>Novo parágrafo</p>");
$("body").prepend("<p>Novo parágrafo no início</p>");
```

- Remover um elemento

```javascript
$("#meuId").remove();
```

- Alterar valor de atributos

```javascript
$("img").attr("src", "nova-imagem.jpg");
```

- Adicionar *listener* de evento de clique

```javascript
$("button").click(function(){
    alert("Botão clicado!");
});
```


- Adicionar *listener* de evento de "mouse sobre"

```javascript
$("p").mouseover(function(){
    $(this).css("color", "red");
});
```


-  Esconder ou mostrar elementos (`.hide()` e `.show()`)

```javascript
$("#meuElemento").hide();
$("#meuElemento").show();
$("#meuElemento").toggle();
```

- Aplicação de estilos

```javascript
$("p").css("color", "blue");
```

- Definição do conteúdo dos elementos
  
```javascript
$("#meuElemento").html("<strong>Novo conteúdo HTML</strong>");
$("#meuElemento").text("Novo conteúdo de texto");
```

Além de métodos relacionados com a manipulação do DOM da página, a JQuery oferece um conjunto de utilitários que simplificam operações comuns no desenvolvimento frontend.

- `$.each()` para iterar sobre arrays e objetos

```javascript
$.each([1, 2, 3], function(index, value){
    console.log(index + ": " + value);
});
```

- `$.extend()` para mesclar o conteúdo de dois ou mais objetos em apenas um

```javascript
var obj1 = {a: 1, b: 2};
var obj2 = {b: 3, c: 4};
var resultado = $.extend({}, obj1, obj2);
console.log(resultado); 
```

- `$.grep()` para filtrar dados de um array com base em uma função de filtragem

```javascript
var numeros = [1, 2, 3, 4, 5];
var pares = $.grep(numeros, function(valor){
    return valor % 2 === 0;
});
console.log(pares);
```

1. `$.map()` para modificar dados de um array a partir de uma função de transformação
```javascript
var numeros = [1, 2, 3];
var quadrados = $.map(numeros, function(valor){
    return valor * valor;
});
console.log(quadrados);
```

2. `$.inArray()` para verificar se um valor está presente em um array e retornar o índice em que se encontra

```javascript
var frutas = ["maçã", "banana", "laranja"];
var indice = $.inArray("banana", frutas);
console.log(indice); 

```

