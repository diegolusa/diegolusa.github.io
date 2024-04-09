---
title: "CSS3 - Posicionamento"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---



A propriedade `position` é fundamental para controlar o posicionamento dos elementos em uma página da web. Os quatro valores possíveis são `static`, `relative`, `absolute` e `fixed`.

- `static`: Este é o valor padrão. Elementos com `position: static` são renderizados na ordem normal do fluxo do documento. Eles não são afetados pelas propriedades de posicionamento (`top`, `right`, `bottom`, `left`).
- `relative`: Com `position: relative`, você pode mover o elemento em relação à sua posição normal no fluxo do documento, usando as propriedades `top`, `right`, `bottom` e `left`. Ele permanece no fluxo normal do documento, apenas a posição é ajustada.
- `absolute`: Elementos com `position: absolute` são removidos do fluxo normal do documento e posicionados em relação ao seu ancestral mais próximo que tenha uma posição definida (ou seja, que tenha `position: relative`, `position: absolute`, ou `position: fixed`). Isso permite um posicionamento preciso.
- `fixed`: Com `position: fixed`, o elemento é posicionado em relação à janela de visualização do navegador, permanecendo fixo mesmo quando a página é rolada. É útil para cabeçalhos de páginas, barras de navegação e outros elementos que devem permanecer visíveis enquanto o usuário rola a página.

Exemplo de `position: relative`:
```css
#cabecalho {
  position: relative;
  top: 20px;
  left: 30px;
}
```

## Float Property

A propriedade `float` é usada para alinhar elementos ao lado esquerdo ou direito de seu contêiner. Isso é frequentemente utilizado para criar layouts de várias colunas. No entanto, é importante notar que o uso excessivo de `float` pode causar problemas de layout e é geralmente evitado em favor de técnicas mais modernas, como Flexbox e Grid Layout.

Exemplo:
```css
.coluna {
  float: left;
  width: 50%;
}
```

## Flexbox

O Flexbox é um modelo de layout bidimensional que oferece mais controle e flexibilidade na disposição dos elementos em relação aos métodos tradicionais de layout. Ele permite o alinhamento e distribuição de elementos em qualquer direção, tornando-o ideal para criar layouts responsivos e complexos.



Para fazer uso do flexbox precisamos definir um container em torno dos elementos que deverão ser posicionais de maneira responsiva. Para isso, é preciso utilizar a property `display:flex`. Normalmente você definirá uma classe para isso, como a exibida a seguir:

```css
.container {
  display: flex;
}
```

Também é possível definir a direção com que os elementos dentro do container serão dispostos. As opções são `row` e `column` para a property `flex-direction`.

Para organizar a distribuição dos elementos ao longo do espaço vertical ou horizontal utilizamos a property [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content). Seus possíveis valores são diversos, sendo os mais comuns `start`, `center`, `space-between` e `space-around`.


Muitas outras properties são utilizadas em layouts Flexbox. Recomendo a leitura do texto [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), o qual oferece uma visão detalhadas da técnica, valores de properties e efetivos gerados pelo uso da mesma.

Outro site interessante chama-se [Flexbox Froggy - A game for learning CSS flexbox](https://flexboxfroggy.com/). Nele você pode treinar seus conhecimentos de flexbox.







## 4. Grid Layout

O Grid Layout é um sistema bidimensional que permite dividir o espaço de uma página em linhas e colunas, tornando mais fácil o posicionamento dos elementos de forma precisa. Ele fornece controle total sobre o dimensionamento e o posicionamento dos elementos em relação ao layout da página.

O posicionamento dos elementos, tal qual ocorre em  uma tabela, é feito em linhas e colunas.

Exemplo:
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 10px;
}
```

Recomendo a leitura do texto [A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) para conhecer de forma mais aprofundada o funcionamento da técnica.





## Outras referências

- [Grid Layout - FR Unit](https://www.digitalocean.com/community/tutorials/css-css-grid-layout-fr-unit?utm_medium=content_acq&utm_source=css-tricks&utm_campaign=&utm_content=awareness_bestsellers)
- [CSS grid layout - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [CSS Grid](https://web.dev/learn/css/grid)