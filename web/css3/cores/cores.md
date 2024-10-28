---
title: "CSS3 - Cores"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00

---

Cores são um dos recursos mais importantes da linguagem CSS. Várias propriedades de estilo as utilizam, como àquelas que modificam bordas, preenchimento de fundo, texto e sombras, por exemplo.

Temos a disposição grande variedade de cores (mais de \(16\) milhões) e podemos especificá-las de várias formas. A mais simples é através do nome da cor, se a mesma constar no [rol de cores](https://www.tutorialrepublic.com/css-reference/css-color-names.php) suportadas pelo navegador e/ou predefinidas na especificação do CSS3. Embora simples, esta não costuma ser a forma mais adequada para definir valor de cor.

As outras opções que temos são `código hexadecimal` e as funções `rgb`, `rgba`, `hsl` e `hlsa`. Dentre todos, o código hexadecimal é a opção mais comum, correspondendo a um conjunto de \(6\) caracteres iniciado com o símbolo `#`. Estes caracteres representam a quantidade de vermelho, verde e azul que irá compor a cor final. Observe o esquema a seguir:

![Decomposição do código hexadecimal nos canais vermelho, verde e azul](../../img/web/cor.png)

Cada canal de cor pode receber valores entre `00` (sem cor) a `ff` (cor cheia). Logo, o código `#000000` é branco, enquanto que `#ffffff` indica a cor preta. Já para as funções `rgb` e `rgba`, a quantidade de cor de cada canal é definida no intervalo \(0\) a \(255\) e, no caso da `rgba`, um último valor entre \(0.0\) a \(1.0\) indicando a transparência aplicada [@csstutrep2021]. Observe:

```css
    body {
         background-color: #000010;
    }
    
    .artigo {
        background-color: rgb(200,240,255);
    }

    .secao {
        background-color: rgba(100,55,36,0.5);
    }
```
    O outro modelo de cores suportado chama-se [HSL](https://en.wikipedia.org/wiki/HSL_and_HSV) (*Hue-Saturation-Lightness*), especificado por meio das funções `hsl` e `hlsa`. Novamente a função terminada com *a* permite especificar o canal *alpha* para transparência.

```css
    .artigo {
        background-color: hsl(167,15,35);
    }

    .secao {
        background-color: rgba(167,40,35,0.5);
    }
```

Escolher cores e criar as combinações mais adequadas não é simples. Requer conhecimentos e uma boa percepção visual para que o resultado final seja agradável ao usuário. Contudo, especialistas ou não em cores, boas ferramentas de composição auxiliam muito no processo. É o caso dos sites [colordesigner.io](https://colordesigner.io/) e [material.io](https://material.io/resources/color/#!/?view.left=0&view.right=0).