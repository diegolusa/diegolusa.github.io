---
title: "HTML5 - Tabelas"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-09-06 08:00:00
---

A criação de tabelas requer o uso de diferentes elementos HTML de forma adequada. Temos elementos específicas para cabeçalho, rodapé, conteúdo, linhas e colunas. Na sequência abordaremos cada uma delas em detalhes.

A elemento `<table>` é utilizada para delimitar a tabela. Como descendentes, podemos indicar o cabeçalho, conteúdo e rodapé através das elementos `<thead>`, `<tbody>` e `<tfoot>`, respectivamente. Estas elementos não são obrigatorias e são aplicadas para adicionar semântica ao conteúdo da tabela.

Efetivamente, os dados da tabela estão contidos nas células de dados, criadas a partir do elemento `<td>`, organizadas em linhas especificadas a partir do elemento `<tr>`. Para células que representam cabeçalhos, podemos utilizar o elemento `<th>` para diferenciar das células de dados.

No exemplo que segue apresentamos um documento contendo uma tabela \(3 \times 4\). A primeira linha representa o cabeçalho, as duas intermediárias, os dados e a última, o rodapé. Fique atendo ao uso dos elementos para alcançar o resultado.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tabela</title>
    <meta charset="utf-8">
  </head>
  <body>
    <table>
        <thead>
            <tr>
                <th>Estudante</th>
                <th>Avaliação I</th>
                <th>Avaliação II</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Aluno 1</td>
                <td>9.5</td>
                <td>5.7</td>
            </tr>
            <tr>
                <td>Aluno 2</td>
                <td>8.6</td>
                <td>6.2</td>
            </tr>
    </tbody>
    <tfoot>
        <tr>
            <td></td>
            <td>8.7</td>
            <td>6.0</td>
        </tr>
    </tfoot>
    </table>
</body>
</html>

```

As linhas da tabela são criadas a partir da abertura de elementos `<tr>`. Em cada linha, devemos adicionar células, sejam de dados ou de cabeçalho, por meio de `<td>` e `<th>`. Cada nova célula requer a abertura e o fechamento do respectivo elemento dentro da linha. Contudo, em alguns casos, precisamos realizar mesclagem de células, o que demanda utilizar os atributos **rowspan** e **colspan**. Ao aplicar **rowspan**, indicamos que uma célula se projeta pela quantidade de linhas informada, enquanto que **colspan** indica a quantidade de colunas que a célula irá preencher.


```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tabela</title>
    <meta charset="utf-8">
  </head>
  <body>
    <table>
        <thead>
            <tr>
                <th colspan="4">Faturamento</th>
            </tr>
        </thead>
            <tbody>
                <tr>
                    <td colspan="2"></td>
                    <td>Filial A</td>
                    <td>Filial B</td>
                </tr>
                <tr>
                    <td rowspan="3">1º Trimestre</td>
                    <td>Janeiro</td>
                    <td>5</td>
                    <td>6</td>
                </tr>
                <tr>
                    <td>Fevereiro<br></td>
                    <td>4</td>
                    <td>5</td>
                </tr>
                <tr>
                    <td>Março</td>
                    <td>7</td>
                    <td>8</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

```

É importante ressaltar que as tabelas devem ser utilizadas para organizar dados e não para diagramar conteúdo. De fato, os primeiros *web sites* utilizavam tabelas como forma de posicionar conteúdo, mas na época não havia disponibilidade dos atuais recursos providos pelo HTML5 e CSS3. Portanto, hoje, evite essa má prática.

\bibliography