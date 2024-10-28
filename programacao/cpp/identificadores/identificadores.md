---
title: "Literais e Identificadores"
excerpt: "A representação de objetos do programa e valores por ele manipulados é parte fundamental da programação. Cada linguagem define as regras de representação. Neste artigo veremos como definir literais e identificadores no C++."
tags:
 - Programação
 - Linguagens de Programação
date: 2020-01-14 15:37:00
toc: true
toc_label: "Neste artigo, você encontra"
toc_icon: "cog"
order: 1
header:
  teaser: /assets/images/c++/mudar.png
sidebar:
  nav: "cplusplus"
---

Codificar um software compreende, basicamente, modificar estados conforme sequência e regras previamente definidas. Neste processo, dar nomes às estruturas e, por vezes, inicializá-las com valores é tarefa trivial. 

Por ser praticamente indissociável da prática de programação, toda linguagem estabelece regras para nomenclatura de identificadores (nome que o programador atribui às estruturas) e para definição de literais (valores fixos).

Na sequência vamos abordar como variáveis e literais são definidos na linguagem C++.

# Variáveis

Um programa é composto por **instruções** e **dados**, ambos armazenados na memória RAM do computador. Enquanto que instruções, em sua maioria, representam que tipo de manipulação o processador deve executar com os dados (somas, subtrações, multiplicações, etc.), as variáveis representam os espaços de armazenamento de dados do programa.

Os dados são armazenados em **variáveis**, que nada mais são que espaços de memória RAM reservados para tal finalidade. Precisamos lembrar que variáveis apresentam alguma propriedades importantes:

- ***Nome***: O nome da variável é a identificação que o programador atribui à área de memória. O nome deve ser suficientemente claro para indicar o significado dos dados nela armazenados. A nomenclatura de variáveis deve respeitar as restrições impostas a identificadores da linguagem, bem como padrões de legibilidade de código que a boa prática recomenda. Também há diferença entre caracteres maiúsculos e minúsculos.
  
- ***Tipo***: Variáveis, em linguagens fortemente tipadas, devem indicar qual é a natureza dos dados que o programador poderá nelas armazenar. O tipo representa uma restrição, limitando o conjunto de valores aceitos. A linguagem C++ define um conjunto de tipos básicos. Sugiro a leitura [deste tutorial](http://www.cplusplus.com/doc/tutorial/variables/) para maiores detalhes.


No código apresentado ao final deste tutorial, você irá observar diversas declarações de variáveis. A título de exemplo, observe o trecho de código que segue. Nele são declaradas três variáveis, a saber, `contador`, `preco`, `lucro_liquido`. Estes são os nomes das variáveis. Já `int`, `float` e `double` representam o tipo de dado. 

No caso da variável *contador*, estamos fazendo a declaração e a inicialização em uma única instrução. Assim, tão logo criada, a variável receberá o valor `0`.

```c++
    int contador = 0;
    float preco;
    double lucro_liquido;
```

# Literais

Literal é todo valor informado de forma fixa no código. É comum utilizar a expressão `hard code` para descrever a operação. Normalmente os literais são utilizados para iniciar estruturas do programa, ou seja, definir seu valor inicial.

Os literais podem representar números inteiros, números reais, valores booleanos, caracteres ou sequência de caracteres. Para cada caso existem particularidades, as quais iremos tratar a seguir.

## Literais para números inteiros

[Números inteiros](https://pt.wikipedia.org/wiki/Número_inteiro)  são números não fracionais, ou seja, não apresentam valores após a vírgula. Sua representação se dá, normalmente, em base decimal. Contudo, o C++ aceita também números representados em [base octal](https://pt.wikipedia.org/wiki/Sistema_octal), [hexadecimal](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_hexadecimal) e [binária](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_bin%C3%A1rio).

Quando em **decimal**, um número pode ser expresso utilizando somente caracteres de 0 a 9. A representação decimal é a mais confortável na perspectiva do programador porque é o sistema de representação numérico do nosso dia-a-dia. Literais inteiros expressos em decimal podem utilizar aspa simples para demarcar milhares. Tal recurso conforme apenas maior legibilidade ao código-fonte. Observe o trecho de código a seguir:


```c++
    var_int = 24'000;       //base decimal    
```

A presentação **octal**, por sua vez, considera apenas caracteres de 0 a 7. Para informar literais octais em um programa C++, o programador deve prefixar o número com 0. Observe o código abaixo:

```c++  
    var_octal = 071;        //base octal   
```
Um método simples para conversão de octal para decimal é utilizar uma tabela de potências de base `8`. Isso porque assim como decimal, o octal é um sistema numérico posicional. Observe:


| 8<sup>3</sup> | 8<sup>2</sup> | 8<sup>1</sup> | 8<sup>0</sup> |
|----|----|----|----|
| | | 7 | 1|

Considerando a tabela de conversão, o valor octal `71` equivale a `57` em decimal, resultante de `8*7 + 1`.

No caso da representação **hexadecimal**, os caracteres aceitos são de `0` a `9` e de `A` a `F`. Todo literal hexadecimal deve ser prefixado com `0X` ou `0x`. A base hexadecimal é muito utilizada para expressar conteúdo de memória do computador, pois além de reduz a quantidade de caracteres necessários, o processo de conversão binário-hexadecimal é bastante simples. Observe o trecho de código a seguir:

```c++   
    var_hex = 0xF2;         //base hexadecimal    
```


Os caracteres de `A` a `F` do sistema hexadecimal equivalem a `10`, `11`, `12`, `13`,`14` e `15` no sistema decimal, respectivamente. Desta forma, para converter de hexadecimal para decimal, podemos utilizar a tabela de potências, agora com base `16`.

| 16<sup>3</sup> | 16<sup>2</sup> | 16<sup>1</sup> | 16<sup>0</sup> |
|----|----|----|----|
| | | F | 2|


Em nosso exemplo, `F2` equivale ao valor `242` em decimal, visto que é o resultado da expressão `15*16 + 2`.


E finalmente chegamos a representação **binária**, natural da máquina. Literais inteiros expressos em binário são sequências de `0s` e `1s` prefixados com `0b` ou `0B`.

## Literais para números de ponto flutuante

Ponto flutuante é o nome dado para um número real representado digitalmente no computador. Quando informamos um literal que expressa um número real na programação, devemos utilizar o caractere `.` para separar a parte decimal da inteira. Também é possível utilizar aspas simples para separar os milhares.

Números de ponto flutuante podem ser armazenados com precisão simples (identificados com o tipo `float`) ou com precisão dupla (tipo `double`). Números de precisão simples utilizam 32 bits de espaço de memória, enquanto números de precisão dupla utilizam 64 bits. Outra importante diferença refere-se a quantidade de casas decimais armazenadas: enquanto um tipo `float` armazena até `7` casas decimais, um `double` armazena `15` casas.  

```c++
    float var_float;
    double var_double;

    var_float = 1'234.34;
    var_double = 345;
```

## Literais booleanos

[Álgebra booleana](https://www.tecmundo.com.br/programacao/1527-logica-booleana-saiba-um-pouco-mais-sobre-esta-logica-e-como-ela-funciona.htm) é um formalismo matemático utilizado na computação para implementar testes lógicos. Na álgebra booleana temos dois estados possíveis para um proposição lógica: `verdadeiro` e `falso`. 

No C++, o estado `verdadeiro` é representado pelo literal `true` (ou pelo literal inteiro `1`). Já o estado `falso` é representado pelo literal `false` (ou pelo literal inteiro `0`). Observe o exemplo:

```c++
    bool var_true, var_false;
    var_true = true;
    var_false = false;

    var_true = 1;
    var_false = 0;
```


## Literais para caracteres
Caracteres são os símbolos do alfabeto, pontuação, entre outros. Nem todo caractere tem representação gráfica (quebra de linha e fim de arquivo, por exemplo). 

Para representar caracteres computacionalmente, pode-se utilizar `1` ou `2` bytes. O padrão [Unicode](https://www.unicode.org/standard/WhatIsUnicode.html) é a norma atual para representação de caracteres de forma universal, independentemente de plataforma, programa, linguagem ou mesmo idioma.

O padrão Unicode utiliza `2` bytes para representar o código numérico de cada um dos `137,929` caracteres existentes ([Versão 12](https://www.unicode.org/versions/Unicode12.0.0/UnicodeStandard-12.0.pdf))

Em C++, os literais de caracteres são representados envolvidos por aspas simples. Observe o exemplo:

```c++
    char var_char;
    var_char = 'c';
    var_char = 'B';

```

## Literais para strings

Strings são sequências de caracteres, ou simplesmente, a forma de expressar texto na programação. Literais são definidos no C++ por meio de aspas duplas, conforme demonstra o exemplo. 


```c++
    string var_string;
    var_string = "Olá, isso é um texto";
```

## Um pouco de código

Observe o código-fonte do programa a seguir. Perceba que nele são declaradas variáveis cuja inicialização faz uso dos literais que estudamos anteriormente. 

<script src="https://gist.github.com/diegolusa/97572b0ca9fbfdd74ffce4003a7e7172.js"></script>

