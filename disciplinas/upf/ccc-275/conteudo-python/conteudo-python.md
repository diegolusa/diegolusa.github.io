---
title: "Fundamentos de algoritmos e programação com Python"
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

## Variáveis e constantes

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



## Tipos de dados

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



## Entradas e saídas

Para receber entrada do usuário, Python oferece a função `input()`. O valor retornado após executar a função foi o que o usuário digitou no terminal. Aqui estamos falando de entrada em terminal, ou seja, sem uso de interface gráfica.

No trecho de código que segue, a mensagem `Digite seu nome: ` é impressa na tela e o cursor fica aguardando a entrada do usuário. Após o usuário digitar os dados e pressionar ENTER, o valor é armazenado na variável `nome`.

```python
nome = input("Digite seu nome: ")
```

Já para exibir informações para o usuário, podemos usar a função `print()`, conforme o exemplo a seguir. No código em questão, será impresso na tela a mensagem `Olá, ` acompanhada do valor da variável `nome`.

```python
print("Olá,", nome)
```

## Operadores aritméticos

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



## Conversões de dados

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



## Estruturas condicionais


As estruturas condicionais na programação visam oferecer ao programador maneiras de tomar decisões dentro de um programa, executando diferentes blocos de código com base em condições específicas. Elas permitem que o fluxo de execução do programa seja alterado de acordo com a avaliação de expressões lógicas, cujo valor poder ser verdadeiro ou falso, a depender do estado da execução.


O comando condicional mais básico em Python é o `if`, que permite verificar se uma condição lógica é verdadeira e então executar um bloco de código associado a ela. 

```python
idade = 18

if idade >= 18:
    print("Idade igual ou superior a 18 anos.")
```
No exemplo, o código verifica se a variável `idade` é maior ou igual a `18`. Se for, imprime a mensagem `Idade igual ou superior a 18 anos.`

!!! note "Condição lógica"
    Uma condição lógica é uma expressão cujo resultado de sua avaliação será verdadeiro (*True*) ou falso (*False*). Utilizam-se operadores de comparação e operadores lógicos na composição das expressões.


Ao utilizar o comando o `if`, temos a disposição o `else`, utilizado para executar um bloco de código quando a condição especificada NÃO é verdadeira. Observe no caso abaixo que a saída `Você é menor de idade.` deve ser apresentada caso o teste lógico resulte em falso.

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```


Há casos em que temos a necessidade de múltiplas condições. Para isso, utilizamos o comando `elif` (abreviação de `else if`), que permite verificar condições adicionais após a condição inicial `if`. Tal construção permite a criação de uma cadeia de testes para avaliar várias condições em uma única instrução.

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

Os comandos condicionais em Python também podem ser aninhados, ou seja, podem conter outros comandos condicionais dentro deles. Isso permite uma lógica mais complexa de decisão. Contudo, não é boa prática aplicar vários níveis de aninhamento, pois isso aumenta a complexidade e reduz a legibilidade do código.


Conforme você deve ter observado, o comando `if` avalia uma expressão lógica, cujos únicos valores possíveis são `VERDADEIRO` ou `FALSO`. Expressões nem sempre são simples, contendo apenas uma premissa. Tipicamente, temos duas ou mais premissas lógicas compondo as expressões. Neste caso, precisamos dos operadores lógicos para unir as partes.

### Operadores de comparação

Operadores de comparação são usados para comparar valores e expressões, resultando em valores *booleanos* (True ou False) que indicam se a comparação é verdadeira ou falsa. Eles são usados para construir condições lógicas em instruções condicionais, loops e em muitas outras partes do código onde a lógica de decisão é necessária.

!!! info "Operadores de Comparação"
    === "Igualdade" 
        O operador **== (igual a)** verifica se dois valores são iguais. Não confunda com `=`, que indica atribuição.
        ```python
            a = 5
            b = 10
            print(a == b)
        ```

    === "Diferença"
        O operador **!= (diferente de)** verifica se dois valores são diferentes.
        ```python
            a = 5
            b = 10
            print(a != b)
        ```
    === "Menor que" 
        O operador **< (menor que)** verifica se o valor à esquerda é menor que o valor à direita.
        ```python
            a = 5
            b = 10
            print(a < b)
        ```
    === "Maior que"
        O operador **> (maior que)** verifica se o valor à esquerda é maior que o valor à direita.
        ```python
            a = 5
            b = 10
            print(a > b)
        ```
    === "Menor ou igual a"
        O operador **<= (menor ou igual a)** verifica se o valor à esquerda é menor ou igual ao valor à direita.
        ```python
            a = 5
            b = 10
            print(a <= b)
        ```
    === "Maior ou igual a"
        O operador **>= (maior ou igual a)** verifica se o valor à esquerda é maior ou igual ao valor à direita.
        ```python
            a = 5
            b = 10
            print(a >= b)
        ```


Esses operadores são frequentemente usados em instruções condicionais (como `if`, `elif`, `else`), onde o fluxo do programa depende do resultado das comparações.

Também é importante mencionar que os operadores de comparação podem ser combinados com operadores lógicos (`and`, `or`, `not`) para criar condições mais complexas. Isso permite construir lógicas de decisão mais elaboradas em um programa.


### Operadores lógicos


Operadores lógicos são elementos fundamentais em linguagens de programação que permitem combinar e avaliar condições booleanas. Eles são essenciais para controlar o fluxo de execução de um programa com base em diversas situações e critérios.

Em Python, existem três operadores lógicos principais: `and`, `or` e `not`. Cada um deles desempenha um papel específico na avaliação e combinação de expressões booleanas.


!!! note "Operadores Lógicos"

    === "**Operador `and`**"

        Este operador retorna `True` se ambas as expressões que ele conecta forem verdadeiras e `False` caso contrário. Ele é frequentemente utilizado para verificar se múltiplas condições devem ser atendidas para que uma determinada ação seja tomada. Por exemplo:

        ```python
        idade = 25
        if idade >= 18 and idade <= 30:
            print("Você é um adulto jovem.")
        ```

        A tabela verdade do operador `and` é:

        | A     | B     | A and B |
        | ----- | ----- | ------- |
        | True  | True  | True    |
        | True  | False | False   |
        | False | True  | False   |
        | False | False | False   |



    === "**Operador `or`**"

        Este operador retorna `True` se pelo menos uma das expressões que ele conecta for verdadeira e `False` apenas se ambas as expressões forem falsas. Ele é útil quando pelo menos uma de várias condições precisa ser verdadeira para que uma ação seja executada. Por exemplo:

        ```python
        peso = 200
        if peso >=190 or peso <= 210:
            print("Peso válido.")
        ```

         A tabela verdade do operador `or` é:

        | A     | B     | A or B |
        | ----- | ----- | ------ |
        | True  | True  | True   |
        | True  | False | True   |
        | False | True  | True   |
        | False | False | False  |




    === "**Operador `not`**"

        Este operador é utilizado para inverter o valor de uma expressão booleana. Se a expressão original for True, o `not` a transformará em False, e vice-versa. Ele é frequentemente utilizado para verificar se uma condição não é verdadeira. Por exemplo:

        ```python
        idade = 15
        if not idade >= 18:
            print("Você é menor de idade.")
        ```

        A tabela verdade para o operador `not` (negação) é muito simples, pois compreende o oposto do valor lógico recebido. Observe:

        | A     | not A |
        | ----- | ----- |
        | True  | False |
        | False | True  |



### Match

O comando [`match`](https://docs.python.org/3/tutorial/controlflow.html#match-statements) foi introduzido no Python a partir da versão 3.10 e oferece uma nova forma de realizar múltiplas comparações de padrões de forma mais legível e concisa do que as estruturas condicionais tradicionais.

Ele é especialmente útil quando se tem múltiplas condições a serem verificadas e quando cada condição envolve uma expressão de padrão específica. O `match` funciona de maneira semelhante ao `switch` em outras linguagens de programação. Observe o exemplo:

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
Também podemos testar vários valores em cada caso utilizando o operador `|`. Isso por vezes é necessário quando o mesmo tratamento deve ser aplicado a mais de um valor da variável em avaliação.

```python

match codigo:
    case 0 | -1:
        print("Valor 0 ou -1")
    case 1 | 2 | 3:
        print("Valor 1, 2, ou 3.")
    case _:
        print("Algum outro valor")

```

Você irá encontrar mais detalhes em [PEP 636](https://peps.python.org/pep-0636/) e [Oficial Reference](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement).


## Estruturas de repetição

Laços de repetição são estruturas de controle que permitem criar iterações, ou seja, repetição de uma ou mais intruções. No Python, as principais estruturas são o `for` e o `while`. Abaixo, seguem detalhes e exemplos destes dois laços de repetição

### Laço `for`

O laço `for` é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outro objeto iterável qualquer. Ele executa um bloco de código para cada item da sequência. Seu uso é destinado justamente para situações em que conhecemos de antemão a quantidade de ciclos (iterações) necessárias.



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

### Laço `while`

O laço `while` serve ao mesmo propósito do `for`: repetir instruções. Contudo, é usado especialmente para repetir um bloco de código enquanto uma condição especificada for verdadeira. Em boa parte dos casos, a quantidade de iterações não pode ser determinada com exatidão antecipadamente.


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



### Comandos `break`, `continue` e `else`


O comando `continue` é utilizado para interromper a iteração atual de um loop e passar para a próxima iteração, ignorando o restante do código que segue até o final do bloco.  No código abaixo, quando `i` tiver valor igual a `3`, o comando `print(i)` não será executado. Isso porque, executar a instrução `continue`, o interpretador irá retornar para o início do laço, iniciando uma próxima iteração sem considerar as instruções que estão na sequência.


```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```


O comando `break` é utilizado para interromper completamente a execução de laço de repetição. Quando o `break` é encontrado dentro de um laço, o controle do programa é transferido para a instrução imediatamente após o bloco. Em nosso exemplo apresentado abaixo, quando `i` alcançar o valor `3`, o laço será interrompido e o interpretador seguirá com o próximo comando após o bloco `for` () (no caso é `x = 10`).

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
x = 10
```

Tanto o laço `for` quanto `while` podem conter um bloco `else` em sua definição. O uso assemelha-se ao `else` da construção `try except`. No caso dos laços, o bloco `else` será executado sempre que o laço concluir suas iterações normalmente, ou seja, sem o uso de `break` internamente.




### Função `range`

A função `range()` gera uma sequência de números inteiros em um intervalo especificado. Esta função é comumente utilizada conjuntamente com o laço `for` para iterar sobre uma sequência de números. O uso da função `range()` é simples, pois compreende informar apenas o valor final da sequência. Há também opções para modificar o valor de início e o incremento. 

Considerando que a assinatura da função é `range(start, stop, step)`, temos que:


- `start`: O valor inicial da sequência (opcional). Se não especificado, o padrão é 0.
- `stop`: O valor final da sequência (obrigatório). A sequência gerada não inclui este valor.
- `step`: O incremento entre os números na sequência (opcional). Se não especificado, o padrão é 1.


Observe um exemplo que utiliza a função `range()` com três argumentos.

```python
for i in range(1, 10, 2):
    print(i)
```


## Funções

 

Uma função é um bloco de código reutilizável que realiza uma tarefa específica, geralmente encapsulando um conjunto de instruções para evitar a repetição de código e modularizar um programa. O conceito de função é fundamental na programação, pois facilita a escrita, leitura, manutenção ea reutilização do código ao longo do tempo. Além disso, utilizar funções melhora a testabilidade do código, uma propriedade muito importante para processos que buscam garantir a qualidade do código produzido.

 
Toda função deve ser **declarada** para então ser utilizada em outras partes do código. A declaração da função compreende definir seu nome, uma lista de parâmetros (ou deixar em branco) e um corpo que contém as instruções a serem executadas. Em Python, isso é feito usando a palavra reservada `def`.

Os parâmetros funcionam como variáveis locais, tendo visibilidade apenas no escopo das instruções que pertencem ao bloco da função. Definimos parâmetros sempre que precisamos receber do contexto externo à função valores necessários ao seu processamento. Isso oferece maior amplitude de uso da função, tornando-a mais genérica (e este é o objetivo!).

Funções também podem retornar valores a quem as chamou. A palavra reservada `return` aplicada nestes casos. Nossa funcão de exemplo utiliza tal recurso, pois retorna a soma dos valores informados por parâmetro.


```python
def minha_funcao(param1, param2):        
    return param1 + param2
```

Uma vez definida, a função pode ser chamada (invocada) em qualquer parte do programa, passando os argumentos necessários, quando estes tiverem sido definidos.

```python
    resultado = minha_funcao(10, 5)
    print(resultado) 
```


!!! info "Quais são os componentes de uma funcão"

    === "**Nome da função**" 
        Identificador único que diferencia uma função das outras. Segue as regras de nomenclatura de variáveis na linguagem de programação. 
    === "**Parâmetros**" 
        Variáveis listadas na definição da função, que recebem os valores dos argumentos passados durante a chamada da função. São valores que a função irá receber do mundo externo e são utilizados para torná-la genérica em propósito de uso. Lembre-se que parâmetros são opcionais, assim como podem ser definidos com valores padrão.
    === "**Argumentos**" 
        Nome formal dado aos valores passados para os respectivos parâmetros da função quando ela é chamada.
    === "**Corpo da função**"
        Corresponde ao bloco de código que define as operações realizadas pela função. Esse bloco é executado quando a função é chamada. É sua implementação.
    === "**Valor de retorno**"
        O resultado que a função devolve ao ponto onde foi chamada, usando a palavra-chave `return`. Uma função pode não retornar nenhum valor. Neste caso, em Python, o valor `None` é implicitamente retornado. Outras linguagens chamam de `void`.


### Funções com número de argumentos variáveis

Há casos específicos onde é conveniente permitir que uma função possa receber uma quantidade indeterminada de argumentos. Para este fim, a linguagem Python oferece dois recursos distintos: usando `*args` para argumentos posicionais variáveis e `**kwargs` para argumentos nomeados variáveis. 



!!! info "Como funcionam parâmetros de quantidade variável?"

    === "Argumentos Posicionais Variáveis (`*args`)"

        Quando não sabemos de antemão quantos argumentos serão passados para uma função, é possível usar `*args` na definição da função. `*args` permite que a função receba um número arbitrário de argumentos posicionais, que são recebidos internamente como uma tupla.

        ```python
        def soma(*args):
            return sum(args)

        print(soma(1, 2, 3))        
        print(soma(10, 20, 30, 40)) 
        ```

    === "Argumentos Nomeados Variáveis (`**kwargs`)"

        Para o case de uma quantidade variável de argumentos nomeados, utilizamos `**kwargs`. `**kwargs` permite que a função receba um número arbitrário de argumentos nomeados, que são recebidos internamente como um dicionário.

        

        ```python
        def imprimir_dados(**kwargs):     
            for chave, valor in kwargs.items():
                print(f"{chave}: {valor}")

        imprimir_dados(nome="Alice", idade=30, cidade="São Paulo")
        ```
        

    === "Combinação de `*args` e `**kwargs`"

        É possível combinar `*args` e `**kwargs` na mesma função para aceitar uma quantidade variável de argumentos posicionais e nomeados. Quando usados juntos, `*args` deve vir antes de `**kwargs` na definição da função.

        

        ```python
        def misturar_argumentos(a, b, *args, **kwargs):
            print(f"a: {a}, b: {b}")
            print("args:", args)
            print("kwargs:", kwargs)
        misturar_argumentos(1, 2, 3, 4, 5, x=10, y=20)
        ```


### Escopo e ciclo de vida de variáveis

Quando trabalhamos com funções, assim como ocorre com outros comandos de bloco, devemos estar cientes do **escopo de visibilidade** das variáveis e de seu **ciclo de vida**. O escopo de uma variável refere-se ao contexto dentro do qual essa variável é reconhecida e pode ser utilizada na programação. Já o ciclo de vida diz respeito ao período de existência em memória, desde a criação até sua destruição.

No **escopo local**, variáveis ali definidas existem somente naquele contexto. São variáveis disponíveis apenas às instruções do escopo e seus subníveis.  É o caso de variáveis criadas dentro de funções, cuja existência se restringe ao corpo da mesma. Utilizar variáveis locais é uma boa prática de programação. Outro ponto importante é que a variável somente está disponível para uso após a sua declaração. Isso significa que, em instruções anteriores, mesmo estando no escopo de visibilidade, a variável estará indisponível.

   ```python
   def minha_funcao():
       x = 10  # X só existe no contexto desta função
       print(x)
   ```

O **escopo global**, por sua vez, compreende as variáveis definidas fora de qualquer função. Estas variáveis são acessíveis em qualquer parte do programa. Sempre que possível, o escopo global deve ser evitado. Isso porque o uso deste tipo de variável cria dependências desnecessárias entre os componentes e aumenta a probabilidade de ocorrência de bugs. **A regra de ouro é evitar variáveis globais**.

   ```python
   x = 10  # Esta variável vale para todo o programa
   
   def minha_funcao1():
       x = x + 1

   def minha_funcao2():
       print(x)

    
   ```

 
Para certas situações, é necessário utilizar as palavras reservadas [`global`](https://www.w3schools.com/python/ref_keyword_global.asp) e [`nonlocal`](https://www.w3schools.com/python/ref_keyword_nonlocal.asp) para resolver questões associadas com escopo de variáveis no Python.

## Captura e tratamento de exceções


Exceções são eventos que ocorrem durante a execução de um programa e interrompem seu fluxo normal devido a situações inesperadas ou erros. Elas são usadas para lidar com condições anômalas, como entrada inválida do usuário, falhas na rede, falta de memória ou tentativa de acesso a um arquivo inexistente. O desenvolvedor pode criar também exceções customizadas que representam estados inválidos de negócio, como saldo negativo, limite de transferência excedido, entre outras situações.


Na maioria das linguagens de programação, as exceções são tratadas por meio de blocos de tratamento que capturam e lidam com os erros de maneira controlada. O fluxo típico envolve:

1.	**Lançamento da Exceção (Throwing an Exception)**: Quando um erro ocorre, a linguagem gera uma exceção automaticamente, ou o programador pode lançá-la explicitamente.
2.	**Captura da Exceção (Catching an Exception)**: Um bloco de código tenta capturar e tratar a exceção para evitar que o programa falhe inesperadamente (termine abruptamente).
3.	**Finalização (Finally Block - opcional)**: Algumas linguagens como o Python permitem executar um bloco de código independentemente de ter ocorrido ou não uma exceção.


O `try`, `except`, `finally` é a estrutura em Python que permite lidar com exceções de forma controlada e garantir que determinadas ações sejam executadas independentemente de ocorrer uma exceção ou não. 


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

!!! info  "Detalhando a estrutura try/except/finally"

    === "Bloco try`"
        Corresponde ao código do fluxo normal de execução que se deseja monitorar a ocorrência de exceções. Sua presença é obrigatória.

  
    === "Bloco `except`"
        Este bloco captura exceções específicas que podem ocorrer dentro do bloco `try`. É possível ter vários blocos `except` para diferentes tipos de exceções. Isso permite tornar o tratamento de cada tipo de situação específico.

    === "Bloco `else`"
        É opcional e executado apenas se nenhuma exceção ocorrer dentro do bloco `try`. É útil para código que deve ser executado apenas em caso de não ter ocorrido exceções.
    
    === "Bloco `finally`"
        Se declarado, o bloco `finally` será sempre executado, independentemente de ocorrer uma exceção ou não dentro do bloco `try`. É usado para garantir que determinadas ações, como a liberação de recursos, sejam executadas mesmo em caso de exceção.


A biblioteca padrão do Python oferece diversos tipos de exceção nativas. A lista completa pode ser encontrada na [documentação oficial](https://docs.python.org/3/library/exceptions.html).



## Coleções de Dados

As coleções de dados são estruturas fundamentais em programação utilizadas para armazenar e organizar múltiplos valores de maneira eficiente. Elas permitem a manipulação de grandes volumes de informação, possibilitando operações como inserção, remoção, pesquisa e iteração de elementos.

Em Python, as coleções mais comuns são listas, tuplas, conjuntos e dicionários. As listas são estruturas ordenadas e mutáveis, permitindo a adição e remoção de elementos conforme necessário. Já as tuplas são semelhantes às listas, porém imutáveis, o que garante maior segurança e eficiência quando os dados não precisam ser alterados.

Os conjuntos são coleções não ordenadas que não permitem elementos duplicados, sendo úteis para operações como união e interseção. Por outro lado, os dicionários armazenam pares de chave e valor, possibilitando acesso rápido aos dados por meio de uma chave única, em vez de um índice numérico.

Cada tipo de coleção possui características específicas que se adaptam a diferentes necessidades. O uso adequado dessas estruturas melhora o desempenho do código e facilita a manipulação de informações em diversas aplicações. 

Na sequência iremos analisar em detalhes as principais coleções de dados da biblioteca padrão do Python.


### Listas

As listas são uma estrutura de dados versátil que permite armazenar coleções de itens em uma **ordem específica**. São **mutáveis**, o que significa que você pode adicionar, remover e modificar itens conforme necessário sem gerar uma cópia do objeto. Normalmente, as listas são utilizadas para armazenar dados de forma homogênea, ou seja, todos os items apresentam mesmo tipo. Contudo, é possível criar listas com elementos de tipos distintos, pois o Python não impõe a necessidade de homogeneidade.

Para criar uma lista, podemos especificar os valores entre colchetes. Cada elemento deve ser separado dos demais com vírgulas. Caso a lista deva estar vazia, basta utilizar `[]`.


```python
minha_lista = [1, 2, 3, 4, 5]
outra_lista = []
outra_lista.append(10)
outra_lista.append(20)
```

O acesso aos elementos se dá por meio de um índice numérico (inteiro), onde a primeira posição será sempre `0`. O índice deve ser aplicado utilizando o operador de slicing (`[]`).

```python
print(minha_lista[0]) 
print(minha_lista[2])
```

O mesmo se aplica quando almejamos modificar o valor de uma posição: basta atribuir ao índice desejado um novo valor.

```python
minha_lista[0] = 100
print(minha_lista)  
```


Para iterar sobre os elementos de uma lista, o mais comum é utilizar o laço `for`. Em certas condições é interessante utilizá-lo em conjunto com a função [enumerate](https://docs.python.org/3/library/functions.html#enumerate).

```python
for item in minha_lista:
    print(item)
```



!!! info "Principais operações e funções"

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





#### List Comprehension

*List comprehension* é uma maneira concisa e elegante de criar listas em Python. Ela permite criar listas de forma mais eficiente e legível, muitas vezes em uma única linha de código.

A sintaxe utilizada é apresentada na sequência. Observe que `expressão` define cada elemento da nova lista, enquanto `item` corresponde ao elemento presente em `iterável` (origem dos dados para criação da nova lista).


```python
[expressão for item in iterável]
```

O recurso de *list comprehension* é muito utilizado na programação, não somente para criar listas, mas também dicionários e conjuntos. Conhecer bem a sintaxe e aplicação certamente é um diferencial importante.

Vejamos alguns exemplos concretos:

```python
# Lista contendo o quadrado dos valores de 1 a 6
quadrados = [x ** 2 for x in range(1, 6)]

# Lista contendo apenas os números pares da variável `numeros`
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]

# Lista contendo tuplas do resultado das combinações de valores possíveis entre 1 e 4 (produto cartesiano)
tuplas = [(x, y) for x in range(1, 4) for y in range(1, 4)]
```


#### Slicing

*Slicing* é uma técnica que permite extrair partes específicas de uma coleção de dados (string, lista, tupla, etc). O operador de slicing é de grande valia para manipulação eficiente e flexível de dados. A sintaxe básica é  ```string[início:fim:passo]```, onde: 

- `início`: Índice onde o slicing começa. Se não especificado, é considerado o início da string.
- `fim`: Índice onde o slicing termina. Este índice não é incluído na substring resultante. Se não especificado, é considerado o final da string.
- `passo`: Opcional. Define o intervalo entre os caracteres a serem considerados durante o slicing. Se não especificado, o padrão é 1.



Observe alguns exemplos de uso do `slicing`.


```python
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# Pegando do índice 1 ao 4 (o índice 5 não é incluído)
sublista = numeros[1:5]
print(sublista)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Omissão do índice de início (começa do início da lista)
print(numeros[:4])  # [1, 2, 3, 4]

# Omissão do índice de fim (vai até o final da lista)
print(numeros[5:])  # [6, 7, 8, 9]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pegando de 2 em 2
print(numeros[::2])  # [0, 2, 4, 6, 8]

# Pegando de 3 em 3
print(numeros[::3])  # [0, 3, 6, 9]

letras = ['A', 'B', 'C', 'D', 'E']

# Invertendo com slicing
print(letras[::-1])  # ['E', 'D', 'C', 'B', 'A']

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Pegando os elementos de trás para frente de 2 em 2
print(numeros[::-2])  # [90, 70, 50, 30, 10]

```


### Tuplas


 

Uma tupla é uma estrutura de dados semelhante a uma lista, mas com a diferença crucial de que ela é **imutável**. Isso significa que uma vez criada, seus elementos não podem ser alterados. As tuplas são definidas utilizando parênteses `()`.

Geralmente tuplas são utilizadas para agregar dados diversos, mantendo-os imutáveis e dispostos de uma determinada ordem. Se houver apenas um elemento na tupla, é necessário incluir uma vírgula após o elemento para diferenciá-lo de uma expressão entre parênteses. O acesso aos dados é feito por índices e a maneira mais comum de iterar sobre os dados é através do laço `for`.

```python
tupla_com_um_elemento = (10,)
minha_tupla = (1, 2, 3, 4, 5)
tupla_vazia = ()
print(minha_tupla[0])  # Saída: 1
print(minha_tupla[2])  # Saída: 3

for e in minha_tupla:
    print(e)

```



### Dicionários 

Um dicionário é uma estrutura de dados que armazena pares chave-valor. É uma das estruturas de dados mais utilizadas devido à sua eficiência e flexibilidade. Os dicionários são **mutáveis**, o que significa que você pode adicionar, modificar e remover itens conforme necessário. Cada chave em um dicionário deve ser única e associada a um único valor. As chaves podem ser de qualquer tipo, como strings, números, tuplas, listas, outros dicionários, etc.


Para criar um dicionário, devemos utilizar a sintaxe de chaves `{}` e especificar os pares chave-valor separados por vírgulas. O acesso aos valores armazenados é feito por meio da chave informada entre `[]`.

```python
meu_dicionario = {"nome": "Alice", "idade": 30, "cidade": "Nova York"}
outro_dicionario = {}
outro_dicionario["marca"] = "Toyota"
outro_dicionario["modelo"] = "Corolla"
```

Se a chave não existir no dicionário, será lançada uma exceção `KeyError`. Para evitar isso, podemos utilizar usar o método `get()`, que permite indicar um valor padrão caso a chave não exista.

```python
print(meu_dicionario.get("cidade", "Não encontrado"))  # Saída: Nova York
print(meu_dicionario.get("profissão", "Não encontrado"))  # Saída: Não encontrado
```

Os principais métodos disponíveis em objetos de dicionário são:

- `keys()`: Retorna uma lista contendo todas as chaves do dicionário.
- `values()`: Retorna uma lista contendo todos os valores do dicionário.
- `items()`: Retorna uma lista de tuplas contendo todos os pares chave-valor do dicionário.
- `update()`: Atualiza o dicionário com os pares chave-valor de outro dicionário ou de uma sequência de pares chave-valor.



### Conjuntos

Um conjunto é uma estrutura de dados que armazena elementos únicos e não ordenados. Os conjuntos são muito úteis para realizar operações de conjunto oriundos da Matemática, como união, interseção, diferença e teste de pertencimento. Os conjuntos são mutáveis, assim como listas e dicionários.

Para criar um conjunto utilizamos a função `set()` ou a sintaxe de chaves `{}`. Se o objetivo for criar um conjunto vazio, então será necessário utilizar `set()`.

```python
meu_conjunto = {1, 2, 3, 4, 5}
conjunto_vazio = set()
```

Para adicionar elementos, utilizamos o método `add()`. Já para remover um elemento, temos a disposição os métodos `remove()` ou `discard()`. A diferença é que `remove()` gera um erro se o elemento não estiver presente no conjunto, enquanto `discard()` não gera nenhum erro.

```python
meu_conjunto.add(6)
meu_conjunto.remove(5)
meu_conjunto.discard(2)
```

 
Tal qual ocorre na Matemática, o uso de conjuntos no Python oferece suporte às mesmas operações. Para fins didáticos, vamos utilizar como exemplo dois conjuntos de números inteiros, identificados pelas variáveis `conjunto_a` e `conjunto_b`. Tais conjuntos contém os seguintes valores:

```python
conjunto_a = {1, 3, 5, 7, 9}
conjunto_b = {2, 4, 6, 8, 10}

print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)
```

!!! note "Operações sobre conjuntos"

    === "`union()`, `|`" 
        Retorna um novo conjunto com todos os elementos de ambos os conjuntos.

        ```python
        conjunto_uniao = conjunto_a | conjunto_b
        print("Conjunto União:", conjunto_uniao)
        ```

    === "`intersection()`, `&`:" 
        Retorna o que há de comum entre ambos os conjuntos.

        ```python
        conjunto_inserseccao = conjunto_a & conjunto_b
        print("Conjunto Intersecção:", conjunto_inserseccao)
        ```

    === "`difference()`, `-`" 
        Retorna um novo conjunto com os elementos presentes no primeiro conjunto que não estão no segundo.

        ```python
        conjunto_diferenca = conjunto_a - conjunto_b
        print("Conjunto Diferença:", conjunto_diferenca)
        ```

    === "`symmetric_difference()`, `^`" 
        Retorna um novo conjunto contendo os elementos que estão em apenas um dos conjuntos, nunca em ambos.
    
        ```python
        conjunto_diferenca = conjunto_a ^ conjunto_b
        print("Conjunto Diferença:", conjunto_diferenca)
        ```

    === "`issuperset()`, `>=`"
        Verifica se um conjunto é **superconjunto** de outro. Para ser superconjunto, é necessário ter todos os elementos do outro conjunto avaliado, sendo possível ter elementos adicionais.

        ```python
        conjunto_a >= conjunto_b
        ```

    === "`issubset()`, `<=`"
        Verifica se um conjunto é **subconjunto** de outro. Para ser subconjunto é preciso que todos os elementos do conjunto estejam contidos no outro avaliado.

        ```python
        conjunto_a <= conjunto_b
        ```


 



