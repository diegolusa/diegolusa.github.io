---
title: "HTML5 - Hiperlinks"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-09-01 08:00:00
---

A capacidade da linguagem HTML de expressar relacionamentos entre documentos certamente é um dos fatores-chave para o sucesso da *web*. 

Os `hiperlinks`, como chamamos estas ligações, constituem vias que ligam um documento a outro, contido no mesmo site ou em sites diferentes, através de palavras, imagens, vídeos e outras coisas. Esse emaranhado de vias levou ao termo *web*, ou seja, uma grande teia de informação, cujo caminho a ser seguido depende unicamente das escolhas do usuário.

Em nossos documentos HTML5 podemos criar hiperlinks através da tag [`<a>`](https://developer.mozilla.org/docs/Web/HTML/Element/a). Para fins didáticos, iremos apresentar como criamos âncoras posicionais para elementos do documento, links locais e links externos.

Para que a tag `<a>` seja considerada um hiperlink, o atributo `href` deve estar presente com o endereço do recurso. Quando o usuário clicar sobre o objeto que representa o hiperlink (texto, imagem, etc), o navegador irá transportar o usuário até o recurso informado.

Outro atributo importante do elemento `<a>` é `target`. Sua função é especificar ao navegador onde o recurso deverá ser apresentado (contexto do navegador). As opções que temos são:

+ **_blank**: Abre o recurso em nova janela ou aba.
+ **_self**:  Abre o recurso no mesmo contexto de navegação do documento origem do hiperlink.
+ **_parent**:  Abre o recurso no contexto de navegação pai.
+ **_top**:  Abre o recurso no contexto de navegação mais elevado da página.

Não apenas recursos obtidos via protocolo HTTP podem ser informados no atributo `href`. Podemos utilizá-lo para várias finalidades, informando valores dos seguintes tipos [@w3chref21]:

+ **URL** ([Uniform Resource Locator](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)) absoluto, como `href="http://localhost:8000/web/html5/hiperlinks/"`. Quando informado de forma absoluta, frequentemente estamos apontando para um recurso externo ao nosso site.
+ **URL relativa**, como `href="hiperlinks/"`. Esse formato é utilizado para navegar entre recursos locais do site.
+ **Link** para algum elemento da página através de seu valor de atributo `id`, como `href="#rodape"`. Neste caso, utilizamos para marcar posições no documento, a fim de facilitar a navegação pelo conteúdo. Imagine o botão *Voltar ao topo*, comum em diversos sites.
+ **Código JavaScript**, como `href="javascript:alert("oi");"`. Este recurso nos permite executar código (algum comportamento) a partir de um link. Muito utilizado na programação Web.



```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hiperlinks</title>
    <meta charset="utf-8">
  </head>
  <body>
      <p>Para explorar o mundo da aventura, confira o <a href="https://www.adventureworld.com/">Adventure World</a>. Se você é apaixonado por culinária, não perca o <a href="https://www.cookingdelights.com/">Cooking Delights</a>, onde você pode encontrar receitas deliciosas e dicas de cozinha. Além disso, se estiver interessado em arte e cultura, visite a <a href="https://www.artgalleryhub.com/">Art Gallery Hub</a> para descobrir obras incríveis de artistas de todo o mundo.</p>


  </body>
</html>
```

Você deve ter percebido no exemplo que o hiperlink é construído a partir do conteúdo do elemento `<a>`. Nós utilizamos texto, mas poderíamos ter utilizado imagens, vídeos ou aúdios, por exemplo.

\bibliography
