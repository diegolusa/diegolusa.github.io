---
title: "HTML5 - Imagens"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---

Adicionar imagens à documentos HTML5 é algo trivial. O que mais se observa são documentos que utilizam texto, imagens, áudio e vídeo de forma combinada para passar a informação desejada ao usuário. Isso porque recursos audiovisuais conferem uma experiência mais rica, tornando o documento atrativo e, eventualmente, mais informativo.

Em termos de código, utilizamos o elemento `<img>` para incorporar imagens ao HTML5. Os atributos obrigatórios são `src` e `alt`. O primeiro deles indica o caminho para o  arquivo, que pode ser absoluto ou relativo. Já o atributo `alt` contém uma descrição textual que será exibida pela navegador em substituição à imagem, caso ela não possa ser apresentada.

Outros dois atributos importantes são `width` (largura) e `heigth` (altura). Utilizamos eles para especificar as dimensões da imagem em pixels. É conveniente utilizar valores nestas propriedades para melhorar a experiência do usuário quando da carga do recurso pelo navegador. Também merece menção o atributo `title`, o qual fornece um texto de título que é exibido quando o usuário passa o mouse sobre a imagem.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Figuras/Imagens</title>
    <meta charset="utf-8">
  </head>
  <body>
    <img src="caminho/para/a/imagem.jpg" alt="Descrição da Imagem" title="Exemplo" width="20px" heigth="10px" >
  </body>
</html>
```

## Tag *figure*


A tag `figure` é uma tag semântica introduzida no HTML5 usada para encapsular elementos como imagens, ilustrações, gráficos, códigos, entre outros, que são referenciados no contexto de um documento. É frequentemente combinada com a tag `figcaption` para fornecer uma legenda ou  escrição associada ao conteúdo encapsulado. Além de servir ao propósito de atribuir semântica aos elementos de conteúdo, a tag `figure` também  contribuiu para os fundamentos de acessibilidade pois melhora a experiência de quem utilize tecnologias assistivas.


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
          <img src="https://pt.wikipedia.org/wiki/Gal%C3%A1xia_de_Andr%C3%B4meda#/media/Ficheiro:Pic_iroberts1.jpg" alt="Galáxia de Andrômeda"  width="300" height="500" >
          <<figcaption>Galáxia de Andrômeda: Wikipédia</figcaption>>
      </figure>

  </body>
</html>
```


## Formatos de gráficos suportados

Os navegadores modernos suportam vários tipos de gráficos. Os mais comuns são JPEG, PNG, GIF e SVG.

- **JPEG (Joint Photographic Experts Group)** é amplamente utilizado para fotografias e imagens com tons contínuos de cor. Ele oferece uma boa compressão com perdas, o que resulta em arquivos menores, mas pode sacrificar um pouco da qualidade da imagem.
-** PNG (Portable Network Graphics)** é frequentemente usado para imagens com áreas de cor sólida, como logotipos e gráficos. Ele suporta transparência, o que o torna ideal para imagens com fundos transparentes.
- **GIF (Graphics Interchange Format)** é conhecido por suportar animações, mas também é usado para imagens estáticas, especialmente aquelas com poucas cores. O formato GIF suporta transparência e é amplamente utilizado para ícones e gráficos simples.
- **SVG (Scalable Vector Graphics)** é um formato baseado em XML que descreve imagens vetoriais. Ele é ideal para gráficos escaláveis, como ícones e logotipos, pois pode ser redimensionado sem perda de qualidade.