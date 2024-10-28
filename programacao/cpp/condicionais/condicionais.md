---
title: "Desvios Condicionais"
excerpt: ""
tags:
 - Programação
 - Linguagens de Programação
date: 2020-01-02 23:00:00

---

Na programação, os estruturas de seleção são um dos componentes básicos na construção dos programas. Entendemos por estruturas de seleção comandos que permitem desviar o fluxo natural de execução das instruções de um programa sob determinadas condições. Tais estruturas permitem criar ramificações de fluxo e estão intimamente relacionadas com o uso da lógica booleana.

Desta forma, a compreensão de desvios condicionais requer bons fundamentos de lógica, o que tentaremos oferecer na sequência, antes de propriamente apresentarmos os comandos de seleção.

## Lógica Booleana

Como sabemos, computação e matemática são áreas irmãs. Uma das mais relevantes contribuições da matemática incorporadas à computação foi do matemático inglês George Boole (1815-1864), que desenvolveu um sistema algébrico binário essencial ao funcionamento dos computadores. De modo simplificado, as ideias de Boole permitem obter conclusões lógicas a partir de variáveis que representam apenas dois valores (0 e 1) e operadores que retornam apenas dois valores (0 e 1).


!!! info "Dica"
    **0** indica FALSO e **1**, VERDADEIRO

A aplicação da Lógica Booleana, como normalmente é conhecida, vai desde a construção de circuitos de hardware a partir de portas lógicas até a programação, quando se faz necessário realizar testes lógicos no código. Mas afinal, o que são testes lógicos e qual é a relação destes com o sistema algébrico desenvolvido por Boole?


Nós, humanos, expressamos e avaliamos proposições lógicas a todo o momento. De forma prática, vamos entender **proposição lógica** como sendo uma `declaração que pode ser avaliada como VERDADEIRA ou FALSA, mas nunca ambas`. Logo, as duas afirmações abaixo podem ser consideradas proposições lógicas:

- *p*: Vai chover amanhã
- *q*: Tenho 10 reais na carteira


Tanto para *p* quanto para *q*, somente existem duas possibilidades de conclusão: **V**erdadeiro ou **F**also. Sabemos também que os operadores lógicos somente podem retornar **V** ou **F**, o que nos leva a concluir que expressões lógicas que combinam várias proposições, ao final, se reduzem a  **V** ou **F**. Mas, para elaborar tais expressões, precisamos conhecer o funcionamento de três operadores lógicos básicos: `AND`, `OR` e `NOT`.

!!! warning "Atenção"
    Estamos direcionando o entendimento da lógica booleana para a programação, omitindo alguns formalismos matemáticos propositalmente.


### Operador AND (conjunção)

O operador lógico **AND** (^), também conhecido como conjunção, é definido como sendo um `operador lógico binário que retorna VERDADEIRO sempre que TODOS os seus operandos forem verdadeiros`.

Para facilitar a compreensão, utilizamos uma tabela de valores lógicos, a **tabela verdade**, para expressar os possíveis resultados da aplicação do operador **AND** sobre duas proposições. Vamos supor que *p* tenha seus valores expressos na coluna e *q*, nas linhas. Deste modo, os possívels resultados de *p* ^ *q* são:

| **AND** | **V** | **F** |
|:---:|:-:|:-:|
|  **F**  | F | F |
|  **V**  | <span style="color:red;font-weight:bolder;">V</span>| F |



!!! info "Resumo"
    A conclusão lógica do operador AND somente é verdadeira se todas as proposições forem verdadeiras.




### Operador OR (disjunção)

O operador lógico **OR** (∨), também conhecido como disjunção, é definido como sendo um `operador lógico binário que retorna FALSO sempre que TODOS os seus operandos forem falsos`.

Utilizando a tabela verdade para expressar os possíveis resultados de *p* v *q* temos:

| **OR** | **V** | **F** |
|:---:|:-:|:-:|
|  **F**  | V | <span style="color:red;font-weight:bolder;">F</span> |
|  **V**  | V | V |



!!! info "Resumo"
    A conclusão lógica do operador OR somente é falsas se todas as proposições forem falsas.


### Operador NOT (~)

O operador lógico **NOT** (~), também conhecido como negação, é definido como sendo um `operador lógico unário que retorna a negação (inverso lógico) de seu operando`.

Utilizando a tabela verdade para expressar os possíveis resultados de *~p* temos:

| **p** | **~p** | 
|:---:|:-:|
|  **F**  |V |
|  **V**  | F |


!!! info "Resumo"
    A conclusão lógica do operador NOT é *verdadeiro* quando receber *falso*, e *falso* quando receber verdadeiro


Tudo bem, sabemos o que são proposições lógicas e conhecemos os três operadores lógicos básicos. Mas, de que forma utilizamos tais recursos na programação? ...É justamente isso que vou apresentar na sequência ;)


## Lógica booleana aplicada à programação


Microprocessadores possuem uma ou mais unidades lógico-aritméticas (ULA), componente que, como o próprio nome sugere, tem a capacidade de executar instruções aritméticas e instruções lógicas. Utilizando linguagens de programação de alto nível, como C++, temos acesso a estes recursos através de operadores, símbolos que a linguagem define para tais finalidades.

Especificamente sobre as operações lógicas, precisamos lembrar que o C++ define um tipo de dado específico para representar valores booleanos, o tipo [bool](identificadores.md#literais-booleanos). Quanto aos operadores lógicos, os símbolos utilizados são: `&&` para AND, `||` para OR e `!` para NOT.

Já os operadores de comparação principais são os seguintes:

| Operador |    Significado   | Exemplo |                Descrição                |
|:--------:|:----------------:|:-------:|:---------------------------------------:|
|     >    |     maior que    |  a > b  |     verdadeiro, se a for maior que b    |
|     <    |     menor que    |  a < b  |     verdadeiro, se a for menor que b    |
|    >=    | maior ou igual a |  a >= b | verdadeiro, se a for maior ou igual a b |
|    <=    | menor ou igual a |  a <= b | verdadeiro, se a for menor ou igual a b |
|    ==    |       igual      |  a == b |          verdadeiro, se iguais          |
|    !=    |     diferente    | a !== b |        verdadeiro, se diferentes        |


Utilizando os operadores lógicos e os operadores de comparação temos como escrever expressões lógicas em nossos programas. Imaginemos por um instante que estamos trabalhando em código para seleção de candidatos. Nossos critérios de seleção serão *idade igual ou superior a 18 anos, altura superior a 160cm e peso superior a 60kg*. Em nosso código, armazenamos a idade do candidato em uma variável inteira chamava `idade_c`, altura em uma variável inteira `altura_c` e peso, em uma variável de ponto flutuante `peso_c`.

Após atribuir os dados às respectivas variáveis, poderíamos codificar a expressão abaixo para determinar se o candidato será selecionado ou não:

```c++

bool is_selecionado = idade_c >= 18 && altura_c > 160 && peso_c > 60.0;

```

Observe que utilizamos o operador `&&`, uma vez que as três condições (proposições) devem ser atendidas. Portanto, a variável `is_selecionado` receberá `true` somente nesta situação.

Mas o que faremos com a variável `is_selecionado`? Sabemos que sendo `true` precisamos indicar ao usuário de nosso programa que o candidato atende os critérios. Ou seja, precisamos **condicionar** a execução de determinadas instruções do programa ao resultado de avaliação da expressão lógica. Como fazer então?


### Comando IF ELSE

Um dos comandos da linguagem C++ (e de boa parte das outras) é o `if`. Utilizamos ele para criar desvios condicionais na execução das instruções, que, pela ordem natural, são executadas em sequência.

A estrutura do comando `if` é simples e para demostrar, vamos seguir falando do nosso programa hipotético de seleção de candidatos. Observe o código a seguir:



```c++

bool is_selecionado = idade_c >= 18 && altura_c > 160 && peso_c > 60.0;

if (is_selecionado){
    cout << "Candidato atende aos critérios de seleção"<< endl;
} else {
    cout << "Candidato desclassificado"<< endl;
}

```

Perceba que existem três partes do comando `if` no código.

- **expressão lógica**: sempre fica entre os parênteses `()`. É parte obrigatória do comando e requer qualquer expressão lógica válida, que possa ser reduzida a `true` ou `false`. Em nosso exemplo, estamos avaliando o valor contido na variável `is_selecionado`, que é do tipo  `bool`. 
- **bloco de comandos para o resultado true**: é o primeiro par de chaves `{}` logo após a expressão lógica. Pode conter uma ou mais instruções, que serão executadas somente quando o resultado da expressão lógica for avaliado como `true`. É parte obrigatória do comando.
- **bloco de comandos para o resultado false (else)**: par de chaves imediatamente após a palavra `else`. Pode conter uma ou mais instruções que serão executadas somente quando o resultado da expressão lógica for avaliado como `false`. É parte *opcional* do comando.

Então, conforme explicamos, nosso código irá executar a instrução `cout << "Candidato atende aos critérios de seleção"<< endl;` quando `is_selecionado` for `true` e `cout << "Candidato desclassificado"<< endl;` quando for `false`.

A expressão lógica pode ser informada diretamente no comando `if`. Inclusive, esta é a forma mais comum de encontrá-la. Assim, podemos simplificar nosso trecho de código, eliminando a variável `is_selecionado`. Teríamos então:

```c++

if (idade_c >= 18 && altura_c > 160 && peso_c > 60.0){
    cout << "Candidato atende aos critérios de seleção"<< endl;
} else {
    cout << "Candidato desclassificado"<< endl;
}

```


### Comando IF ELSE IF

Uma variação do comando `if` permite especificar condições para os blocos `else`. Para demonstrar seu uso, vamos imaginar um novo programa que apresente a situação de estudantes com base na média final em determinada disciplina. A relação entre as notas e as respectivas situações estão na tabela que segue.

|   Nota  |  Situação |
|:-------:|:---------:|
|  0-4.9  | Reprovado |
| 5.0-6.9 |   Exame   |
|  7.0-10 |  Aprovado |


Uma possível codificação para o programa em questão seria:


```c++
/*definição de variáveis e leitura de dados...*/

if (nota>=0 && nota <=4.9){
    cout <<"Reprovado";
} else if (nota>=5.0 && nota <=6.9){
    cout <<"Exame";
} else {
    cout <<"Aprovado";
}


```

Note que o `else if` pode aparecer várias vezes na mesma instrução, tantas quantas forem necessárias. E, mais importante: assim que uma condição for avaliada como `true`, nenhuma outra da mesma instrução será avaliada. 


### Operador ternário

Para algumas situações, podemos utilizar uma simplificação de sintaxe da estrutura `if else` chamada **operador ternário**. Seu uso é especialmente interessante para testes simples, como aquele que fizemos no programa de seleção de candidatos. Veja a diferença:


```c++
    cout << (idade_c >= 18 && altura_c > 160 && peso_c > 60.0 ? "Candidato atende aos critérios de seleção": "Candidato desclassificado") << endl;
```

Pelo código, percebemos que a sintaxe do comando é: `expressão lógica ? valor quando true : valor quando false`. É simples de usar, mas pode prejudicar a legibilidade do código se aplicado para testes mais complexos. Vale o bom senso ;)

### Switch

Finalizamos nosso estudo com o comando `switch`,  uma estrutura de decisão baseada em casos. Antes de conhecermos a sintaxe do comando, vamos propor um código de exemplo:

```c++
    int nota;
    cin >> nota;

	switch(nota) {
		case 1:
		case 2:
		case 3:
		case 4:
			cout << "Reprovado" << endl;
			break;
		case 5 :
		case 6 :
			cout << "Exame" << endl;
			break;
		case 7 :
		case 8 :
		case 9 :
		case 10:
			cout << "Aprovado" << endl;
			break;
		default:
			cout << "Nota inválida" << endl;
	}	
```

Nosso exemplo trás importantes informações acerca da sintaxe e uso do comando `switch`. O primeiro deles é que devemos informar uma variável (ou expressão) que possa ser avaliada como inteiro ou tipo enumerável. No código, a variável `nota` entre parenteses `()` serve  a tal finalidade. Objetivamente estamos consultando o valor de `nota` e estabelecendo o que fazer para cada um dos valores de interesse. Estes valores de interesse estão expressos nos casos (`case`).

Então, se a leitura da variável `nota` indicar que seu valor é `4`, o programa vai executar as instruções `cout << "Exame" << endl;` e `break`. E se o valor for `1`, vai executar todas as instruções que seguem nos próximos `cases` até encontrar o `break`. 

Opa, como assim executar os "outros cases"? Exatamente isso: o comando `break` indica a interrupção do processamento do `switch`. Se ele não estiver presente, a execução irá iniciar pelo `case` pertinente ao valor da expressão, continuando até o final, passando pelas instruções de outros casos. Então, se você quer finalizar a execução naquele `case` específico, deve colocar o comando `break`.


Ok, mas por que o código anterior não tem break em vários `cases`? Bem, porque notas entre `1` e `4` estão associadas com a situação `Reprovado`. Para não repetir a mesma instrução várias vezes, colocamos o break somente no `case 4`. O mesmo vale para `5` e `6` e `7` a `10`.

Já o comando `default` é especial, executado quando nenhum dos `cases` anteriores corresponde ao valor da expressão avaliada. A presença do  `default` é opcional no comando `switch`.


Para mais informações sobre desvios condicionais, recomendo a leitura do [tutorial da W3C](https://www.w3schools.com/cpp/cpp_conditions.asp) que trata deste assunto.