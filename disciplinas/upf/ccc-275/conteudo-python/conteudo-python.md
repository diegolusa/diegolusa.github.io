---
title: "Python - Introdução"
tags:
 - Programação
 - Linguagens de Programação
 - Python
date: 2024-02-26 08:00:00
---

A programação é o processo de escrever instruções que serão executadas por um computador para realizar tarefas específicas. Essas instruções são escritas em **linguagens de programação**, que servem como uma ponte entre o pensamento humano e a máquina. A sequência de passos elaborada pelo programador para alcançar a solução de um problema é chamada de **algoritmo**. Existem diferentes estratégias/abordagens para expressar e organizar um algoritmo em código. Estas abordagens recebem o nome de **paradigmas de programação**.

Logo, de forma objetiva, temos:


- **Paradigma de Programação – O Estilo ou Abordagem**
  - Um paradigma de programação define o estilo, a abordagem e as diretrizes de como o código será escrito e organizado.
  - Ele estabelece o “como pensar” sobre a solução de um problema usando conceitos específicos.
  - Exemplo:
      - No paradigma imperativo, pensamos em uma sequência de passos a serem seguidos.
      - No paradigma orientado a objetos, pensamos em termos de objetos que interagem entre si.
      - No paradigma funcional, pensamos em funções que recebem entradas e retornam saídas, sem alterar o estado.

- **Algoritmo – A Solução**
    - Um algoritmo é uma sequência finita de passos ou instruções que resolve um problema.
    - É independente de linguagem e paradigma: um algoritmo pode ser descrito em português, em pseudocódigo ou implementado em qualquer linguagem de programação.
    - No entanto, o paradigma escolhido influencia a forma como o algoritmo é estruturado.
   

- **Linguagem de Programação – A Ferramenta ou Meio**
    - Uma linguagem de programação é o meio pelo qual o programador expressa o algoritmo seguindo as regras de um paradigma. É um idioma com regras específicas usada para comunicar ao computador o que ele deve executar.
    - Cada linguagem tem sua sintaxe, semântica e recursos específicos, mas algumas suportam múltiplos paradigmas.
    - Exemplo:
            - Python suporta paradigmas imperativo, orientado a objetos e funcional.
            - C é mais focada no paradigma imperativo/procedural.
            - Haskell é fortemente funcional.
  

# Linguagem Python


Python é uma linguagem de programação de alto nível, interpretada, multi paradigma e de tipagem dinâmica. Desenvolvida por [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) e lançada pela primeira vez em 1991, Python ganhou imensa popularidade devido à sua sintaxe simples e legibilidade, tornando-a uma escolha preferida para uma variedade de aplicações, desde desenvolvimento web, ciência de dados, engenharia de dados e automação de tarefas, por exemplo. Possui um ecossistema muito rico em bibliotecas e ferramentas, as quais ajudaram a tornar a linguagem uma das mais populares no mercado de tecnologia atual. 

## Variáveis e Constantes

Em Python, as variáveis são utilizadas para armazenar valores e são declaradas atribuindo um valor a um nome específico. Ao contrário de outras linguagens, Python não exige a declaração explícita de tipos de dados, pois opera sob o princípio da tipagem dinâmica (o tipo de dado é inferido pelo intepretador na medida que o código é analisado).

No exemplo a seguir estamos declarando duas variáveis. A primeira chama-se `numero` e a segunda, `nome`. Na primeira, o tipo de dado é inteiro e sabemos disso a partir do valor atribuído. Já na segunda linha, a variável `nome` é inicializada com uma cadeia de caracteres, também conhecida como `string`.

```python
numero = 10
nome = "Maria"
```

No Python não temos palavra reservada para declarar constantes. Neste caso, utilizamos uma convenção, colocando o nome em caixa alta. Todavia, são variáveis como qualquer outra.

```python
PI = 3.14159
GRAVIDADE = 9.8
```


## Indentação de código

Em Python, a indentação é um conceito fundamental e parte integrante da sintaxe da linguagem. Diferentemente de muitas outras linguagens de programação, que utilizam chaves `{}` para delimitar blocos de código, Python utiliza a indentação para definir a estrutura e a organização do código.

A indentação é utilizada para indicar a estrutura hierárquica do código, especialmente em construções como loops, condicionais, funções e classes. Ela define quais linhas de código estão dentro de um determinado bloco e quais estão fora.

Por convenção, é recomendado utilizar *quatro espaços* para cada nível de indentação. Embora o uso de tabulações (tab) seja permitido, é uma prática comum e recomendada seguir a convenção de espaços. Isso garante consistência em todo o código e evita problemas de formatação em diferentes ambientes de desenvolvimento. Para esta tarefa as IDEs (*Integrated Development Environment*) são muito importantes, pois automatizam boa parte desta atividade.

```python
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

No exemplo acima, as linhas de código dentro do bloco `if` e `else` estão indentadas com quatro espaços, indicando que elas pertencem a esses blocos condicionais.

!!! note "O que são blocos"
    Bloco é uma estrutura de código em que as instruções estão no mesmo nível e compartilham de um mesmo escopo de visibilidade. São os blocos que permite construções como laços de repeticão, condicionais, funções e classes, por exemplo.



## Tipos de Dados

Python oferece diversos tipos de dados embutidos, incluindo:

- **Inteiros (int)**: Números inteiros, como `1`, `100`, `-5`.
- **Float (float)**: Números de ponto flutuante, como `3.14`, `2.0`, `-0.5`.
- **String (str)**: Sequência de caracteres, como `"Olá, mundo!"`, `'Python é legal'`. (perceba que podemos inicializar com aspas simples ou duplas)
- **Booleano (bool)**: Valores verdadeiro (`True`) ou falso (`False`).
- **Lista (list)**: Coleção ordenada e *mutável* de itens.
- **Tupla (tuple)**: Coleção ordenada e *imutável* de itens.
- **Dicionário (dict)**: Coleção *não ordenada* de pares de chave-valor.
- **Conjunto (set)**: Coleção *não ordenada* de itens únicos.


| Tipo  | Descrição                                                                                                 | Exemplo                              |
| ----- | --------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| int   | Números inteiros, positivos ou negativos, sem casas decimais.                                             | x = 10, y = -5                       |
| float | Números reais, com casas decimais. Também pode representar notação científica.                            | pi = 3.14, e = 2.7e3                 |
| str   | Cadeia de caracteres (texto). Deve ser delimitada por aspas simples ou duplas.                            | nome = "Python", s = 'Oi'            |
| bool  | Valores booleanos que representam verdadeiro (True) ou falso (False).                                     | ativo = True, erro = False           |
| list  | Coleção ordenada e mutável de itens, que pode conter diferentes tipos de dados. Definida entre colchetes. | nums = [1, 2, 3]                     |
| tuple | Coleção ordenada e imutável de itens. Definida entre parênteses.                                          | cores = ("azul", "vermelho")         |
| set   | Coleção desordenada de itens únicos. Definida entre chaves.                                               | vogais = {'a', 'e', 'i'}             |
| dict  | Estrutura que armazena pares chave-valor. Definida entre chaves com dois pontos separando chave e valor.  | aluno = {"nome": "Ana", "idade": 20} |



## Entradas e Saídas

Para receber entrada do usuário, Python oferece a função `input()`. O valor retornado após executar a função foi o que o usuário digitou no terminal. Aqui estamos falando de entrada em terminal, ou seja, sem uso de interface gráfica.

No trecho de código que segue, a mensagem `Digite seu nome: ` é impressa na tela e o cursor fica aguardando a entrada do usuário. Após o usuário digitar os dados e pressionar ENTER, o valor é armazenado na variável `nome`.

```python
nome = input("Digite seu nome: ")
```

Já para exibir informações para o usuário, podemos usar a função `print()`, conforme o exemplo a seguir. No código em questão, será impresso na tela a mensagem `Olá, ` acompanhada do valor da variável `nome`.

```python
print("Olá,", nome)
```

## Operadores Aritméticos

Os operadores aritméticos são utilizados para realizar operações matemáticas em valores numéricos. Em sua grande maioria, são os mesmo da Matemática e representam operações como adição, subtração, multiplicação, divisão, por exemplo. Na sequência vamos apresentar eles.


!!! info "Operadores Aritméticos"

    === "Adição (+)"

        ```python
        resultado = 5 + 3
        ```

    === "Subtração (-)"

        ```python
        resultado = 10 - 7
        ```

    === "Multiplicação (*)"

        ```python
        resultado = 4 * 6
        ```

    === "Divisão (/)"

        ```python
        resultado = 20 / 5
        ```

    === "Divisão Inteira (//)"

        ```python
        resultado = 20 // 6
        ```

    === "Resto da Divisão (%)"

        O operador de resto da divisão (%) retornar o resto da divisão inteira entre o dividendo e o divisor.

        ```python
        resto = 20 % 6
        ```

    === "Exponenciação (**)"

        O operador de exponenciação (**) é utilizado para elevar um número a uma potência

        ```python
        resultado = 2 ** 3
        ```


## Comentários

Comentários são trechos de texto dentro do código-fonte que são ignorados pelo interpretador Python durante a execução do programa. Eles são utilizados para explicar o código, fazer anotações, fornecer documentação ou desativar temporariamente partes do código. Seu uso é altamente recomendável, pois auxilia na documentação do código.

Temos a disposição diferentes duas maneiras distintas de comentar código: c**omentário de linha** e **comentário de bloco**. Comentários de linha começam com o símbolo `#` e continuam até o final da linha. São úteis para adicionar breves explicações ou notas em uma única linha de código.

```python
# Este é um comentário de linha
numero = 10  # Este comentário segue o código na mesma linha
```

Já os comentários em bloco são utilizados para comentários que excedem uma linha e são delimitados por três aspas simples (`'''`) ou três aspas duplas (`"""`). Eles são frequentemente utilizados para documentar funções, classes ou trechos de código de maneira mais extensa. 
```python
'''
Este é um comentário em bloco.
Ele pode abranger várias linhas.
'''
print("Isso é um teste")

```

Quando pensamos em comentários devemos levar em consideração alguns critérios importantes para torná-los realmente úteis no processo de desenvolvimento. Os principais deles são:

-  Escrever comentários suficientemente descritivos que irão apoiar o entendimento do algoritmo
-  Não comentar situações óbvias
-  Padronizar a escrita de comentários no código-fonte.



## Conversões de Dados

Conversão de dados é um tipo de operação em que é solicitado a mudança de representação de um tipo  para outro. Considere uma variável qualquer com o valor `124` em formato de texto, mas que precisamos representá-la como inteira para aplicar operações aritméticas na sequência. Este é o objetivo da conversão de dados, conhecida também como *type casting*.

É importante frisar as possibilidades de conversão são restritas às características do valor de origem e que em algumas situações a conversão irá implicar em perda de dados.

!!! info "Conversões entre tipos de dados"

    === "Conversão de Inteiro para String"

        Para converter um número inteiro em uma string, utilizamos a função `str()`.

        ```python
        numero = 10
        numero_string = str(numero)
        ```

    === "Conversão de String para Inteiro"

        Para converter uma string em um número inteiro, utilizamos a função `int()`.

        ```python
        numero_string = "10"
        numero = int(numero_string)
        ```

    === "Conversão de String para Float"

        Para converter uma string em um número de ponto flutuante (float), utilizamos a função `float()`.

        ```python
        numero_string = "3.14"
        numero_float = float(numero_string)
        ```

    === "Conversão de Float para Inteiro"

        Para converter um número de ponto flutuante em um número inteiro, aplicamos a função `int()`. Isso porque a função remove a parte decimal do valor.

        ```python
        numero_float = 3.14
        numero_inteiro = int(numero_float)
        ```


## Strings

As strings são usadas para representar texto e são imutáveis, o que significa que uma vez que uma string é criada, ela não pode ser alterada. O Python fornece uma grande variedade de métodos embutidos para manipular e operar em strings de maneira eficiente. Aqui vamos explorar os métodos mais comuns. Caso você queira conhecer em detalhes todos os métodos, acesse  [a documentação oficial sobre cadeias de caracteres](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) da linguagem.


!!! info "Métodos para manipulação de strings"

    === "`len()`"

        Retorna o comprimento da string, ou seja, o número de caracteres presentes nela.

        ```python
        string = "Olá, mundo!"
        print(len(string))
        ```
        === "`upper()` e `lower()`"

        `upper()` converte todos os caracteres da string para maiúsculo, enquanto `lower()` os converte para minúsculo.


        ```python
        string = "Olá, Mundo!"
        print(string.upper())
        print(string.lower())
        ```

    === "`strip()`, `lstrip()` e `rstrip()`"

        Removem espaços em branco e caracteres especiais do início e/ou final da string.

        Exemplo:
        ```python
        string = "   Olá, Mundo!   "
        print(string.strip())
        print(string.lstrip())
        print(string.rstrip())
        ```

    === "`split()` e `join()`"

        `split()` divide a string em uma lista de substrings com base em um separador, enquanto `join()` junta uma lista de strings em uma única string.


        ```python
        string = "Python é uma linguagem de programação"
        lista = string.split()
        print(lista) 

        string_nova = "-".join(lista)
        print(string_nova)
        ```

    === "`replace()`"

        Substitui todas as ocorrências de uma substring por outra.

        ```python
        string = "Python é incrível!"
        nova_string = string.replace("incrível", "fantástica")
        print(nova_string)
        ```

    === "`startswith()` e `endswith()`"

        Verificam se a string começa ou termina com uma determinada substring, respectivamente.

        Exemplo:
        ```python
        string = "Olá, Mundo!"
        print(string.startswith("Olá"))
        print(string.endswith("!"))     
        ```

    === "`find()` e `index()`"

        `find()` retorna a primeira ocorrência de uma substring na string, enquanto `index()` retorna o índice da primeira ocorrência. A diferença é que `index()` gera uma exceção se a substring não for encontrada.

        ```python
        string = "Python é uma linguagem de programação"
        print(string.find("linguagem"))
        print(string.index("linguagem"))
        ```

        === "`count()`"

        Conta o número de ocorrências de uma substring na string.

        Exemplo:
        ```python
        string = "Python é uma linguagem de programação, e Python é incrível!"
        print(string.count("Python"))
        ```


    === "`str.translate(table)`"

        O método `translate()` retorna uma cópia da string original onde cada caractere foi traduzido usando a tabela de tradução fornecida.

        ```python

        tabela = str.maketrans("aeiou", "12345")
        string_original = "Olá, mundo!"
        string_traduzida = string_original.translate(tabela)
        print(string_traduzida)

        ```

        O método `translate()` é útil para realizar operações de tradução em strings de maneira eficiente e rápida. Ele é especialmente útil quando você precisa substituir caracteres por outros em grandes volumes de dados.



## Estruturas Condicionais


As estruturas condicionais na programação visam oferecer ao programador maneiras de tomar decisões dentro de um programa, executando diferentes blocos de código com base em condições específicas. Elas permitem que o fluxo de execução do programa seja alterado de acordo com a avaliação de expressões lógicas, cujo valor poder ser verdadeiro ou falso, a depender do estado da execução.


O comando condicional mais básico em Python é o `if`, que permite verificar se uma condição lógica é verdadeira e então executar um bloco de código associado a ela. 

```python
idade = 18

if idade >= 18:
    print("Idade igual ou superior a 18 anos.")
```

!!! note "Condição lógica"
    Uma condição lógica é uma expressão cujo resultado de sua avaliação será verdadeiro (*True*) ou falso (*False*)


## Todo: parei aqui


Neste exemplo, o código verifica se a variável `idade` é maior ou igual a 18. Se for, ele imprime a mensagem `Idade igual ou superior a 18 anos.`

Além do `if`, Python também oferece o comando `else`, que pode ser utilizado em conjunto com o `if` para executar um bloco de código quando a condição especificada não é verdadeira:

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Neste caso, se a idade for menor que 18, o programa imprime `Você é menor de idade.`

Por vezes, queremos avaliar múltiplas condições. Para isso, utilizamos o comando `elif` (abreviação de `else if`), que permite verificar condições adicionais após a condição inicial `if`. Por exemplo:

```python
idade = 20

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de atingir a maioridade.")
else:
    print("Você é maior de idade.")
```

Neste caso, se a idade for igual a 18, o programa imprime `Você acabou de atingir a maioridade.` Se a idade for maior que 18, ele imprime `Você é maior de idade.` Se nenhuma das condições anteriores for verdadeira, o programa imprime `Você é menor de idade.`

Os comandos condicionais em Python também podem ser aninhados, ou seja, podem conter outros comandos condicionais dentro deles. Isso permite uma lógica mais complexa de decisão em um programa.


Conforme você deve ter observado, o comando `if` avalia uma expressão lógica, cujos únicos valores possíveis são `VERDADEIRO` ou `FALSO`. Expressões nem sempre são tão simples, contendo apenas uma premissa. Tipicamente, temos duas ou mais premissas lógicas compondo as expressões. Neste caso, precisamos dos operadores lógicos para compor a expressão.

## Operadores de comparação

Operadores de comparação são usados para comparar valores e expressões, resultando em valores booleanos (True ou False) que indicam se a comparação é verdadeira ou falsa. Eles são usados para construir condições lógicas em instruções condicionais, loops e em muitas outras partes do código onde a lógica de decisão é necessária.

Python oferece os seguintes operadores de comparação:

1. **== (igual a)**: Verifica se dois valores são iguais. Não confunda com `=`, que indica atribuição.
2. **!= (diferente de)**: Verifica se dois valores são diferentes.
3. **< (menor que)**: Verifica se o valor à esquerda é menor que o valor à direita.
4. **> (maior que)**: Verifica se o valor à esquerda é maior que o valor à direita.
5. **<= (menor ou igual a)**: Verifica se o valor à esquerda é menor ou igual ao valor à direita.
6. **>= (maior ou igual a)**: Verifica se o valor à esquerda é maior ou igual ao valor à direita.

Exemplos:

```python
a = 5
b = 10

# Igual a
print(a == b)  # False

# Diferente de
print(a != b)  # True

# Menor que
print(a < b)   # True

# Maior que
print(a > b)   # False

# Menor ou igual a
print(a <= b)  # True

# Maior ou igual a
print(a >= b)  # False
```

Esses operadores são frequentemente usados em instruções condicionais (como `if`, `elif`, `else`), onde o fluxo do programa depende do resultado das comparações.

Também é importante mencionar que os operadores de comparação podem ser combinados com operadores lógicos (`and`, `or`, `not`) para criar condições mais complexas. Isso permite construir lógicas de decisão mais elaboradas em um programa.


## Operadores lógicos


Operadores lógicos são elementos fundamentais em linguagens de programação que permitem combinar e avaliar condições booleanas. Eles são essenciais para controlar o fluxo de execução de um programa com base em diversas situações e critérios.

Em Python, existem três operadores lógicos principais: `and`, `or` e `not`. Cada um deles desempenha um papel específico na avaliação e combinação de expressões booleanas.

### **Operador `and`**: 

Este operador retorna `True` se ambas as expressões que ele conecta forem verdadeiras e `False` caso contrário. Ele é frequentemente utilizado para verificar se múltiplas condições devem ser atendidas para que uma determinada ação seja tomada. Por exemplo:

```python
idade = 25
if idade >= 18 and idade <= 30:
    print("Você é um adulto jovem.")
```

Neste exemplo, a mensagem será impressa apenas se a idade estiver entre 18 e 30 anos.


!!! info "Tabela Verdade para o Operador `and` (e)"

        | A     | B     | A and B |
        | ----- | ----- | ------- |
        | True  | True  | True    |
        | True  | False | False   |
        | False | True  | False   |
        | False | False | False   |



### **Operador `or`**: 

Este operador retorna `True` se pelo menos uma das expressões que ele conecta for verdadeira e `False` apenas se ambas as expressões forem falsas. Ele é útil quando pelo menos uma de várias condições precisa ser verdadeira para que uma ação seja executada. Por exemplo:

```python
sexo = "feminino"
if sexo == "feminino" or sexo == "masculino":
    print("Sexo válido.")
```

!!! info "Tabela Verdade para o Operador `or` (ou)"
        | A     | B     | A or B |
        | ----- | ----- | ------ |
        | True  | True  | True   |
        | True  | False | True   |
        | False | True  | True   |
        | False | False | False  |



Neste caso, a mensagem será impressa se o valor da variável `sexo` for `feminino` ou `masculino`.

### **Operador `not`**: 


Este operador é utilizado para inverter o valor de uma expressão booleana. Se a expressão original for True, o `not` a transformará em False, e vice-versa. Ele é frequentemente utilizado para verificar se uma condição não é verdadeira. Por exemplo:

```python
idade = 15
if not idade >= 18:
    print("Você é menor de idade.")
```

Neste exemplo, a mensagem será impressa apenas se a idade não for maior ou igual a 18.


!!! info "Tabela Verdade para o Operador `not` (negação)"
    | A     | not A |
    | ----- | ----- |
    | True  | False |
    | False | True  |



## Match

O comando [`match`](https://docs.python.org/3/tutorial/controlflow.html#match-statements) foi introduzido no Python a partir da versão 3.10 e oferece uma nova forma de realizar múltiplas comparações de padrões de forma mais legível e concisa do que as estruturas condicionais tradicionais.

Ele é especialmente útil quando se tem múltiplas condições a serem verificadas e quando cada condição envolve uma expressão de padrão específica. O `match` funciona de maneira semelhante ao `switch` em outras linguagens de programação.

Vamos ver um exemplo de como o `match` pode ser usado:

```python
def dia_da_semana(numero):
    match numero:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Número inválido")
```

Neste exemplo, a função `dia_da_semana` recebe um número e utiliza o comando `match` para verificar qual dia da semana corresponde a esse número. Se o número corresponder a um dos casos especificados (de 1 a 7), o programa imprime o nome do dia correspondente. Caso contrário, imprime `Número inválido`.

O `match` permite a combinação de padrões mais complexos usando a sintaxe `case <padrão> if <condição>:`, onde `<padrão>` é um padrão a ser verificado e `<condição>` é uma expressão booleana que também deve ser verdadeira para que a correspondência seja feita.

```python

match valor:
    case valor if valor>0 and valor%2==0:
        print("PAR e POSITIVO")
    case valor if valor>0 and valor%2!=0:
        print("ÍMPAR e POSITIVO")
    case valor if valor<0 and valor%2==0:
        print("PAR e NEGATIVO")
    case valor if valor<0 and valor%2!=0:
        print("ÍMPAR e NEGATIVO")
    case _:
        print("ZERO")
 
``` 
Também podemos testar vários valores em cada caso utilizando o operador `|`. Veja o exemplo.

```python

match codigo:
    case 0 | -1:
        print("Valor 0 ou -1")
    case 1 | 2 | 3:
        print("Valor 1, 2, ou 3.")
    case _:
        print("Algum outro valor")

```

 

Saiba mais em [PEP 636](https://peps.python.org/pep-0636/) e [Oficial Reference](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement).




Laços de repetição são estruturas de controle que permitem criar iterações, ou seja, repetição de instruções. No Python, as principais estruturas são o `for` e o `while`. Abaixo, seguem detalhes e exemplos destes dois laços de repetição

### Laço `for`:

O laço `for` em Python é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outro objeto iterável. Ele executa um bloco de código para cada item da sequência, logo seu uso é destinado justamente para situações em que conhecemos de antemão a quantidade de ciclos (iterações) necessárias.



```python
# Lista de valores
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# Caracteres de uma string
palavra = "Python"
for letra in palavra:
    print(letra)

# Dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave, valor in dicionario.items():
    print(chave, valor)

# Intervalo de valores
for i in range(1, 6):  
    print(i)

```

### Laço `while`:

Já o laço `while`, por sua vez, é usado para repetir um bloco de código enquanto uma condição especificada for verdadeira.


```python
# Imprimindo números de 1 a 5 usando while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Pedindo entrada ao usuário até que ele insira "sair"
while True:
    entrada = input("Digite algo (ou 'sair' para sair): ")
    if entrada == 'sair':
        break  # Sai do laço
    print("Você digitou:", entrada)
```

Utilizamos `while` comumente em situações onde o número de iterações não é conhecido de antemão. 



### Comandos `break`, `continue` e `else`


O comando `continue` é utilizado para interromper a iteração atual de um loop e passar para a próxima iteração, ignorando o restante do código que segue.  No código que segue, quando `i` tiver valor igual a `3`, o comando `print(i)` não será executado. Isso porque, executar a instrução `continue`, o interpretador irá retornar para o início do laço, iniciando a próxima iteração.


```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```


Já o comando `break` é utilizado para interromper completamente a execução de um loop. Quando o break é encontrado dentro de um loop, o controle do programa é transferido para a instrução imediatamente após o bloco de loop. Em nosso exemplo, quando `i` tiver o valor `3`, o laço é interrompido e o interpretador segue com o próximo comando após o `for`, que no caso é `x = 10`.

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
x = 10
```

Tanto `for` quanto `while` podem conter um bloco `else` em sua definição. O uso assemelha-se ao `else` da construção `try except`. No caso dos laços, o bloco `else` será executado sempre que o laço concluir suas iterações normalmente, ou seja, sem o uso de `break`.




### Função `range`

A função `range()` gera uma sequência de números inteiros em um intervalo especificado. Esta função é comumente utilizada em laços (loops), como `for`, para iterar sobre uma sequência de números.

A sintaxe básica da função `range()` é a seguinte:

```
range(start, stop, step)
```

Onde:

- `start`: O valor inicial da sequência (opcional). Se não especificado, o padrão é 0.
  
- `stop`: O valor final da sequência (obrigatório). A sequência gerada não inclui este valor.
  
- `step`: O incremento entre os números na sequência (opcional). Se não especificado, o padrão é 1.


Veja um exemplo que utiliza a função `range()` com seus três argumentos (`start`, `stop`, e `step`) preenchidos.

```python
for i in range(1, 10, 2):
    print(i)
```
 

 

Uma função é um bloco de código reutilizável que realiza uma tarefa específica, geralmente encapsulando um conjunto de instruções para evitar a repetição de código e para modularizar um programa. O conceito de função é fundamental na programação, facilitando a escrita, a leitura, a manutenção e a reutilização do código. Além disso, utilizar funções melhora a testabilidade do código, que uma propriedade muito importante em termos de qualidade.

 
Toda função deve ser **declarada** para então ser utilizada em outras partes do código. A declaração da função compreende definir seu nome, uma lista de parâmetros opcionais e um corpo que contém as instruções a serem executadas. Em Python, isso é feito usando a palavra-chave `def`.

```python
def minha_funcao(param1, param2):        
    return param1 + param2
```

Uma vez definida, a função pode ser chamada ou invocada em qualquer parte do programa, passando os argumentos necessários, quando estes tiverem sido definidos.

```python
    resultado = minha_funcao(10, 5)
    print(resultado) 
```

Vamos detalhar cada um dos componentes da declaração e invocação de uma função na sequência:

- **Nome da função**: identificador único que diferencia uma função das outras. Segue as regras de nomenclatura de variáveis na linguagem de programação. 
- **Parâmetros**: variáveis listadas na definição da função, que recebem os valores dos argumentos passados durante a chamada da função. São valores que a função irá receber do mundo externo e são utilizados para torná-la genérica em propósito de uso. Lembre que parâmetros são opcionais.
- **Argumentos**: nome formal dado aos valores passados para os respectivos parâmetros da função quando ela é chamada.
- **Corpo da função**: corresponde ao bloco de código que define as operações realizadas pela função. Esse bloco é executado quando a função é chamada. É sua implementação.
- **Valor de retorno**: O resultado que a função devolve ao ponto onde foi chamada, usando a palavra-chave `return`. Uma função pode não retornar nenhum valor. Neste caso, em Python, o valor `None` é implicitamente retornado. Outras linguagens chamam de `void`.


### Funções com número de argumentos variáveis

Há casos específicos onde é conveniente permitir que uma função possa receber uma quantidade indeterminada de argumentos. Para este fim, a linguagem Python oferece dois recursos distintos: usando `*args` para argumentos posicionais variáveis e `**kwargs` para argumentos nomeados variáveis.

#### Argumentos Posicionais Variáveis (`*args`)

Quando não sabemos de antemão quantos argumentos serão passados para uma função, é possível usar `*args` na definição da função. `*args` permite que a função receba um número arbitrário de argumentos posicionais, que são recebidos internamente como uma tupla.

```python
def soma(*args):
    return sum(args)

print(soma(1, 2, 3))        
print(soma(10, 20, 30, 40)) 
```

#### Argumentos Nomeados Variáveis (`**kwargs`)

Para o case de uma quantidade variável de argumentos nomeados, utilizamos `**kwargs`. `**kwargs` permite que a função receba um número arbitrário de argumentos nomeados, que são recebidos internamente como um dicionário.

 

```python
def imprimir_dados(**kwargs):     
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_dados(nome="Alice", idade=30, cidade="São Paulo")
```
 

#### Combinação de `*args` e `**kwargs`

É possível combinar `*args` e `**kwargs` na mesma função para aceitar uma quantidade variável de argumentos posicionais e nomeados. Quando usados juntos, `*args` deve vir antes de `**kwargs` na definição da função.

 

```python
def misturar_argumentos(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)
misturar_argumentos(1, 2, 3, 4, 5, x=10, y=20)
```


### Escopo e Ciclo de Vida de Variáveis

Quando trabalhamos com funções, assim como ocorre com outros comandos de bloco, devemos estar cientes do escopo de visibilidade das variáveis e de seu ciclo de vida. O escopo de uma variável refere-se ao contexto dentro do qual essa variável é reconhecida e pode ser utilizada na programação.



No **escopo local**, variáveis ali definidas existem somente naquele contexto, não sendo acessíveis fora dele. É o caso de variáveis criadas dentro de funções. Sua existência se restringe ao corpo da função.

   ```python
   def minha_funcao():
       x = 10  # X só existe no contexto desta função
       print(x)
   ```

Estão no **escopo global**, por sua vez, variáveis definidas fora de qualquer função. Estas são acessíveis em qualquer parte do programa. Sempre que possível, o escopo global deve ser evitado.

   ```python
   x = 10  # Esta variável vale para todo o programa
   def minha_funcao():
       print(x)
   ```

 
Para certas situações, é necessário utilizar as palavras reservadas [`global`](https://www.w3schools.com/python/ref_keyword_global.asp) e [`nonlocal`](https://www.w3schools.com/python/ref_keyword_nonlocal.asp) para resolver questões associadas com escopo de variáveis no Python.



O `try`, `except`, `finally` é uma estrutura em Python que permite lidar com exceções de forma controlada e garantir que determinadas ações sejam executadas independentemente de ocorrer uma exceção ou não.

### Sintaxe:

A estrutura básica é composta por três blocos:

```python
try:
    # Código que pode gerar exceções
    # Se ocorrer uma exceção, o controle será transferido para o bloco except correspondente
except Excecao_Tipo_1:
    # Bloco executado se ocorrer uma exceção do tipo ExcecaoTipo1
except Excecao_Tipo_2:
    # Bloco executado se ocorrer uma exceção do tipo ExcecaoTipo2
else:
    # Bloco opcional executado se nenhuma exceção ocorrer no bloco try
finally:
    # Bloco opcional executado sempre, independentemente de ocorrer uma exceção ou não
```

- `try`: Este bloco contém o código que pode gerar exceções.
  
- `except`: Este bloco captura exceções específicas que podem ocorrer dentro do bloco `try`. É possível ter vários blocos `except` para diferentes tipos de exceções.

- `else`: É opcional e executado apenas se nenhuma exceção ocorrer dentro do bloco `try`. É útil para código que deve ser executado apenas se não houver exceções.

- `finally`: O bloco `finally` é sempre executado, independentemente de ocorrer uma exceção ou não dentro do bloco `try`. É usado para garantir que determinadas ações, como a liberação de recursos, sejam executadas, mesmo em caso de exceção.

### Exemplo de Uso:

```python
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
else:
    print("O arquivo foi lido com sucesso.")
finally:
    arquivo.close()  # Garante que o arquivo seja fechado, mesmo se ocorrer uma exceção
```

Neste exemplo:

- O bloco `try` tenta abrir e ler um arquivo.
  
- Se o arquivo não for encontrado, uma exceção `FileNotFoundError` será levantada e o bloco `except` correspondente será executado, exibindo uma mensagem apropriada.

- Se o arquivo for lido com sucesso, o bloco `else` será executado, indicando que o arquivo foi lido sem problemas.

- O bloco `finally` garante que o arquivo seja fechado, independentemente de ter sido lido com sucesso ou não.

### Utilizações Comuns:

- **Manipulação de Arquivos:** Usado para abrir, ler e fechar arquivos de forma segura, garantindo que os recursos sejam liberados adequadamente.

- **Conexões de Rede e Banco de Dados:** É comum usar `try`, `except`, `finally` ao lidar com operações de rede ou banco de dados para garantir a limpeza adequada de recursos, como fechar conexões.

- **Validação de Entrada de Usuário:** Pode ser usado para validar entrada de usuário e lidar com erros de entrada de forma elegante.


A lista de exceções nativas do Python pode ser encontrada na [documentação oficial](https://docs.python.org/3/library/exceptions.html).





## Listas

As listas são uma estrutura de dados versátil que permite armazenar coleções de itens em uma **ordem específica**. São **mutáveis**, o que significa que você pode adicionar, remover e modificar itens conforme necessário sem gerar uma cópia do objeto. Normalmente, as listas são utilizadas para armazenar dados de forma homogenea, ou seja, com todos os items apresentando mesmo tipo, embora não haja restrição quanto a isso.

Para criar uma lista em Python, utilizamos colchetes `[]` e separamos os itens com vírgulas. Por exemplo:

```python
minha_lista = [1, 2, 3, 4, 5]
```
Outra possibilidade é criar uma lista vazia e ir adicionando itens a mesma através do método `append`.

```python
outra_lista = []
outra_lista.append(10)
outra_lista.append(20)
```


Para acessarmos os elementos, utilizandos colchetes `[]`, com o índice do elemento desejado. Lembre-se de que os índices em Python começam em 0. Lembre-se também que podemos utilizar aqui as operações de slicing já vistas. Por exemplo:

```python
print(minha_lista[0]) 
print(minha_lista[2])
```

Para modificar um elemento, atribuímos um novo valor ao respectivo índice:

```python
minha_lista[0] = 100
print(minha_lista)  
```

### Principais operações e funções

As principais operações que podem ser realizadas com listas são:

- Adição de elementos: `append()`, `insert()`
- Remoção de elementos: `remove()`, `pop()`
- Ordenação: `sort()`
- Reversão: `reverse()`
- Concatenação: `+`

Já em termos de funções,  relacionam-se às listas as funções:

- `len()`: Retorna o número de elementos em uma lista.
- `sum()`: Retorna a soma de todos os elementos em uma lista.
- `max()`: Retorna o elemento máximo em uma lista.
- `min()`: Retorna o elemento mínimo em uma lista.



### Iteração de elementos

Para iterar sobre os elementos de uma lista, podemos utilizar o laço `for`. Por exemplo:

```python
for item in minha_lista:
    print(item)
```

### List Comprehension

List Comprehension é uma maneira concisa e elegante de criar listas em Python. Ela permite criar listas de forma mais eficiente e legível, muitas vezes em uma única linha de código.

A sintaxe utilizada é apresentada na sequência. Observe que `expressão` define cada elemento da nova lista, enquanto `item` corresponde ao elemento presente em `iterável` do atual ciclo de iteração.

```python
[expressão for item in iterável]
```

Vejamos alguns exemplos concretos:

1. Criando uma lista de números ao quadrado:

```python
quadrados = [x ** 2 for x in range(1, 6)]
```

2. Filtrando uma lista para conter apenas números pares:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
```

3. Criando uma lista de tuplas com valores invertidos:

```python
tuplas = [(x, y) for x in range(1, 4) for y in range(1, 4)]
```


## Tuplas


 

Uma tupla é uma estrutura de dados semelhante a uma lista, mas com a diferença crucial de que ela é imutável, o que significa que uma vez que uma tupla é criada, seus elementos não podem ser alterados. As tuplas são definidas utilizando parênteses `()`.

Tuplas são utilizadas para agregar dados diversos, mantendo-os imutáveis e dispostos de uma determinada ordem.


```python
minha_tupla = (1, 2, 3, 4, 5)
tupla_vazia = ()
```
 
Se houver apenas um elemento na tupla, é necessário incluir uma vírgula após o elemento para diferenciá-lo de uma expressão entre parênteses. Por exemplo:

```python
tupla_com_um_elemento = (10,)
```

### Acessando Elementos

Para acessar os elementos de uma tupla utilizando índices, da mesma forma que faria com uma lista:

```python
print(minha_tupla[0])  # Saída: 1
print(minha_tupla[2])  # Saída: 3
```

Lembre-se que as tuplas são imutáveis. Isso significa que uma vez que uma tupla é criada, você não pode adicionar, remover ou modificar elementos.  




Claro! Aqui está uma documentação detalhada sobre dicionários em Python:

---

## Dicionários 

Um dicionário em Python é uma estrutura de dados que armazena pares chave-valor. Ele é uma das estruturas de dados mais utilizadas devido à sua eficiência e flexibilidade. Os dicionários são mutáveis, o que significa que você pode adicionar, modificar e remover itens conforme necessário. Cada chave em um dicionário deve ser única e associada a um único valor. As chaves podem ser de qualquer tipo imutável, como strings, números e tuplas.



Para criar um dicionário, devemos utilizar a sintaxe de chaves `{}` e especificar os pares chave-valor separados por vírgulas. Por exemplo:

```python
meu_dicionario = {"nome": "Alice", "idade": 30, "cidade": "Nova York"}
```

Também é possível criar um dicionário vazio e adicionar itens posteriormente:

```python
outro_dicionario = {}
outro_dicionario["marca"] = "Toyota"
outro_dicionario["modelo"] = "Corolla"
```

O acesso aos valores de um dicionário se dá por meio das chaves correspondentes. Por exemplo:

```python
print(meu_dicionario["nome"])
print(meu_dicionario["idade"])
```

Se a chave não existir no dicionário, será lançada uma exceção `KeyError`. Para evitar isso, podemos utilizar usar o método `get()`:

```python
print(meu_dicionario.get("cidade", "Não encontrado"))  # Saída: Nova York
print(meu_dicionario.get("profissão", "Não encontrado"))  # Saída: Não encontrado
```

Para remover um par chave-valor, utilizamos o comando `del`:

```python
del meu_dicionario["idade"]
```

### Métodos Úteis

- `keys()`: Retorna uma lista contendo todas as chaves do dicionário.
- `values()`: Retorna uma lista contendo todos os valores do dicionário.
- `items()`: Retorna uma lista de tuplas contendo todos os pares chave-valor do dicionário.
- `update()`: Atualiza o dicionário com os pares chave-valor de outro dicionário ou de uma sequência de pares chave-valor.



## Conjuntos

Um conjunto é uma estrutura de dados que armazena elementos únicos e não ordenados. Os conjuntos são muito úteis para realizar operações de conjunto oriundos da Matemática, como união, interseção, diferença e teste de pertencimento. Os conjuntos são mutáveis, assim como listas e dicionários.

### Criando um Conjunto

Para criar um conjunto utilizamos a função `set()` ou a sintaxe de chaves `{}`. Por exemplo:

```python
meu_conjunto = {1, 2, 3, 4, 5}
```
Já para criar um conjunto vazio, a única opção é usar `set()`:

```python
conjunto_vazio = set()
```

### Adicionar e Remover Elementos

Para adicionar elementos, utilizamos o método `add()`:

```python
meu_conjunto.add(6)
```

Para remover um elemento, temos os métodos `remove()` ou `discard()`. A diferença é que `remove()` gera um erro se o elemento não estiver presente no conjunto, enquanto `discard()` não gera nenhum erro:

```python
meu_conjunto.remove(5)
meu_conjunto.discard(2)
```

### Operações de Conjunto

Tal qual ocorre na Matemática, o uso de conjuntos no Python oferece suporte às mesmas operações. Para fins didáticos, vamos utilizar como exemplo dois conjuntos de números inteiros, identificados pelas variáveis `conjunto_a` e `conjunto_b`. Tais conjuntos contém os seguintes valores:

```python
conjunto_a = {1, 3, 5, 7, 9}
conjunto_b = {2, 4, 6, 8, 10}

print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)
```

Agora, vamos às operações:

- `union()`, `|`: Retorna um novo conjunto com todos os elementos de ambos os conjuntos.

```python
conjunto_uniao = conjunto_a | conjunto_b
print("Conjunto União:", conjunto_uniao)
```

- `intersection()`, `&`: Retorna o que há de comum entre ambos os conjuntos.

```python
conjunto_inserseccao = conjunto_a & conjunto_b
print("Conjunto Intersecção:", conjunto_inserseccao)
```

- `difference()`, `-`: Retorna um novo conjunto com os elementos presentes no primeiro conjunto que não estão no segundo.

```python
conjunto_diferenca = conjunto_a - conjunto_b
print("Conjunto Diferença:", conjunto_diferenca)
```

- `symmetric_difference()`, `^`: Retorna um novo conjunto contendo os elementos que estão em apenas um dos conjuntos, nunca em ambos.
  
```python
conjunto_diferenca = conjunto_a ^ conjunto_b
print("Conjunto Diferença:", conjunto_diferenca)
```

- `issuperset()`, `>=`: Verifica se um conjunto é **superconjunto** de outro. Para ser superconjunto, é necessário ter todos os elementos do outro conjunto avaliado, sendo possível ter elementos adicionais.

```python
conjunto_a >= conjunto_b
```

- `issubset()`, `<=`: Verifica se um conjunto é **subconjunto** de outro. Para ser subconjunto é preciso que todos os elementos do conjunto estejam contidos no outro avaliado.

```python
conjunto_a <= conjunto_b
```


### Iterando sobre um Conjunto

Assim como listas, podemos iterar conjuntos utilizando um loop `for`:

```python
for elemento in meu_conjunto:
    print(elemento)
```




## Slicing

*Slicing* é uma técnica que permite extrair partes específicas de uma string, criando subtrings com base em índices específicos. O operador de slicing é de grande valia para manipulação de strings de maneira eficiente e flexível no Python.

### Sintaxe:

A sintaxe básica para slicing em Python é:

```
string[início:fim:passo]
```

- `início`: Índice onde o slicing começa. Se não especificado, é considerado o início da string.
- `fim`: Índice onde o slicing termina. Este índice não é incluído na substring resultante. Se não especificado, é considerado o final da string.
- `passo`: Opcional. Define o intervalo entre os caracteres a serem considerados durante o slicing. Se não especificado, o padrão é 1.

### Exemplos de Uso:

1. **Extraindo Substrings:**

   ```python
   s = "Python"
   print(s[2:5])  # Saída: thon
   ```

2. **Invertendo uma String:**

   ```python
   s = "Python"
   print(s[::-1])  # Saída: nohtyP
   ```

3. **Extraindo Partes com Intervalos Específicos:**

   ```python
   s = "Python Programming"
   print(s[0:10:2])  # Saída: Pto rg
   ```

4. **Obtendo Todos os Caracteres a Partir de um Índice Específico:**

   ```python
   s = "Python"
   print(s[3:])  # Saída: hon
   ```
 

 

Em Python, assim como em praticamente todas as linguagens de programação, os comandos condicionais desempenham um papel fundamental na execução de um código de forma controlada e adaptável. Eles permitem que um programa tome decisões com base em condições específicas, direcionando o fluxo de execução do código de acordo com o resultado dessas condições.

