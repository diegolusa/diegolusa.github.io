
Kotlin é uma linguagem moderna desenvolvida pela JetBrains, amplamente utilizada para desenvolvimento Android. Apresenta sintaxe concisa, recursos avançados e forte suporte do Google, que a tornam a primeira opção para desenvolvimento mobile. Caso você conheça a linguagem Java perceberá semelhanças e o aprendizado tende a ser mais rápido. Mas se for seu primeiro contato com a linguagem vale a máxima de sempre: respeite seu tempo e pratique.

---

## Sintaxe Básica

Aprender uma nova linguagem sempre começa pelo entendimento da sua sintaxe e estrutura básica. Aqui falamos de declaração de variáveis, tipos de dados, definição de blocos, funções e classes.

Para declarar variáveis devemos utilizar  `val` para valores imutáveis e `var` para valores mutáveis. Lembre-se que uma variável imutável é toda aquela cujo valor referenciado não pode ser modificado após a primeira atribuição.

```kotlin
val pi = 3.14     
var counter = 0   
counter += 1 
```

Toda variável tem um tipo de dado associado. Isso torna o Kotlin uma **linguagem fortemente tipada**. Contudo, não é sempre necessário definir explicitamente o tipo. É o que chamamos de **inferência de tipos**.

```kotlin
val age: Int = 25          // Tipagem explícita, ou seja, o programador diz qual deve ser o tipo
val name = "John"          // Inferência de tipo, feita automaticamente com base no valor atribuído na inicialização (String)
```

Em termos de operadores matemáticos nada foge dos conhecidos símbolos. E, além destes, temos operadores de incremento e decremento pré e pós-fixados (`++` e `--`).

| **Operador** | **Descrição**             | **Exemplo** | **Resultado** |
| ------------ | ------------------------- | ----------- | ------------- |
| `+`          | Adição                    | `5 + 3`     | `8`           |
| `-`          | Subtração                 | `5 - 3`     | `2`           |
| `*`          | Multiplicação             | `5 * 3`     | `15`          |
| `/`          | Divisão                   | `5 / 2`     | `2` (Inteiro) |
| `%`          | Módulo (resto da divisão) | `5 % 2`     | `1`           |


Certamente uma característica importante da linguagem chama-se `null safety`. Trata-se de um recurso que permite ao interpretador antecipar e evitar problemas relacionados ao acesso de valores e métodos em variáveis nulas (comuns no Java, por exemplo). 

Quatro operadores são utilizados especificamente para o recurso de `null safety` além do símbolo de `?` junto ao tipo. Ou seja, quando desejamos declarar uma variável que pode vir a receber valores nulos, devemos acrescentar `?` ao nome do tipo. Veja:


```kotlin
    var nome: String? = null //a variável aceita nulo
    var idade: Int = 0 // a variável não aceita nulo
```

Os operadores especificamente associados com `null safety`são:

- **Safe Call (?.)**: acessa métodos e propriedades de uma variável somente se ela não for nula.

```kotlin
    val nome: String? = null
    println(nome?.length) 
```


- **Elvis Operator (?:)**: retorna um valor padrão caso a propriedade seja nula.

```kotlin
    val nullableName: String? = null
    val length = nullableName?.length ?: 0 
    println(length)  //Aqui, o retorno será zero
```

- **Non-Null Assertion (!!)**: garante que a variável não é `null` e lança um NullPointerException se essa garantia for falsa.
  
```kotlin

    val nullableName: String? = null
    println(nullableName!!.length)

```

- **Safe Cast (as?)**: tenta converter um tipo e retorna `null` se a conversão falhar.

```kotlin

    val valor: Any = "Kotlin"
    val str: String? = valor as? String  //ok, será convertido com sucesso
    val num: Int? = obj as? Int        // Retorna null, pois a conversão não é possível

```

### Tipos de Dados Comuns

| **Tipo**      | **Descrição**                                            | **Tamanho**       | **Exemplo**                                                        |
| ------------- | -------------------------------------------------------- | ----------------- | ------------------------------------------------------------------ |
| `Int`         | Número inteiro                                           | 32 bits           | `val number: Int = 42`                                             |
| `Long`        | Número inteiro longo                                     | 64 bits           | `val bigNumber: Long = 123456789L`                                 |
| `Short`       | Número inteiro curto                                     | 16 bits           | `val smallNumber: Short = 32000`                                   |
| `Byte`        | Número inteiro pequeno (byte)                            | 8 bits            | `val byteValue: Byte = 127`                                        |
| `Float`       | Número de ponto flutuante (precisão simples)             | 32 bits           | `val floatValue: Float = 3.14F`                                    |
| `Double`      | Número de ponto flutuante (precisão dupla)               | 64 bits           | `val doubleValue: Double = 3.141592653589793`                      |
| `Char`        | Um único caractere                                       | 16 bits (Unicode) | `val charValue: Char = 'A'`                                        |
| `String`      | Sequência de caracteres                                  | Tamanho variável  | `val text: String = "Hello, Kotlin!"`                              |
| `Boolean`     | Representa valores lógicos                               | 1 bit             | `val isKotlinFun: Boolean = true`                                  |
| `Array`       | Coleção ordenada de elementos                            | Tamanho variável  | `val numbers: Array<Int> = arrayOf(1, 2, 3)`                       |
| `List`        | Lista imutável de elementos                              | Tamanho variável  | `val items: List<String> = listOf("Apple", "Banana")`              |
| `MutableList` | Lista mutável de elementos                               | Tamanho variável  | `val items: MutableList<String> = mutableListOf("Apple")`          |
| `Set`         | Conjunto imutável sem elementos duplicados               | Tamanho variável  | `val uniqueItems: Set<Int> = setOf(1, 2, 3)`                       |
| `MutableSet`  | Conjunto mutável sem elementos duplicados                | Tamanho variável  | `val uniqueItems: MutableSet<Int> = mutableSetOf(1, 2)`            |
| `Map`         | Coleção de pares chave-valor                             | Tamanho variável  | `val map: Map<String, Int> = mapOf("A" to 1, "B" to 2)`            |
| `MutableMap`  | Coleção mutável de pares chave-valor                     | Tamanho variável  | `val mutableMap: MutableMap<String, Int> = mutableMapOf("A" to 1)` |
| `Any`         | Tipo raiz de todos os objetos                            | -                 | `val anyValue: Any = "Kotlin"`                                     |
| `Unit`        | Representa a ausência de valor em funções                | -                 | Funções sem retorno explícito retornam `Unit`                      |
| `Nothing`     | Representa a ausência de um valor ou código inalcançável | -                 | `fun fail(): Nothing = throw Exception("Erro")`                    |

---




## Controle de Fluxo

No que diz respeito a estruturas condicionais, o Kotlin utiliza `if` e `when`. A sintaxe do  `if` é semelhante a muitas outras linguagens, mas se destaca pela possibilidade de retornar valores, tal qual ocorre com o `when`. Este último, por sua vez, é um comando mais sofisticado, apresentando diversas variações.

```kotlin
    val numero = 10

    // Usando if-else
    val resultado = if (numero % 2 == 0) "Par" else "Ímpar"

    // Usando when (substituto do switch)
    val nota = "A"
    val feedback = when(x) {
        0 -> "Zero" // quando exatamente zero
        in 1..4 -> "Four or less" // quando entre 1 e 4
        5, 6, 7 -> "Five to seven" // se 5, 6 ou 7
        is Byte -> "Byte" // se o tipo for byte
        else -> "Some number" // caso nenhuma das opções
    }
```

Os operadores lógicos da linguagem estão descritos na tabela abaixo.

| **Operador** | **Descrição**                                                                           | **Exemplo**           | **Resultado**                                                                 |
| ------------ | --------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------- |
| `&&`         | **E lógico**: Retorna `true` se ambas as condições forem verdadeiras.                   | `(x > 0) && (y > 0)`  | `true` se `x > 0` e `y > 0`                                                   |
| `            |                                                                                         | `                     | **OU lógico**: Retorna `true` se pelo menos uma das condições for verdadeira. | `(x > 0) |  | (y < 0)` | `true` se uma das condições for verdadeira |
| `!`          | **Não lógico**: Inverte o valor lógico de uma condição.                                 | `!(x > 0)`            | `true` se `x <= 0`                                                            |
| `xor`        | **OU exclusivo lógico**: Retorna `true` se exatamente uma das condições for verdadeira. | `(x > 0) xor (y > 0)` | `true` se apenas uma condição for verdadeira                                  |

---


## Laços de Repetição

Os laços de repetição disponíveis são `for`, `while`e `do-while`, assim como outras em linguagens de programação. O laço `for` também permite percorrer coleções de dados de forma simplifica, tornando o código mais sucinto.


```kotlin
// Iterando sobre uma lista
val items = listOf("Apple", "Banana", "Cherry")
for (item in items) {
    println(item)
}

// Laço while
var count = 3
while (count > 0) {
    println("Contagem: $count")
    count--
}

```

## Funções

Funções em Kotlin podem ser declaradas de vários formas. Suportam parâmetros e valores de retorno.


```kotlin

fun add(a: Int, b: Int): Int {
    return a + b
}

// Função de linha única
fun multiply(a: Int, b: Int) = a * b

println(add(3, 5))       // 8
println(multiply(4, 7))  // 28


```

### Funções lambdas

Funções lambda são funções anônimas (sem nome) que podem ser armazenadas em variáveis e passadas como argumento para outras funções. Elas são muito utilizadas para programação funcional e manipulação de coleções. Para criar uma variável que armazena uma função lambda, precisamos de uma declaração nos moldes de `val nomeDaLambda: (TipoDoParametro) -> TipoDeRetorno = { parametro -> expressão }`. O mesmo vale para declarar parâmetros que aceitam tais funções (neste caso, a implementação da função depois do `=` é opcional).

Quando uma lambda tem apenas um parâmetro, podemos usar `it` para referenciá-lo implicitamente no código. Trata-se de uma convenção da linguagem.

```kotlin
val saudacao: (String) -> String = { "Olá, $it!" }
println(saudacao("Kotlin"))
```

Outro recurso interessante aplica-se quando uma função recebe uma lambda como seu último argumento. Nesta situação podemos colocá-la fora dos parênteses da chamada da função utilizando uma sintaxe alternativa conhecida como `Trailing Lambda Syntax (Sintaxe de Lambda no Final)`.


```kotlin

fun calcular(a: Int, b: Int, operacao: (Int, Int) -> Int): Int {
    return operacao(a, b)
}

fun main() {
    // forma convencional
    val resultado = calcular(5, 3, { x, y -> x + y })
    println(resultado) 

    // trailing lambda sintax
    val resultado = calcular(5, 3) { x, y -> x + y }
    println(resultado) 

}

```






## Orientação a Objetos

A **Programação Orientada a Objetos (POO)** é um paradigma de programação baseado no conceito de objetos, que encapsulam **dados (atributos)** e **comportamentos (métodos)**. Kotlin é uma linguagem moderna que suporta POO e oferece recursos interessantes para facilitar o desenvolvimento de software.


### Classes e Objetos

Uma **classe** é um modelo que define um conjunto de atributos e métodos que um objeto pode ter. Em Kotlin, utilizamos a palavra-chave `class` para definir uma classe.

```kotlin
class Pessoa {
    var nome: String = ""
    var idade: Int = 0

    fun apresentar() {
        println("Olá, meu nome é $nome e tenho $idade anos.")
    }
}

fun main() {
    val pessoa1 = Pessoa()
    pessoa1.nome = "João"
    pessoa1.idade = 25
    pessoa1.apresentar()
}
```

### Construtures

Construtores são métodos especiais de uma classe, cuja finalidade é definir o estado inicial dos objetos. No Kotlin, temos a possibilidade de definir construtores primários e secundários. 

O construtor primário é definido na declaração da classe e permite inicializar as propriedades de forma direta. Para executar alguma lógica de inicialização adicional, é possível utilizar o bloco `init`. Já o secundário é definido dentro da classe através da palavra reservada `constructor`. Os construtores secundários representam formas alternativas de inicializar um novo objeto da classe em questão.

```kotlin
class Pessoa(val nome: String, val idade: Int) {
    init {
        println("objeto inicializado")
    }
    fun apresentar() {
        println("Olá, meu nome é $nome e tenho $idade anos.")
    }
}

class Aluno(val nome: String) {
    var idade: Int = 0

    constructor(nome: String, idade: Int) : this(nome) {
        this.idade = idade
    }
}

```



### Data Class

*Data classes* são usadas para representar modelos de dados de forma simples. Isso porque o próprio compilador fica responsável por gerar algums métodos importantes, como `equals`, `hashcode`, `tostring`, `componentN` e `copy`. Assim, a forma mais simples de declaração de um `data class` compreende definir seu nome e a lista de seus atributos através do construtor principal.


```kotlin

data class Usuario(val nome: String, val idade: Int)

fun main() {
    val usuario1 = Usuario("Carlos", 28)
    val usuario2 = usuario1.copy(idade = 30)
    
    println(usuario1)
    println(usuario2)
}

```