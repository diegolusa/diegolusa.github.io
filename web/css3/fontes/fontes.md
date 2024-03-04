---
title: "CSS3 - Fontes"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-10-13 08:00:00
---

A escolha de uma fonte é crucial para o sucesso de uma interface web, visto que está diretamente ligada à experiência de leitura do usuário (que deve ser agradável, naturalmente).

As propriedades de estilo que o CSS3 nos fornece para manipularmos fontes são `font-family`, `font-style`, `font-weight`, `font-size`, e `font-variant`. Na sequência iremos abordar cada uma delas:

## font-family

Especifica a família de fontes que o navegador deve utilizar para renderizar o texto. A propriedade aceita vários valores separados por vírgula, indicando opções de fontes quando não for possível utilizar a anterior. Normalmente finalizamos especificando uma das cinco famílias genérias de fonte disponíveis: *serif*, *sans-serif*, *monospace*, *coursive* e *fantasy* [@fontfamilymdn2021] [@cssw3s2021] [@csstutrep2021].

A família genérica deve ser utilizada para contornar a possibilidade do usuário não ter disponível em seu navegador as outras famílias listadas. Logo, nestes casos, o navegador conseguirá preservar o padrão tipográfico com outra fonte semelhante disponível [@fontfamilymdn2021] [@cssw3s2021] [@csstutrep2021]. 

Cada família de fontes genérica tem características tipográficas particulares. Vejamos quais são elas.

- `serif`: Cada glifo (símbolo) de caractere apresenta traços, terminações, de acabamento. 

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Garamond, serif;font-size: 0.9rem; border: black 1px solid;border-radius: 3px;">Exemplo de texto utilizando fonte serifada.</p>

-  `sans-serif`: Os glifos não apresentam traços de acabamento.

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif;font-size: 0.9rem; border: black 1px solid;border-radius: 3px;">Exemplo de texto utilizando fonte sem serifas.</p>

-  `monospaced`: Cada glifo ocupa o mesmo espaço (mesmo tamanho). Assemelha-se com a forma de escrita das antigas máquinas de escrever.

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:'Courier New', monospaced;font-size: 0.9rem; border: black 1px solid;border-radius: 3px;">Exemplo de texto utilizando fonte monoespaçada.</p>

-  `cursive`: Os glifos assemelham-se a escrita manual.

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:'Lucida Handwriting', cursive;font-size: 0.9rem; border: black 1px solid; border-radius: 3px;">Exemplo de texto utilizando fonte cursiva.</p>

- `fantasy`: São fontes artísticas.


<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Copperplate, fantasy;font-size: 0.9rem; border: black 1px solid;border-radius: 3px;">Exemplo de texto utilizando fonte artística.</p>



## font-style

Propriedade que permite especificar a apresentação da face dos glifos, se normais, em itálico ou oblíquos [@cssw3s2021] [@csstutrep2021]. Os possíveis valores são:

-  `normal`

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif;font-size: 0.9rem; border: black 1px solid;border-radius: 3px; ">Normal (padrão).</p>

-  `italic`

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif;font-size: 0.9rem; border: black 1px solid;border-radius: 3px; font-style:italic">Em itálico.</p>

-  `oblique`

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif;font-size: 0.9rem; border: black 1px solid;border-radius: 3px; font-style:oblique">Oblíquo (quase igual ao itálico).</p>


## font-size

Permite especificar o tamanho da fonte, a partir de medidas relativas, como percentual, *em*, *rem*, etc ou medidas absolutas como *pixels*. Para saber mais sobre unidades de medida, acesse [nosso conteúdo sobre o tema](unidades-medida.md) [@cssw3s2021] [@csstutrep2021].

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif; border: black 1px solid;border-radius: 3px; font-style:oblique">
<span style="font-size: 16px">16px</span> - <span style="font-size: 2rem">2rem</span> - <span style="font-size: 2em">2em</span> </p>


## font-weight

Define o peso (intensidade de negrito)  da fonte. Os valores podem ser `normal`, `bold`, `bolder`, `lighter`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900` e `inherit`. Os valores numéricos indicam uma graduação de negrito. O valor `400` equivale a `normal` enquanto que o valor `700` é equivalente a `bold`. Os valores `bolder` e `lighter` aplicam-se em relação ao peso herdado do ancestral, enquanto que `normal` e `bold` aplicam-se em absoluto ao texto (sem relação com o valor do ancestral) [@cssw3s2021] [@csstutrep2021].


<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif; border: black 1px solid;border-radius: 3px; font-style:oblique">
<span style="font-weight: 200">Valor 200</span> - <span style="font-weight: 400">Valor 400</span> - <span style="font-weight: 600">Valor 600</span> - <span style="font-weight: 900">Valor 900</span> </p>



## font-variant

Indica se o texto deve ser exibido ou não considerando apenas caracteres maiúsculos. Os valores possíveis são `small-caps` e `normal` (padrão) [@cssw3s2021] [@csstutrep2021].

<p style="margin-left: 10%;margin-right: 10%;text-align: center; font-family:Arial, sans-serif; border: black 1px solid;border-radius: 3px; font-style:oblique">
<span style="font-variant: normal">Escrita normal</span> - <span style="font-variant: small-caps">Escrita em small caps</span></p>




\bibliography