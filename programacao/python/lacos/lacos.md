---
title: "Python - Laços de Repetição"
tags:
 - Programação
 - Linguagens de Programação
 - Python
 - Laços de Repetição
date: 2024-02-26 08:00:00
---


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
 

 