---
title: "HTML5 - Tags Estruturais"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-09-06 08:00:00
---


Um documento escrito em HTML pode ter seu conteúdo dividido em diferentes segmentos, como cabeçalho, rodapé, seções, artigos, barra de navegação e informações associadas. Antes do HTML5, a divisão destes conteúdos era feita basicamente por meio de divisões genéricas (tag `<div>`), o que conferia a estrutura desejada para o desenvolvedor, mas não atribuia a semântica necessária para interpretação automática da informação.


Para ilustrar a situação, vamos imaginar a página inicial de um *web site* fictício. Inicialmente iremos utilizar apenas divisões para segmentar o conteúdo e, na sequência, faremos uso das tags específicas do HTML5. No primeiro caso aplicamos várias vezes a tag `<div>` para organizar o conteúdo e utilizamos o atributo global `id` para indicar o significado de cada segmento.

Embora a estratégia de utilizar `<div>` atenda ao objetivo do desenvolvedor, qualquer processamento automático de conteúdo do documento fica muito difícil de ser realizado. Vamos imaginar, por exemplo, que quiséssemos obter somente os artigos do conteúdo da página. Talvez você possa pensar: ok, basta consultar o conteúdo das `<div>`s que contém em seu atributo `id` os valores *art1* ou *art2*. Se o documento preservar os identificadores de artigos, então o algoritmo funciona, é claro, somente para esta página específica.

O tempo passa, a página é modificada e novos artigos são adicionados. É preciso vasculhar o HTML, entender quais marcas foram atribuídas pelo desenvolvedor aos novos artigos e então ajustar o algoritmo para coletá-los. Aí começam os problemas...


```html
<!DOCTYPE html>
<html>

<head>
    <title>IFRS News</title>
    <meta charset="utf-8">
</head>

<body>
    <div id="cabecalho">
        <ul>
            <li><a href="home.html">Home</a></li>
            <li><a href="ensino.html">Ensino</a></li>
            <li><a href="pesquisa.html">Pesquisa</a></li>
            <li><a href="extensao.html">Extensão</a></li>
        </ul>

    </div>
    <div id="conteudo">
        <div id="secao_academico">
            <h1>Informações Acadêmicas</h1>
            <div id="art1">
                <h2>Ensino Remoto</h2>
                <p>O ensino remoto ...</p>

            </div>

        </div>
        <div id="secao_processo_seletivo">
            <h1>Processo Seletivo</h1>
            <div id="art2">
                <h2>Ingresso 2022/1</h2>
                <p>O processo seletivo 2022/1 ...</p>
            </div>
        </div>

    </div>
    <div id="rodape">
        <address>
            <small>Rua General Osório, 348 – Bairro Centro – Bento Gonçalves/RS</small>
            <small>CEP: 95700-086</small>
        </address>
    </div>


</body>

</html>
```

Quando utilizamos `tags` genéricas para representar conteúdo, precisamos adicionar alguma informação em seus atributos para que possamos (nós, humanos) diferenciar seu conteúdo das demais. Ocorre que o sentido que atribuímos a partir destas informações adicionais não é explícito, pois dependente da interpretação do contexto. Esta semântica não é precisa, formal. Nada impede que o desenvolvedor atribua ao `id` de uma `<div>` o valor *xyz01*, com vistas a denotar um artigo. Qual software poderia facilmente deduzir o significado contextual desta informação?

Em razão destas dificuldades de representação de tipos de conteúdo por meio de `tags` genéricas, o HTML5 trouxe um conjunto de novas `tags`, várias delas voltadas à semântica de conteúdo. Vejamos algumas:

 - [`<article>`](https://developer.mozilla.org/docs/Web/HTML/Element/article): Representa um trecho de conteúdo independente, autocontido, que pode ser distribuído sem o restante da página.
 - [`<section>`](https://developer.mozilla.org/docs/Web/HTML/Element/section): Indica uma seção genérica de conteúdo.
 - [`<aside>`](https://developer.mozilla.org/docs/Web/HTML/Element/aside): Seção de conteúdo tangencialmente relacionado ao seu entorno, o qual poderia ser removido sem representar uma perda significativa para a compreensão.
 - [`<footer>`](https://developer.mozilla.org/docs/Web/HTML/Element/footer): Utilizado para rodapé de seções, para registro de informações de direitos autorais, autoria e links relacionados.
 - [`<header>`](https://developer.mozilla.org/docs/Web/HTML/Element/header): Conteúdo introdutório, cabeçalho, recursos iniciais de navegação.
 - [`<nav>`](https://developer.mozilla.org/docs/Web/HTML/Element/nav): Segmento do documento reservado para navegação.
 - [`<main>`](https://developer.mozilla.org/docs/Web/HTML/Element/main): Especifica o trecho do documento que contém o conteúdo principal.


Com estas novas tags é possível interpretar o significado dos trechos de conteúdo de forma inequívoca. Vamos refazer nossa página, agora aplicando as `tags` descritas ao invés de `<div>`s, para demonstrar a diferença.

```html
<!DOCTYPE html>
<html>

<head>
    <title>IFRS News</title>
    <meta charset="utf-8">
</head>

<body>
    <header>
        <nav>
            <ul>
                <li><a href="home.html">Home</a></li>
                <li><a href="ensino.html">Ensino</a></li>
                <li><a href="pesquisa.html">Pesquisa</a></li>
                <li><a href="extensao.html">Extensão</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <header>
                <h1>Informações Acadêmicas</h1>
            </header>
            <article>
                <h2>Ensino Remoto</h2>
                <p>O ensino remoto ...</p>

            </article>

        </section>
        <section>
            <header>
                <h1>Processo Seletivo</h1>
            </header>
            <article>
                <h2>Ingresso 2022/1</h2>
                <p>O processo seletivo 2022/1 ...</p>
            </article>
        </section>

    </main>
    <footer>
        <address>
            <small>Rua General Osório, 348 – Bairro Centro – Bento Gonçalves/RS</small>
            <small>CEP: 95700-086</small>
        </address>
    </footer>


</body>

</html>
```

Agora é natural perceber o que significam os segmentos de conteúdo, tanto para nós, humanos, quando para softwares que interpretam o documento, como os navegadores. E tudo isso por conta da tag utilizada, que possui semântica (significado) específico.

\bibliography