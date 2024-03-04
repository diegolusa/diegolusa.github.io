---
title: "HTML5 - Tags"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-09-06 08:00:00
---

A linguagem HTML5 é composta por um conjunto de `tags` (ou elementos). Cada `tag` serve a um propósito, atribuindo um significado - semântica - ao conteúdo envolvido. Quando aplicadas a um documento, a `tag` é aberta e fechada, ficando o conteúdo em meio. Observe a sintaxe de escrita:

- **Abertura da tag**: colocamos o nome da tag entre os símbolos de \(<\) e  \(>\).
```html
<p>
```
- **Fecho da tag**: colocamos o símbolo \(/\) antes do nome da tag. 
```html
</p>
```

A tag `p`, por exemplo, é utilizada para demarcar parágrafos em um documento HTML5. Logo, qualquer conteúdo entre a abertura e o fechamento da tag compreende o conteúdo de um parágrafo. Observe:
```html
<p>Aqui está um novo parágrafo!</p>
```

As tags podem conter `atributos`, que são propriedades que customizam/modificam comportamentos ou associam valores específicos aos elementos. Assim como os nomes de tags, os atributos são pré-definidos, ou seja, não podemos *inventar* novos. Há atributos que são `globais`[@w3cglobalatributes], ou seja, que estão disponíveis a todas as tags e outros são específicos a algumas tags.

Os atributos são informados na abertura da tag, por meio do seu nome, símbolo \(=\) e o respectivo valor entre aspas duplas. Acompanhe o exemplo:

```html
<p id="par01" class="vermelho" style="font-size:1.3rem">Aqui está um novo parágrafo!</p>
```

## Documento e Metadados


+ [`<html>`](https://developer.mozilla.org/docs/Web/HTML/Element/html): Chamada de *root tag*, corresponde ao elemento que envolve todo documento. Todas as demais tags devem ser descendentes diretas ou indiretas de `<html>`. Espera-se que sigam apenas o elemento `<head>` e o elemento `<body>`. O elemento mais importante da tag é `lang`, que especifica o idioma do conteúdo [@whatwg-html5-21].
+ [`<head>`](https://developer.mozilla.org/docs/Web/HTML/Element/head): Utilizada para indicar informações gerais do documento, como metadados e vinculações com scripts e folhas de estilo [@whatwg-html5-21]. Como descendentes diretas de `<head>` temos:
    - [`<meta>`](https://developer.mozilla.org/docs/Web/HTML/Element/meta): Permite definir metadados que não podem ser especificados em outras tags. 
    - [`<title>`](https://developer.mozilla.org/docs/Web/HTML/Element/title): Metadado que define o título do documento ou seu nome. No máximo uma ocorrência é permitida.
    - [`<link>`](https://developer.mozilla.org/docs/Web/HTML/Element/link): Permite especificar as relações entre o documento e outro recurso externo. Utilizado especialmente para vincular folhas de estilo. O endereço do recurso vinculado fica no atributo `href`. Já o atributo `rel` indica o tipo de relacionamento estabelecido, que deve considerar um [conjunto de opções](https://html.spec.whatwg.org/multipage/links.html#linkTypes) definidas pela linguagem.
    - [`<style>`](https://developer.mozilla.org/docs/Web/HTML/Element/style): Permite incluir regras de estilo ao documento.
    - [`<script>`](https://developer.mozilla.org/docs/Web/HTML/Element/script): Permite definir ou referenciar um script executável (JavaScript). A tag pode aparecer no corpo do documento e há diferenças entre uma opção e outra.
+ [`<body>`](https://developer.mozilla.org/docs/Web/HTML/Element/body): Todo documento contém apenas uma tag `<body>` e nela colocamos o conteúdo que será exibido pelo navegador.


Agora vamos colocar todos estes elementos juntos, de sorte a criar um documento básico e válido. Observe que devemos acrescentar na primeira linha `<!DOCTYPE html>` para indicar que o documento está na versão HTML5. Também é preciso que fique claro que algumas tags não são obrigatórias, como `<meta>`, `<title>`, `<script>` e `<style>`.

```html

<!DOCTYPE html>
<html>
  <head>
    <title>Minha primeira página</title>
    <meta charset="utf-8">
    <script>
      alert("Olá, mundo");
    </script>
    <style>
      p {
        color:red;
      }
    </style>
  </head>
  <body>
    <!--O conteúdo do documento-->
  </body>
</html>

```

Percebeu que as tags são abertas e fechadas respeitando a hierarquia? Bem, isso é essencial para construirmos um documento bem formado, que será corretamente interpretado pelo navegador. A ideia é simples: *a tag deve ser fechada sempre no mesmo nível em que foi aberta*.


Outro ponto que você deve ter notado em nosso documento foi o trecho `<!--O conteúdo do documento-->`. Trata-se de um comentário, ou seja, um trecho sem qualquer significado para o navegador e que é ignorado por ele. Utilizamos comentários para anotar informações importantes no código a fim de melhor compreendê-lo. É uma estratégia de documentação. Em termos de sintaxe, todo comentário deve iniciar com `<!--` e encerrar com `-->` para ser válido.


!!! info "Dica"
    Estamos considerando esta forma estrita de sintaxe para facilitar o aprendizado. O padrão HTML especifica regras mais brandas para a questão de abertura e fechamento de tags.

## Semântica de Texto

Vamos agora abordar as principais tags utilizadas para atribuir semântica a texto. Para parágrafos já sabemos que a tag a ser utilizada é `p`, mas é preciso adicionar uma informação importante, que aplica-se a todas as demais tags: o formato que o navegador utiliza para desenhar o conteúdo na tela considera a definição padrão de estilo do elemento. 


+ [`<p>`](https://developer.mozilla.org/docs/Web/HTML/Element/p): Utilizado para criar um parágrafo.
+ [`<small>`](https://developer.mozilla.org/docs/Web/HTML/Element/small): Representa comentários colaterais, textos de menor relevância [@whatwg-html5-21].
+ [`<s>`](https://developer.mozilla.org/docs/Web/HTML/Element/s): Representa conteúdo desatualizado ou que não é mais relevante [@whatwg-html5-21].
+ [`<strong>`](https://developer.mozilla.org/docs/Web/HTML/Element/strong): Representa um conteúdo de maior seriedade, importância ou urgente.  Quanto mais ancestrais `strong` houver, maior será a relevância do conteúdo [@whatwg-html5-21].
+ [`<br>`](https://developer.mozilla.org/docs/Web/HTML/Element/br): Utilizado para representar uma quebra de linha.
+ [`<pre>`](https://developer.mozilla.org/docs/Web/HTML/Element/pre): Representa um texto pré-formatado, apresentado pelo navegador respeitando a forma em que ele foi inserido no documento.
+ [`<i>`](https://developer.mozilla.org/docs/Web/HTML/Element/i): Corresponde a uma sequencia de texto que distingue-se do restante por estar em outro idioma, ser neologismo, termo técnico ou algo semelhante.
+ [`<sup>`](https://developer.mozilla.org/docs/Web/HTML/Element/sup): Usado para adicionar conteúdo <sup>sobrescrito</sup>
+ [`<sub>`](https://developer.mozilla.org/docs/Web/HTML/Element/sub): Usado para adicionar conteúdo <sub>subscrito</sub>
+ [`<mark>`](https://developer.mozilla.org/docs/Web/HTML/Element/mark): Usado para evidenciar um trecho de conteúdo, com vistas a notificar o leitor de sua relevância.
+ [`<em>`](https://developer.mozilla.org/docs/Web/HTML/Element/em): Utilizado para enfatizar fortemente um determinado trecho de conteúdo. Quanto mais ancestrais `em` houver, maior será a ênfase ao trecho [@whatwg-html5-21].
+ [`<code>`](https://developer.mozilla.org/docs/Web/HTML/Element/code): Aplicado para conteúdo que representa trechos de código de programas de computador.
+ [`<span>`](https://developer.mozilla.org/docs/Web/HTML/Element/span): Utilizado para demarcar um trecho de conteúdo para alguma finalidade específica. A tag, em si, não adiciona qualquer semântica ao conteúdo.
+ [`<q>`](https://developer.mozilla.org/docs/Web/HTML/Element/q): Demarca citações curtas, apresentadas em meio a outro conteúdo.
+ [`<quote>`](https://developer.mozilla.org/docs/Web/HTML/Element/quote): Utilizado para especificar o título de um trabalho (livro, programa de computador, artigo, etc.). Não devemos utilizar para envolver nomes de autores, somente o título da obra.
+ [`<blockquote>`](https://developer.mozilla.org/docs/Web/HTML/Element/blockquote): Demarca citações longas.
+ [`<cite>`](https://developer.mozilla.org/docs/Web/HTML/Element/cite): Utilizado para especificar o título de um trabalho (livro, programa de computador, artigo, etc.). Não devemos utilizar para envolver nomes de autores, somente o título da obra[@whatwg-html5-21].
+ [`<span>`](https://developer.mozilla.org/docs/Web/HTML/Element/span): O elemento não provê nenhuma semântica. É utilizado normalmente em conjunto com atributos globais para agrupar trechos de conteúdo textual a fim de facilitar a plicação de estilos, por exemplo.



### Títulos

No HTML5 temos a possibilidade de utilizar seis níveis de títulos. Para isso, temos disponíveis as tags `<h1>`,`<h2>`,`<h3>`,`<h4>`,`<h5>` e `<h6>`. Títulos `<h1>` são os de maior importância, e na medida que o número aumenta, a relevância do título diminui[@mdnheadings]. Veja um exemplo de documento contendo quatro níveis de títulos.

```html

<!DOCTYPE html>
<html>
  <head>
    <title>Títulos</title>
    <meta charset="utf-8">    
  </head>
  <body>
    <h1> Título de primeiro nível</h1>
    <p>Este é um parágrafo</p>
    <h2> Título de segundo nível</h2>
    <p>Este é um parágrafo</p>
    <h3> Título de terceiro nível</h3>
    <p>Este é um parágrafo</p>
    <h4> Título de quarto nível</h4>
    <p>Este é um parágrafo</p>
  </body>
</html>
```


## Listas

As listas são utilizadas para elencar itens de forma ordenada ou não. Para cada caso, temos a disposição uma tag diferente: se o objetivo é utilizar uma lista **ordenada**, então utilizaremos `<ol>` e, caso haja interesse em uma lista **não ordenada**, então devemos usar `<ul>`. Quando os elementos da lista, para ambos os casos, utilizamos a tag `<li>`.

Vamos imaginar que seja necessário criar a lista da feira utilizando HTML5. Como não há ordem associada, iremos utilizar uma lista não-ordenada na construção do documento. Vejamos o resultado:

```html

<!DOCTYPE html>
<html>
  <head>
    <title>Lista da Feira</title>
    <meta charset="utf-8">    
  </head>
  <body>
    <h1>Compras:</h1>
    <ul>
        <li>Alface</li>
        <li>Couve</li>
        <li>Brócolis</li>
        <li>Cenoura</li>
        <li>Pimentão</li>
    </ul>
  </body>
</html>
```


Por outro lado, se quiséssemos listar em um documento a classificação de estudantes em uma avaliação qualquer, utilizaríamos uma lista ordenada, porque, obviamente, temos ordem associada.


```html

<!DOCTYPE html>
<html>
  <head>
    <title>Classificação na Prova de Culinária</title>
    <meta charset="utf-8">    
  </head>
  <body>
    <h1>Participantes:</h1>
    <ul>
        <li>João</li>
        <li>Amanda</li>
        <li>Angela</li>
        <li>Pedro</li>
        <li>Miguel</li>
    </ul>
  </body>
</html>
```









\bibliography