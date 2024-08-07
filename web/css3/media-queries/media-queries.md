---
title: "Media Queries"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2024-07-30 08:00:00
---

Media queries são regras que permitem condicionar a aplicação de estilos, ou mesmo, sobrescrever quando determinadas condições forem satisfeitas. São amplamente utilizadas no CSS3 para criar designs responsivos, adaptando a apresentação de um site às diferentes características dos dispositivos, como tamanho da tela, resolução e orientação. 

Além do CSS3, media queries podem ser utilizadas em elementos HTML, como `<style>`, `<link>`, `<source>` e via JavaScript, via método [matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia) do objeto *window* [@mdnmediaqueries].


## Estrutura Básica

Uma media query consiste em um tipo de mídia e, opcionalmente, uma ou mais expressões que verificam as condições da mídia. Na especificação das condições, podemos utilizar operadores lógicos, como *not*, *only* e *and*. A estrutura básica é:

```css
@media not|only mediatype and (expressão) {
    /* CSS aqui */
}
```

Na expressão acima, temos:

- **Tipo de mídia (mediatype)**: Especifica o tipo de dispositivo para o qual o estilo se aplica, como `screen` (telas), `print` (impressoras), `all` (todos os dispositivos), entre outros.

- **Expressões**: Verificam as características da mídia, como largura da tela (`width`), altura da tela (`height`), resolução (`resolution`), orientação (`orientation`). Observe algumas possibilidades:
  - `width` e `height`: Largura e altura da área de visualização.
  - `device-width` e `device-height`: Largura e altura da tela do dispositivo.
  - `orientation`: Orientação da tela (`portrait` ou `landscape`).
  - `resolution`: Resolução da tela (pode ser especificada em dpi ou dpcm).
  - `aspect-ratio`: Proporção entre a largura e a altura da área de visualização.
  - `device-aspect-ratio`: Proporção entre a largura e a altura da tela do dispositivo.
  - `color`: Número de bits de cor disponíveis.
  - `color-index`: Número de cores na paleta.
  - `monochrome`: Número de bits por pixel em dispositivos monocromáticos.


A lista de mídias e propriedades é vasta. Acesse a especificação [Media Queries Level 4](https://www.w3.org/TR/2021/CRD-mediaqueries-4-20211225/#intro) para encontrar todo detalhamento do recurso.


As propriedades tipicamente avaliadas são largura máxima e mínima da tela, expressas por `max-width` e `min-width`, respectivamente. No exemplo que segue, a media query aplica estilos específicos para dispositivos com largura de tela de até 600px. Veja:

```css
@media screen and (max-width: 600px) {
    body {
        background-color: lightblue;
    }
}
```

Um exemplo mais complexo envolve a combinação de múltiplas condições através dos operadores lógicos (`and`, `or `, `not` e `only`). Trata-se da verificação que a tela está entre 600px e 1200px de largura.

```css
@media screen and (min-width: 600px) and (max-width: 1200px) {
    body {
        background-color: lightgreen;
    }
}
```

Operadores matemáticos de comparação, como `<`, `<=`, `>`, `>=` podem ser utilizados para potencializar as queries. Observe o exemplo:

```css

@media (width > 500px) {
    body {
        background-color: lightcoral;
    }
}


@media (width <= 800px) {
    body {
        background-color: lightseagreen;
    }
}

```

## Media queries, breakpoints e responsividade

Aplicar media queries é a estratégia utilizada para o desenvolvimento de sites responsivos. Nesta abordagem, definem-se breakpoints (condições em que há mudança no layout) com base na largura da tela. Aqui, embora sendo possível definir breakpoints para dispositivos específicos, o ideal é trabalhar de forma genérica, através de quebras que atendam ao máximo de dispositivos possível [@hostingermediaqueries].

No exemplo que segue temos um documento HTML5 com barra de navegação responsiva. Observe as diferentes *media queries* aplicadas para mudar a quantidade de colunas do layout exibidos (cards) a cada alteração de breakpoint.



```html title="index.html"
    --8<-- "css3/media-queries/index.html"
```


```css title="style.css"
    --8<-- "css3/media-queries/style.css"

```


```javascript title="scripts.js"
    --8<-- "css3/media-queries/scripts.js"

```