---
title: "Python - Funções"
tags:
 - Programação
 - Linguagens de Programação
 - Python
date: 2024-02-26 08:00:00
---


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