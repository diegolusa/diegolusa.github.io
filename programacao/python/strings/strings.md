---
title: "Python - Strings"
tags:
 - Programação
 - Linguagens de Programação
 - Python
 - Strings
date: 2024-02-26 08:00:00
---

As strings são usadas para representar texto e são imutáveis, o que significa que uma vez que uma string é criada, ela não pode ser alterada. Python fornece uma variedade de métodos embutidos para manipular e operar em strings de maneira eficiente. Vamos explorar alguns dos métodos mais comuns. Caso você queira conhecer em detalhes todos os métodos, acesse  [a documentação oficial sobre cadeias de caracteres](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) da linguagem.

## `len()`

Retorna o comprimento da string, ou seja, o número de caracteres presentes nela.

```python
string = "Olá, mundo!"
print(len(string))
```

## `upper()` e `lower()`

`upper()` converte todos os caracteres da string para maiúsculo, enquanto `lower()` os converte para minúsculo.


```python
string = "Olá, Mundo!"
print(string.upper())
print(string.lower())
```

## `strip()`, `lstrip()` e `rstrip()`

Removem espaços em branco e caracteres especiais do início e/ou final da string.

Exemplo:
```python
string = "   Olá, Mundo!   "
print(string.strip())
print(string.lstrip())
print(string.rstrip())
```

## `split()` e `join()`

`split()` divide a string em uma lista de substrings com base em um separador, enquanto `join()` junta uma lista de strings em uma única string.


```python
string = "Python é uma linguagem de programação"
lista = string.split()
print(lista) 

string_nova = "-".join(lista)
print(string_nova)
```

## `replace()`

Substitui todas as ocorrências de uma substring por outra.

```python
string = "Python é incrível!"
nova_string = string.replace("incrível", "fantástica")
print(nova_string)
```

## `startswith()` e `endswith()`

Verificam se a string começa ou termina com uma determinada substring, respectivamente.

Exemplo:
```python
string = "Olá, Mundo!"
print(string.startswith("Olá"))
print(string.endswith("!"))     
```

## `find()` e `index()`

`find()` retorna a primeira ocorrência de uma substring na string, enquanto `index()` retorna o índice da primeira ocorrência. A diferença é que `index()` gera uma exceção se a substring não for encontrada.

```python
string = "Python é uma linguagem de programação"
print(string.find("linguagem"))
print(string.index("linguagem"))
```

## `count()`

Conta o número de ocorrências de uma substring na string.

Exemplo:
```python
string = "Python é uma linguagem de programação, e Python é incrível!"
print(string.count("Python"))
```


## `str.translate(table)`

O método `translate()` retorna uma cópia da string original onde cada caractere foi traduzido usando a tabela de tradução fornecida.

```python

tabela = str.maketrans("aeiou", "12345")
string_original = "Olá, mundo!"
string_traduzida = string_original.translate(tabela)
print(string_traduzida)

```

O método `translate()` é útil para realizar operações de tradução em strings de maneira eficiente e rápida. Ele é especialmente útil quando você precisa substituir caracteres por outros em grandes volumes de dados.