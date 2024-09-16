Escala é uma linguagem fortemente tipada com suporte a orientação a objetos e paradigma funcional. Tudo é objeto, inclusive as funções.

Literais são iguais ao Java. O operador de concatenção é o mesmo.

```scala

println(1)
println(1+1)
println("Olá," + "mundo")


A interpolação de strings é possível iniciando o literal com `s` e indicando as variáveis com `$`.

```

A declaração de variáveis é feita por meio da keywork  `var`.

```scala

var total = 1 + 1

```

Já no caso de constantes, utiliza-se `val`.

A tipagem é estática. Na declaração o tipo da variável pode ser omitido, pois o compilador infere. Ou também é possível explicitamente defini-lo:

```scala

var total: Int = 1 + 1

```

Pode-se criar blocos com `{}`. Neste caso, o resultado da última expressão será o resultado de todo o bloco.


```scala

println(
    {
        var y: Int = 3
        y+=1
        y
    }
)
```

### Funções

As funções são expressões que definem parâmetros e recebem argumentos. Quando anônimas, podemos defini-las da seguinte forma:



```scala

val fx = (a:Int, b:Int) => a*b

println(fx(2,4))

```

Parâmetros podem ter valor default

Argumentos podem ser informados informando-se o nome do parâmetro.

### Métodos

A definição de métodos deve ser por meio da palavra reservada `def` e a declaração é diferente se comparada com as funções. Observe:


```scala

def aMethod (a:Int, b:Int): Int = a*b*43

println(aMethod(2,4))

```

Quando o método possuir várias linhas, a última do bloco será o retorno. a palavra-chave `return` está disponível na linguagem.

## class

A criação de classes pode incorporar a declaração do nome da classe conjuntamente com o construtor e, naturalmente, os métodos.

Se um construtor não for informado, a classe terá um padrão.

Instâncias são criadas a partir da keywork `new`.

Parametros de construtores podem ter valor padrão.

A definição de parâmetros nos construtores já declara os campos da classe

O construtor é a combinação dos parâmetros, métodos e expressões e instruções executadas no corpo da classe.

Construtores auxiliares (sobrecargas) são criados por meio de um `def this() =>

Membros são públicos por padrão. Para torná-los privados, deve-se utilizar `private`.

Parametros sem as keywords `val` ou `var` são privados, por padrão


Herança simples.

## object

Objetos são instâncias únicas de suas próprias definições. Utiliza-se a keywork `object` para declarar. São singletons, ou seja, classes de única instância. É criado tardiamente, quando referenciado. Interessante para métodos utilitários.


Companion objects ocorre quando, no mesmo arquivo Scala, temos uma `class` e um `object`  de mesmo nome. Serve aos seguintes propósitos:

- Separação de responsabilidades
- Implementação de factories e builders


`Class` definem membros não estáticos. `Objects` define membros estáticos.



## trait (característica)

São tipos de dados abstratos que possuem métodos e campos. A classe pode estender múltiplas `traits`. Assemelha-se a interfaces em Java

`override` é utilizado para redefinir métodos

Com Traits é possível fazer mixins, ou seja, uma classe pode estender vários traits.'


## case class

Case classes são classes normais, contudo são imutáveis após atribuídas. São classes estáticas. Não precisam de new para criar objetos. Tem um método padrão chamado apply. 

Na declaração, é preciso preceder a declaração da classe com `case`.

## case objectS


## Arrays

A declaração de arrays é feita da seguinte forma:

```scala

var dados: Array[Float] = new Array[Float] (3)

```

A indexação é feita com `()`. O índice inicial é \[0\]

```scala
dados(1) = 4564.56
```

Para percorrer os itens do array, a sintaxe é:

```scala

for (x <- dados){
    println(x)
}

```


## Tuplas

Tuplas são imutáveis. Cada elemento tem seu tipo específico.

```scala

val valores =("Maça", 2, 5.6)

val (fruta, id, valor) = valores

println(valores._1)

```

É possível acessar o elemento com base na posição utilizando `_`. Também podemos obter os valores em variáveis apartadas.


## Case statement

Equivale ao `switch` da linguagem Java. Contudo pode ser aplicado como corpo de função/método. O caso default é indicado por `case _`. Não é preciso colocar o comando break.



## Estruturas de controle

if sempre retorna valor!