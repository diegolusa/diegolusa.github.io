---
title: "CSS3 - Posicionamento"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---

O CSS3 oferece diferentes maneiras de posicionar elementos em tela. Na sequência iremos abordar com detalhes cada um deles.


## Position


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

## Float

A propriedade `float` é usada para alinhar elementos ao lado esquerdo ou direito de seu contêiner. Isso é frequentemente utilizado para criar layouts de várias colunas. No entanto, é importante notar que o uso excessivo de `float` pode causar problemas de layout e é geralmente evitado em favor de técnicas mais modernas, como Flexbox e Grid Layout.

Exemplo:
```css
.coluna {
  float: left;
  width: 50%;
}
```

## Flexbox Layout

O Flexbox é um modelo de layout bidimensional que oferece controle e flexibilidade na disposição dos elementos em relação aos métodos tradicionais de layout. Ele permite o alinhamento e distribuição de elementos em qualquer direção, tornando-o ideal para criar layouts responsivos e complexos.



Para fazer uso do flexbox precisamos definir um container em torno dos elementos que deverão ser posicionais de maneira responsiva. Para isso, é preciso utilizar a property `display:flex`. Normalmente você definirá uma classe para isso, como a exibida a seguir:

```css
.container {
  display: flex;
}
```

O Flexbox organiza os itens ao longo de um eixo principal (`main axis`) e um eixo transversal (`cross axis`). A direção dos eixos pode ser definida com a propriedade `flex-direction`, cujas opções podem ser `row` e `column`. Já para controlar a distribuição de espaço e a ordenação dos itens no eixo principal e transversal usamos as propriedades `justify-content` e `align-items`

Existem várias outras propriedades aplicáveis no contexto de layouts flex. As principais são:


- `flex-direction`: Define a direção do eixo principal (`row`, `row-reverse`, `column`, `column-reverse`).
- `justify-content`: Distribui espaço ao longo do eixo principal (`flex-start`, `flex-end`, `center`, `space-between`, `space-around`).
- `align-items`: Alinha os itens ao longo do eixo transversal (`flex-start`, `flex-end`, `center`, `baseline`, `stretch`).
- `flex-wrap`: Define se os itens devem quebrar para uma nova linha (`nowrap`, `wrap`, `wrap-reverse`).
- `align-content`: Alinha as linhas do container flexível quando há espaço extra (`flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch`).


Recomendo a leitura do texto [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), o qual oferece uma visão detalhadas da técnica, valores de properties e resultados gerados pelo uso das mesmas. Outro site interessante chama-se [Flexbox Froggy - A game for learning CSS flexbox](https://flexboxfroggy.com/). Nele você pode treinar seus conhecimentos de FlexBox.




## Grid Layout

O Grid Layout é um sistema bidimensional que permite dividir o espaço de uma página em linhas e colunas, tornando mais fácil o posicionamento dos elementos de forma precisa. Ele fornece controle total sobre o dimensionamento e o posicionamento dos elementos em relação ao layout da página.

O posicionamento dos elementos, tal qual ocorre em  uma tabela, é feito em linhas e colunas. Para usar o Grid Layout, é necessário definir um container que usa a propriedade `display: grid;`.

Para definir o número e o tamanho das linhas e colunas do layout utilizamos as propriedades `grid-template-columns` e `grid-template-rows`. Observe que há uma unidade de medida chamada *fr*, a qual representa uma fração do viewport, cujo tamanho é calculado automaticamente pelo navegador. Ao multiplicar *fr* por um valor diferente de *1*, estamos indicando que a coluna ou linha terá *x* vezes o tamanho original. Ou seja, *3fr* corresponde a *3x* o tamanho de uma fração.


Exemplo:
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 10px;
}
```


Outra propriedade interessante chama-se `grid-area`. Ela pode ser usada de duas maneiras principais: *nomear áreas de grade em um contêiner de grade* e *posicionar itens de grade dentro dessas áreas nomeadas ou definir explicitamente a posição e a abrangência de um item de grade*. Vamos descrever cada uma delas:

### Definir áreas nomeadas

No contêiner de grade, usando a propriedade `grid-template-areas`, atribuímos a cada célula da grade um nome, os quais serão posteriormente utilizados para posicionar os itens.

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Três colunas */
    grid-template-rows: auto auto auto; /* Três linhas */
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
}
```

Neste exemplo, três áreas nomeadas são criadas: `header`, `sidebar`, `main` e `footer`. A área `header` abrange todas as três colunas na primeira linha, `sidebar` ocupa a primeira coluna na segunda linha, `main` ocupa as duas últimas colunas na segunda linha, e `footer` abrange todas as três colunas na terceira linha.

### Posicionar items em áreas nomeadas

Após definir áreas nomeadas, posicionamos os itens dentro dessas áreas usando a propriedade `grid-area`. Veja o exemplo:

```css
.header {
    grid-area: header;
}

.sidebar {
    grid-area: sidebar;
}

.main {
    grid-area: main;
}

.footer {
    grid-area: footer;
}
```


A propriedade `grid-area` também pode ser usada para definir explicitamente a posição de um item de grade baseado em índices de linha e coluna. Os valores necessários são quatro, a saber: linha inicial, coluna inicial, linha final e coluna final.

```css
.item {
    grid-area: 1 / 2 / 3 / 4; /* Da linha 1 à linha 3 e da coluna 2 à coluna 4 */
}
```

Recomendo a leitura do texto [A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) para conhecer de forma mais aprofundada o funcionamento da técnica.



## Outras referências

- [Grid Layout - FR Unit](https://www.digitalocean.com/community/tutorials/css-css-grid-layout-fr-unit?utm_medium=content_acq&utm_source=css-tricks&utm_campaign=&utm_content=awareness_bestsellers)
- [CSS grid layout - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [CSS Grid](https://web.dev/learn/css/grid)
- [Grid e Flex Layout Cheat Sheet](https://www.paradigmadigital.com/assets/cms/cheat_sheet_flexbox_6fb013edd1.pdf)