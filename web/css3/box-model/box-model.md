---
title: "CSS3 - Box Model"
tags:
 - Programação
 - Linguagens de Programação
 - Web
 - Box Model
date: 2024-10-13 08:00:00
---


O Box Model é um conceito do CSS que descreve como os elementos HTML são renderizados e ocupam espaço em uma página da web. Ele consiste em quatro partes principais: **conteúdo**, **preenchimento (padding)**, **borda** e **margem**. Cada uma dessas partes influencia as dimensões e o layout de um elemento na página [@mdncss3pseudoelements].

<figure markdown="span">
    ![Componentes do Box Model](https://web.dev/static/learn/css/box-model/image/a-diagram-showing-four-m-af72960a9e79a.svg)
    <figcaption>Quatro caixas do box model [@mdncss3pseudoelements].</figcaption>
</figure>


## Conteúdo (*Content*)

O conteúdo de um elemento HTML é a área onde o texto, imagens ou outros tipos de conteúdo são exibidos. Ele é dimensionado de acordo com as propriedades de largura (`width`) e altura (`height`). O tamanho do conteúdo é determinado pelo conteúdo real do elemento e quaisquer dimensões especificadas pelo desenvolvedor [@mdncss3pseudoelements].

## Preenchimento (*Padding*)

O preenchimento é a área entre o conteúdo do elemento e sua borda. Ele fornece espaço adicional dentro do elemento, aumentando a distância entre o conteúdo e a borda. O preenchimento é útil para criar espaçamento interno e melhorar a legibilidade do conteúdo. Ele pode ser especificado usando as propriedades `padding-top`, `padding-right`, `padding-bottom` e `padding-left`, ou a propriedade abreviada `padding` [@mdncss3pseudoelements].

## Borda (*Border*)

A borda é uma linha que circunda o conteúdo e o preenchimento de um elemento. Ela define os limites visuais de um elemento e pode ter diferentes estilos, espessuras e cores. A borda é definida pelas propriedades `border-width`, `border-style` e `border-color`. Os estilos de borda comuns incluem sólido, pontilhado e tracejado [@mdncss3pseudoelements].

## Margem (*Margin*)

A margem é a área externa à borda de um elemento, que define o espaço entre esse elemento e outros elementos vizinhos. Ela fornece controle sobre o espaçamento entre elementos na página. A margem pode ser especificada usando as propriedades `margin-top`, `margin-right`, `margin-bottom` e `margin-left`, ou a propriedade abreviada `margin` [@mdncss3pseudoelements].
 







<!-- 
https://piccalil.li/blog/a-more-modern-css-reset/


-->