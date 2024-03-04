---
title: "Python - Introdução"
tags:
 - Programação
 - Linguagens de Programação
 - Python
date: 2024-02-26 08:00:00
---




Python é uma linguagem de programação de alto nível, interpretada, multiparadigma e de tipagem dinâmica. Desenvolvida por Guido van Rossum e lançada pela primeira vez em 1991, Python ganhou imensa popularidade devido à sua sintaxe simples e legibilidade, tornando-a uma escolha preferida para uma variedade de aplicações, desde desenvolvimento web, ciência de dados, engenharia de dados e automação de tarefas, por exemplo. Possui um ecossistema muito rico em bibliotecas e ferramentas, as quais ajudaram a tornar a linguagem tão popular no mercado de tecnologia. 

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

## Entrada e Saída

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

Em Python, os operadores aritméticos são utilizados para realizar operações matemáticas em valores numéricos. São operadores como o de adição, subtração, multiplicação, divisão, por exemplo. Na sequência vamos apresentar eles.

### Adição (+)

O operador de adição (+) é utilizado para somar dois valores. Por exemplo:

```python
resultado = 5 + 3
# resultado será igual a 8
```

### Subtração (-)

O operador de subtração (-) é utilizado para subtrair um valor de outro. Por exemplo:

```python
resultado = 10 - 7
# resultado será igual a 3
```

### Multiplicação (*)

O operador de multiplicação (*) é utilizado para multiplicar dois valores. Por exemplo:

```python
resultado = 4 * 6
# resultado será igual a 24
```

### Divisão (/)

O operador de divisão (/) é utilizado para dividir um valor pelo outro. Por exemplo:

```python
resultado = 20 / 5
# resultado será igual a 4.0 (resultado sempre será um float em Python 3.x)
```

### Divisão Inteira (//)

O operador de divisão inteira (//) divide um valor pelo outro e retorna apenas a parte inteira do resultado. Por exemplo:

```python
resultado = 20 // 6
# resultado será igual a 3
```

### Resto da Divisão (%)

O operador de resto da divisão (%) retorna o resto da divisão de um valor pelo outro. Por exemplo:

```python
resto = 20 % 6
# resto será igual a 2 (porque 20 dividido por 6 é igual a 3, com um resto de 2)
```

### Exponenciação (**)

O operador de exponenciação (**) é utilizado para elevar um número a uma potência. Por exemplo:

```python
resultado = 2 ** 3
# resultado será igual a 8 (2 elevado à potência de 3)
```


## Comentários

Comentários são trechos de texto dentro do código fonte que são ignorados pelo interpretador Python durante a execução do programa. Eles são utilizados para explicar o código, fazer anotações, fornecer documentação ou desativar temporariamente partes do código. Seu uso é altamente recomendável, pois auxilia na compreensão do código. 

Temos a disposição diferentes duas maneiras distintas de comentar código: comentário de linha e comentário de bloco.

Comentários de linha começam com o símbolo `#` e continuam até o final da linha. Eles são úteis para adicionar breves explicações ou notas em uma única linha de código. Por exemplo:

```python
# Este é um comentário de linha
numero = 10  # Este comentário segue o código na mesma linha
```

Já os comentários em bloco são utilizados para comentar várias linhas de código e são delimitados por três aspas simples (`'''`) ou três aspas duplas (`"""`). Eles são frequentemente utilizados para documentar funções, classes ou trechos de código mais extensos. Por exemplo:

```python
'''
Este é um comentário em bloco.
Ele pode abranger várias linhas.
'''
```

### Boas Práticas de Uso

- **Seja descritivo**: Escreva comentários que explicam o que o código faz, não o óbvio. Isso ajuda a entenderem o propósito do código.
- **Mantenha os domentários atualizados**: Se o código for alterado, lembre-se de atualizar os comentários correspondentes para manter a precisão.
- **Evite comentários óbvios**: Comentários que simplesmente repetem o que o código faz sem adicionar valor são desnecessários e podem poluir o código. 


## Indentação de código

Em Python, a indentação é um conceito fundamental e parte integrante da sintaxe da linguagem. Diferentemente de muitas outras linguagens de programação, que utilizam chaves `{}` para delimitar blocos de código, Python utiliza a indentação para definir a estrutura e a organização do código.

A indentação é utilizada para indicar a estrutura hierárquica do código, especialmente em construções como loops, condicionais, funções e classes. Ela define quais linhas de código estão dentro de um determinado bloco e quais estão fora.

Por convenção, é recomendado utilizar *quatro espaços* para cada nível de indentação. Embora o uso de tabulações (tab) seja permitido, é uma prática comum e recomendada seguir a convenção de espaços. Isso garante consistência em todo o código e evita problemas de formatação em diferentes ambientes de desenvolvimento.

```python
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

No exemplo acima, as linhas de código dentro do bloco `if` e `else` estão indentadas com quatro espaços, indicando que elas pertencem a esses blocos condicionais.

### Erros de Indentação

Erros de indentação são comuns em Python e podem levar a resultados inesperados ou a mensagens de erro. Por exemplo, se a indentação não estiver correta, o código pode não funcionar como esperado ou gerar um erro de sintaxe. Logo, é importante manter as boas práticas enquanto escrevemos código.

Neste aspecto, o uso de IDEs especializadas para desenvolvimento auxilia o programador, pois a formatação do código é automaticamente ajustada pelo editor.




## Conversões de Dados

Mesmo sendo uma linguagem dinamicamente tipada, o Python oferece funções embutidas para converter entre diferentes tipos de dados. Essas conversões são úteis, e em certos casos necessárias, para modificar o tipo de dado de uma variável para um uso específico. Vejamos alguns casos de conversão na sequência.

### Conversão de Inteiro para String

Para converter um número inteiro em uma string, utilizamos a função `str()`.

```python
numero = 10
numero_string = str(numero)
```

### Conversão de String para Inteiro

Para converter uma string em um número inteiro, utilizamos a função `int()`.

```python
numero_string = "10"
numero = int(numero_string)
```

### Conversão de String para Float

Para converter uma string em um número de ponto flutuante (float), utilizamos a função `float()`.

```python
numero_string = "3.14"
numero_float = float(numero_string)
```

### Conversão de Float para Inteiro

Para converter um número de ponto flutuante em um número inteiro, aplicamos a função `int()`. Isso porque a função remove a parte decimal do valor.

```python
numero_float = 3.14
numero_inteiro = int(numero_float)
```


## Exercícios 

Que tal aplicar o que aprendeu resolvendo alguns [exercícios](res/notebooks/aula-1.ipynb)? 


## Fonte

- Documentação oficial do Python: [python.org](https://docs.python.org/)

