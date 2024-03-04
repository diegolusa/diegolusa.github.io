---
title: "CSS3 - Fundamentos"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---

Sabemos que utilizamos HTML5 para estruturar e atribuir semântica ao conteúdo de documentos na Web, mas é fato que o resultado final é pouco atrativo ao usuário, pois carece de cores, posicionamento e outros elementos estéticos. Neste sentido, iniciamos nosso estudo da linguagem `CSS3` (*Cascading Style Sheets*), que, ao ser incorporada a documentos HTML, permite alterar a representação gráfica dos componentes.

Embora a versão \(3\) seja recente, o `CSS` é uma linguagem que foi apresentada em 1994. Ao longo do tempo foi sendo aperfeiçoada, gerando as *major versions* \(1\), \(2\) e \(3\).

A versão \(3\) da linguagem CSS é uma evolução da versão \(2\). Podemos classificar os recursos da linguagem em diferentes módulos, cada qual com finalidade específica. Estes módulos são [@tutpoints21]:

+ **Selectors**
+ **Box Model**
+ **Backgrounds**
+ **Image Values and Replaced Content**
+ **Text Effects**
+ **2D Transformations**
+ **3D Transformations**
+ **Animations**
+ **Multiple Column Layout**
+ **User Interface**

Em nosso estudo, iremos abordar os tópicos mais básicos da linguagem, buscando explorar um pouco de cada módulo. Começaremos analisando os seletores, fundamentais dentro do escopo de uso da linguagem. Contudo, antes é necessário que conheçamos como incorporar código CSS à nossos documentos, certo?

## Sintaxe

A linguagem CSS3 fornece, basicamente, um vasto conjunto de propriedades de estilo, funções e outras construções que podemos utilizar para modificar algum aspecto da aparencia dos elementos HTML5.

Uma propriedade de estilo é definida por um nome e um valor. Por exemplo, se desejamos justificar determinado texto, podemos escrever o seguinte trecho de código:

```css
text-align:justify;
```
A propriedade chama-se `text-align` e seu valor foi configurado para `justify`, o qual indica que o texto deve ser justificado. Ao final, é necessário colocar `;`. Um mesmo elemento pode receber diversas configurações de estilo através do uso de diferentes propriedades.

Podemos encontrar informações sobre cada propriedade do CSS3 no site da [W3Schools](https://www.w3schools.com/csSref/). 


## Incorporação

A incorporação de código CSS3 a documentos HTML5 pode ser realizada de três formas distintas: arquivo externo, elemento `<style>` ou atributo `style` (*inline*). Vejamos como configuramos cada opção.

Estilos `inline` são aqueles que acompanham o elemento, sendo definidos no atributo `style`. Devem ser utilizados com cautela, pois são difíceis de alterar quando aparecem em grande quantidade no documento. É o caso do elemento `h1` do documento apresentado na sequência. Perceba que o estilo se aplica *somente* ao elemento.

```html
<!DOCTYPE html>
<html>    
	<body>
		<h1 style="color:blue;margin-left:30px;text-align:center;">Titulo</h1>
	</body>
</html>
```

Quando utilizamos o elemento `<style>` temos maior flexibilidade na aplicação dos estilos pois, diferentemente do modo `inline`, podemos aplicar o mesmo estilo a vários elementos do documento por meio de `regras`. Iremos conhecer o conceito de regra de estilo mais a frente, por ora basta pensar nelas como um critério para estabelecer quem (elementos) irá receber as propriedades de estilo.

Observe que o elemento `<style>` deve ser adicionado dentro de `<head>` e todas as regras de estilo devem ser escritas como conteúdo do elemento.


```html linenums="1" hl_lines="6-31"
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8" />
    <title>Minha primeira página Web</title>
    <style>
      body {
        background-color: rgb(159, 169, 170);
      }

      p {
        text-align: center;
        text-decoration: underline;
        font-weight: bolder;
        font-style: italic;
        color: yellow;
        font-family: "Brush Script MT", cursive;
        font-size: 40px;
      }

      h1,
      h2,
      h3,
      h4,
      h5,
      h6 {
        color: black;
        text-transform: uppercase;
        font-family: "Noto Sans", sans-serif;
      }
    </style>
  </head>
  <body>
    
    <h1>Introdução ao CSS3</h1>
    <p>
     Vamos falar de CSS!
    </p>
    <h2>Conceitos básicos</h2>
    <p>O conceito...</p>
    <p >Outro conceito...</p>
  </body>
</html>

```

A terceira forma, em que utilizamos a vinculação de um arquivo com regras de estilo ao documento é a mais utilizada. Isso porque, quando pensamos em um site, devemos considerar a existência de muitos documentos e, todos eles compartilhamento da mesma apresentação. Logo, ao deixarmos as regras de estilo em um único local, podemos facilmente compartilhá-las em todos os documentos sem a necessidade de repetir código. 

Para realizar a vinculação de um arquivo CSS ao documento devemos utilizar a tag `<link>`, que também deve estar no `<head>`. Observe o exemplo:



```html linenums="1" hl_lines="6"
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8" />
    <title>Minha primeira página Web</title>
    <link href="estilos.css" rel="stylesheet"/>
  </head>
  <body>
    
    <h1>Introdução ao CSS3</h1>
    <p>
     Vamos falar de CSS!
    </p>
    <h2>Conceitos básicos</h2>
    <p>O conceito...</p>
    <p>Outro conceito...</p>
  </body>
</html>
```

Em um documento HTML, nós podemos ter simultaneamente as três formas de incorporação de CSS. Neste caso, o navegador utiliza uma escala de prioridade, afinal é possível que haja sobreposição de estilos. Nesta escala, a **maior prioridade** fica com as propriedades `inline`, seguidas daquelas definidas para o documento na tag `<style>` e, por último, as regras oriundas dos arquivos incorporados via `<link>` [@csstutrep2021].



\bibliography