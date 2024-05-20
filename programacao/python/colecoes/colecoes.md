---
title: "Coleções de Dados - Listas, Tuplas, Conjuntos e Dicionários"
tags:
 - Programação
 - Linguagens de Programação
 - Python
date: 2024-02-26 08:00:00
---

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