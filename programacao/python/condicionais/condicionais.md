---
title: "Comandos Condicionais"
tags:
 - Programação
 - Linguagens de Programação
 - Python
date: 2024-02-26 08:00:00
---


Em Python, assim como em praticamente todas as linguagens de programação, os comandos condicionais desempenham um papel fundamental na execução de um código de forma controlada e adaptável. Eles permitem que um programa tome decisões com base em condições específicas, direcionando o fluxo de execução do código de acordo com o resultado dessas condições.



## Comando IF
O comando condicional mais básico em Python é o **IF**, que permite verificar se uma condição é verdadeira e executar um bloco de código associado a ela. 

```python
idade = 18

if idade >= 18:
    print("Idade igual ou superior a 18 anos.")
```

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
        |-------|-------|---------|
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
        | A     | B     | A or B  |
        |-------|-------|---------|
        | True  | True  | True    |
        | True  | False | True    |
        | False | True  | True    |
        | False | False | False   |



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
    |-------|-------|
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