---
title: "Interagindo com o Navegador e DOM"
tags:
 - Programação
 - Linguagens de Programação
 - JavaScript
date: 2024-04-28 08:00:00
---





## Objeto `document`

`document` representa o modelo de objeto do documento HTML, que é a própria representação do conteúdo HTML em objetos JavaScript.

Ao interagir com este objeto, podemos modificar a estrutura e apresentação do documento em resposta a eventos e interações do usuário com a página.

### Propriedades

Vejamos algumas das propriedades que o objeto `document` fornece:

- `document.URL`: retorna a URL do documento.
- `document.title`: permite obter ou definir o título do documento.
- `document.body`: retorna a referência ao elemento `<body>` do documento.
- `document.head`: retorna a referência ao elemento `<head>` do documento.
- `document.documentElement`: retorna o elemento `<html>` do documento.
- `document.domain`: Retorna o domínio do servidor que serve o documento.
- `document.referrer`: retorna a URL do documento que levou o usuário a este documento.
- `document.forms`: retorna uma coleção de todos os elementos `<form>` no documento.
- `document.images`: retorna uma coleção de todos os elementos `<img>` no documento.
- `document.links`: retorna uma coleção de todos os elementos `<a>` que têm um atributo `href` no documento.
- `document.scripts`: retorna uma coleção de todos os elementos `<script>` no documento.

Outras propriedades estão a disposição além destes. Você pode encontrar o detalhamento de cada um no site [Developers Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Document).

### Métodos

- `document.getElementById(id)`

      Retorna uma referência ao elemento que possui o atributo `id` com o valor especificado.

      ```javascript
      var elemento = document.getElementById("logotipo");
      ```

- `document.getElementsByClassName(className)`: 

      Retorna uma coleção de elementos que têm, no atributo `class`, o nome da classe informada como parâmetro. Observe o exemplo.

      ```javascript
      var elementos = document.getElementsByClassName("cm-line")

      for (const e of elementos){
         console.log(e)
      }

      ```

- `document.getElementsByName(name)`: 

      Retorna uma coleção de elementos cujo atributo `name` contém o valor informado como parâmetro.

      ```javascript
      var elementos = document.getElementsByName("viewport")
      ```

- `document.getElementsByTagName(tagName)`: 

      Retorna uma coleção de todos os elementos da tag indicada por parâmetro.

      ```javascript
      var elementos = document.getElementsByTagName("div")
      ```

- `document.querySelector(selector)`

      É uma função que permite selecionar um elemento HTML em uma página usando um seletor CSS válido. O primeiro elemento encontrado, que condiz com o seletor, será retornado pelo método.  

      O método `querySelector()` aceita um parâmetro, que é uma string que representa o seletor CSS. Este seletor pode ser um ID, uma classe, um tipo de elemento, um seletor de atributo ou uma combinação deles. 

      No exemplo abaixo, estamos buscando a primeira ocorrência de elemento da classe `importante` no documento.


      ```javascript
      var elemento = document.querySelector(".importante");
      ```

      Se houver interesse em retornar todos os elementos que atendem ao seletor, devemos utilizar o método `document.querySelectorAll()`, iterando sobre o retorno.

 
- `document.createElement(tagName)`: 

      Cria um novo elemento HTML especificado pelo nome da tag informado como parâmetro.

      ```javascript
         let parag = document.createElement("p")
         parag.textContent = texto
         document.body.appendChild(parag)

      ```   

- `document.write(text)`: 
      Escreve conteúdo HTML diretamente no documento.

      ```javascript
         document.write("<h2>Teste</h2>")
      ```


- `document.addEventListener(event, function)`: 
  
      Adiciona um ouvinte (*listener*) de evento a um elemento do documento. Isso permite executar ações em resposta a eventos disparados.

      ```javascript
         let botao = document.getElementById("btn_calcular")
         botao.addEventListener("click",() => {document.alert("Ouvi seu evento de click")})
      ```

- `document.removeEventListener(event, function)`: 

   Remove um ouvinte (*listener*) de evento de um elemento do documento previamente configurado.

## Tipos de eventos


Eventos são o resultado de ações de ações do usuário sobre os elementos da página ou mesmo estados do próprio sistema e navegador, por exemplo.

Os eventos oriundos de tais condições são emitidos e podem ser processados por funções específicas, escritas pelo desenvolvedor.

Os eventos mais comuns associados ao objeto `document` incluem:

- `DOMContentLoaded`: É acionado quando o HTML do documento foi completamente carregado e analisado, sem aguardar por folhas de estilo, imagens e subframes para concluir o carregamento.
- `load`: É acionado quando todo o conteúdo do documento, incluindo imagens e folhas de estilo, foi completamente carregado.
- `click`: É acionado quando um elemento é clicado pelo usuário.
- `keydown`, `keyup`, `keypress`: São acionados quando uma tecla é pressionada e liberada.







=====================


# Objeto Window

O objeto `window` é um dos principais objetos do navegador da web e representa a janela do navegador que contém o documento HTML.

## Propriedades:

- `window.document`: Retorna o documento HTML carregado na janela.

- `window.location`: Retorna um objeto contendo informações sobre a URL da página.

- `window.navigator`: Retorna um objeto contendo informações sobre o navegador.

- `window.innerWidth` e `window.innerHeight`: Retornam a largura e a altura internas (em pixels) da janela do navegador, incluindo barras de rolagem, mas excluindo a moldura do navegador.

- `window.outerWidth` e `window.outerHeight`: Retornam a largura e a altura externas (em pixels) da janela do navegador, incluindo barras de rolagem e a moldura do navegador.

- `window.screen`: Retorna um objeto contendo informações sobre a tela do dispositivo.

- `window.history`: Retorna o objeto de histórico do navegador, permitindo navegação entre as páginas visitadas.

- `window.localStorage` e `window.sessionStorage`: Oferecem acesso aos mecanismos de armazenamento local e de sessão do navegador, respectivamente, permitindo armazenar dados localmente no navegador do usuário.

- `window.frames`: Retorna uma coleção de objetos representando todas as frames contidas na janela.

- `window.parent`: Retorna a janela pai da janela atual, útil quando uma janela abre outra.

## Métodos:

- `window.alert(message)`: Exibe um diálogo de alerta com o texto especificado.

- `window.confirm(message)`: Exibe um diálogo de confirmação com o texto especificado, retornando `true` se o usuário clicar em "OK" e `false` se clicar em "Cancelar".

- `window.prompt(message, default)`: Exibe um diálogo solicitando que o usuário insira um texto, com uma mensagem opcional e um valor padrão opcional.

- `window.open(url, name, features)`:  Abre uma nova janela do navegador com o URL especificado.

- `window.close()`: Fecha a janela do navegador atual.

- `window.setTimeout(function, milliseconds)`: Executa uma função depois de um certo número de milissegundos.

- `window.setInterval(function, milliseconds)`: Executa uma função repetidamente, com um intervalo de tempo especificado entre cada execução.

- `window.clearTimeout(timeoutID)` e `window.clearInterval(intervalID)`: Cancelam a execução de uma função agendada com `setTimeout()` ou `setInterval()`.

## Eventos:

Alguns dos eventos mais comuns associados ao objeto `window` incluem:

- `load`: É acionado quando o documento e todos os recursos associados foram completamente carregados.
- `resize`: É acionado quando a janela do navegador é redimensionada.
- `scroll`: É acionado quando o usuário rola a página.
- `beforeunload` e `unload`: São acionados quando o documento está prestes a ser descarregado ou completamente descarregado, respectivamente.


