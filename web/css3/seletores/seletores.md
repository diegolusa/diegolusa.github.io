---
title: "CSS3 - Seletores"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-14 08:00:00
---

Seletores são parte de uma regra de estilo. Sua função é orientar o navegador, por meio de um padrão de pesquisa, a encontrar os elementos que devem receber o estilo no documento [@csstutrep2021]. Normalmente escrevemos diversas regras para obter o resultado final desejado. Vamos iniciar com uma simples para observarmos sua sintaxe.

```css
p {
        text-align: center;
        color: yellow;
        font-family: "Brush Script MT", cursive;
        font-size: 40px;
      }
```

A regra acima tem como seletor `p`, indicando que todos os elementos do tipo *parágrafo* do documento devem receber as propriedades de estilo definidas. Cada par de *propriedade:valor* corresponde a uma declaração. Perceba que toda declaração finaliza com um ponto-e-vírgula `;` e que as declarações ficam envolvidas entre chaves `{}`.


!!! info "Que tal conhecermos alguns tipos de seletores disponíveis 😉? [@csstutrep2021]"
    === "Universal"
        Todo elemento da página irá receber o estilo. Utilizamos `*` como seletor.
        ```css
            * { 
            margin: 0px;         
            }
        ``` 
    === "Elemento"
        Especificamos o nome dos elementos HTML que devem receber o estilo no seletor.
        ```css
            p { 
            color: black;         
            }
        ```
    === "Id"
        Todo elemento HTML possui um atributo chamado [`id`](https://www.w3schools.com/tags/att_global_id.asp). Este atributo é utilizado para identificar de forma única um elemento no documento. Isso significa que dois elementos não podem compartilhar o mesmo valor em `id`. No CSS, podemos especificar um seletor para valores de `id` utilizando o caractere `#` acompanhado do valor de `id` correspondente.
        ```css
        #cabecalho { 
            background-color: black;         
            }
        ```
    === "Classe"
        Outro atributo global de elementos do HTML5 chama-se [`class`](https://www.w3schools.com/tags/att_global_class.asp). Diferentemente de `id`, diferentes elementos podem compartilhar do mesmo valor em `class` e, além disso, vários valores são aceitos, deixando-se um espaço entre eles. Seletores baseados em classe são amplamente utilizados. Sua construção requer o uso do caractere ponto `.` acompanhado do nome da classe.

        Podemos deixar o seletor mais específico, associando com um seletor de elemento, como em `p.importante`. A interpretação, neste caso, é *todo parágrafo que contém a classe importante*.
        ```css
            .artigo { 
                text-align: justify;
            }
            p.importante {
                color:red
            }
        ```
    === "Descendentes"
        Utilizamos este tipo de seletor para aplicar estilos a elementos com base em seus elementos "pai". Podemos selecionar, por exemplo, todos os parágrafos (`<p>`) que são descendentes de artigos (`<article>`), desconsiderando todos os demais. Nosso seletor seria escrito da seguinte forma:
        ```css
            article p { 
                font-family: 'Roboto', sans-serif;
            }           
        ``` 
        Observe que este seletor considera descendentes diretos e indiretos. Para ser mais restritivo e considerar somente elementos que são "filhos" diretos, devemos utilizar o símbolo `>`, conforme o exemplo a seguir:
        ```css
            article > p { 
                font-family: 'Roboto', sans-serif;
            }           
        ``` 
    === "Elementos adjacentes"
        São seletores que consideram elementos de mesmo nível ("irmãos", pois são filhos do mesmo "pai"). Se quisessemos aplicar um estilo específico para o primeiro parágrafo (`<p>`) que segue um título de segundo nível (`<h2>`), poderíamos utilizar:
        ```css
            h2 + p { 
                font-family: 'Roboto', sans-serif;
            }           
        ``` 
\bibliography
