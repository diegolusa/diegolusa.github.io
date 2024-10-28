---
title: "CSS3 - Unidades de Medida"
tags:
 - Programação
 - Linguagens de Programação
 - Web
 - Unidades de Medida
date: 2021-10-14 08:00:00
---

As medidas são utilizadas para especificar o tamanho e posicionamento de elementos. Temos a disposição dois tipos, que são as medidas absolutas e relativas. Na sequência iremos analisar cada uma delas:

## Medidas Absolutas:

As medidas absolutas, como **pixels (px)**, **polegadas (in)**, **centímetros (cm)**, etc., são especificadas com um valor fixo que não é afetado pelo ambiente ou contexto da página. Elas fornecem uma precisão absoluta e são consistentes independentemente do dispositivo ou configuração de exibição.

Isso significa que medidas absolutas resultam em elementos com tamanhos fixos e invariáveis, independentemente do tamanho da tela ou do navegador em que estão sendo exibidos. De modo geral, tal característica impõe problemas de adaptação em dispositivos com tamanhos de tela variados, especialmente em dispositivos móveis ou em layouts responsivos.

No CSS3 temos a disposição [diversas medidas absolutas](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units), contudo a que utilizamos com maior frequência é o `pixel (px)`. No exemplo que segue, estamos definido duas propriedades com valores em pixels.

```css
font-size: 16px;
width: 300px;
```

## Medidas Relativas:

Diferentemente das absolutas, as medidas relativas, como **porcentagem (%)**, **em (em)**, **rem (rem)**, **vw (viewport width)**, **vh (viewport height)**, etc., são dimensionadas com base em algum aspecto do ambiente de layout, como o tamanho da fonte, largura da tela ou tamanho do elemento pai.
  
São muito utilizadas, pois elas se ajustam dinamicamente conforme o contexto, proporcionando uma melhor adaptação a diferentes dispositivos e ambientes de visualização. São fundamentais para criar layouts responsivos, onde os elementos se ajustam de acordo com o tamanho da tela, garantindo uma experiência consistente em dispositivos variados.

Deste modo, ao usar medidas relativas, é possível manter proporções consistentes entre elementos em diferentes partes do layout, pois eles são dimensionados proporcionalmente em relação ao ambiente de exibição. 

As unidades que seguem são apenas algumas unidades de medida relativas do CSS3. Você deve considerar que existem [outras mais a disposição](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units).


### Porcentagem (%)
Unidade relativa as proporções do elemento pai.

```css
width: 50%;
```

### Em (em)
EM é uma unidade relativa ao tamanho da fonte do elemento pai.

```css
font-size: 1.2em;
```

### Rem (rem)

REM define o tamanho relativo à fonte do elemento raiz (normalmente o elemento `<html>`).

```css
margin-left: 2rem;
```

### Viewport Width (vw) e Viewport Height (vh)

Referem-se à largura e altura da janela de visualização do navegador, respectivamente.


```css
width: 50vw;
height: 80vh;
```

### Viewport Minimum (vmin) e Viewport Maximum (vmax)

Referem-se à menor ou maior dimensão da janela de visualização do navegador (largura ou altura), respectivamente.
```css
  width: 50vmin;
  height: 80vmax;
```

