---
title: "HTML5 - Imagens"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---

Adicionar imagens à documentos HTML5 é algo trivial. O que mais se observa são documentos que utilizam texto, imagens, áudio e vídeo de forma combinada para passar a informação desejada ao usuário.

Em termos de código, utilizamos o elemento `<img>` para incorporar imagens ao HTML5. Os atributos obrigatórios são `src` e `alt`. O primeiro deles indica o caminho para o  arquivo, que pode ser absoluto ou relativo. Já o atributo `alt` contém uma descrição textual que será exibida pela navegador em substituição à imagem, caso ela não possa ser apresentada.

Outros dois atributos importantes são `width` (largura) e `heigth` (altura). Utilizamos eles para especificar as dimensões da imagem em pixels. É conveniente utilizar valores nestas propriedades para melhorar a experiência do usuário quando da carga do recurso pelo navegador.

Temos também o elemento `<figure>`, que é utilizado para construir um *container* para figuras, ilustrações, diagramas, etc. Torna-se necessário quando precisamos adicionar legendas às imagens, conforme iremos observar no código que segue.



```html
<!DOCTYPE html>
<html>
  <head>
    <title>Figuras/Imagens</title>
    <meta charset="utf-8">
  </head>
  <body>
      <img src="https://cdn.pixabay.com/photo/2014/02/17/10/20/statue-of-liberty-267948_960_720.jpg" alt="Estátua da Liberdade, Ilha da Liberdade, Nova York, EUA" width="300" height="500">

      <p> Na sequência apresentamos a imagem da Galáxia de Andrômeda para que você aprecie:</p>
      <figure>
          <img src="https://pt.wikipedia.org/wiki/Gal%C3%A1xia_de_Andr%C3%B4meda#/media/Ficheiro:Pic_iroberts1.jpg" alt="Galáxia de Andrômeda"  width="300" height="500" />
          <<figcaption>Galáxia de Andrômeda: Wikipédia</figcaption>>
      </figure>

  </body>
</html>
```