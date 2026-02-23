
Kotlin é uma linguagem moderna desenvolvida pela JetBrains, amplamente utilizada para desenvolvimento Android. Ela apresenta sintaxe concisa, recursos avançados e suporte do Google, que a tornam uma das principais opções para desenvolvimento mobile nativo. Para estudantes com familiaridade em Java, é comum perceber semelhanças e ter um aprendizado mais rápido. Para quem está no primeiro contato com a linguagem, o progresso tende a ser melhor quando o estudo é acompanhado de prática frequente.


---

## Primeiros passos (ambiente e execução)

Para iniciar o desenvolvimento com Kotlin, os estudantes precisam de um ambiente mínimo: um **JDK** instalado e uma ferramenta para escrever e executar código. No ecossistema Kotlin, duas abordagens são comuns:

1. **Kotlin/JVM (console/back-end)**: usado para programas de linha de comando e aplicações no servidor.
2. **Android (mobile)**: usado em projetos Android, geralmente com Android Studio.
3. **Kotlin Playground**: uma opção online para experimentar código Kotlin sem configuração local, disponível em [https://play.kotlinlang.org/](https://play.kotlinlang.org/).
4. 

Exemplo de arquivo inicial (`Main.kt`) para Kotlin/JVM:

```kotlin
package app

fun main() {
    println("Olá, Kotlin!")
}
```

Em Android, o ponto de entrada costuma ser uma `Activity` (o projeto Android já fornece a estrutura e dependências):

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```

## Sintaxe Básica

Aprender uma nova linguagem sempre começa pelo entendimento da sua sintaxe e estruturas básicas. Aqui falamos de declaração de variáveis, tipos de dados, definição de blocos, funções e classes.

Para declarar variáveis, usa-se `val` para valores imutáveis e `var` para valores mutáveis. Uma variável imutável é aquela cujo valor referenciado não pode ser modificado após a primeira atribuição.

```kotlin
val pi = 3.14     
var counter = 0   
counter += 1 
```

Toda variável tem um tipo de dado associado. Isso torna o Kotlin uma **linguagem fortemente tipada**. Contudo, não é sempre necessário definir explicitamente o tipo devido a uma característica chamada **inferência de tipos**.

```kotlin
val age: Int = 25          // Tipagem explícita, ou seja, o programador diz qual deve ser o tipo
val name = "John"          // Inferência de tipo, feita automaticamente com base no valor atribuído na inicialização (String)
```

Em termos de operadores matemáticos, nada foge dos conhecidos símbolos. Além destes, existem operadores de incremento e decremento pré e pós-fixados (`++` e `--`).

| **Operador** | **Descrição**             | **Exemplo** | **Resultado** |
| ------------ | ------------------------- | ----------- | ------------- |
| `+`          | Adição                    | `5 + 3`     | `8`           |
| `-`          | Subtração                 | `5 - 3`     | `2`           |
| `*`          | Multiplicação             | `5 * 3`     | `15`          |
| `/`          | Divisão                   | `5 / 2`     | `2` (Inteiro) |
| `%`          | Módulo (resto da divisão) | `5 % 2`     | `1`           |


Uma característica importante da linguagem chama-se `null safety`. Trata-se de um recurso que permite ao **compilador** antecipar e evitar problemas relacionados ao acesso de valores e métodos em variáveis nulas (comuns no Java, por exemplo). Essa característica é implementada por meio de um sistema de tipos que diferencia variáveis que podem ser nulas daquelas que não podem. Assim, o compilador pode detectar possíveis erros de `NullPointerException` em tempo de compilação, aumentando a segurança e a robustez do código.

Quatro operadores são utilizados especificamente para o recurso de `null safety`, além do símbolo de `?` junto ao tipo. Quando se deseja declarar uma variável que pode receber valores nulos, acrescenta-se `?` ao nome do tipo. A seguir, há exemplos.


```kotlin
    var nome: String? = null //a variável aceita nulo
    var idade: Int = 0 // a variável não aceita nulo
```

Os operadores especificamente associados com `null safety` são:

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
    val num: Int? = valor as? Int        // Retorna null, pois a conversão não é possível

```

### Funções de escopo (scope functions)

As *scope functions* ajudam a escrever código mais legível ao executar um bloco de código “no contexto” de um objeto. Em geral, elas variam em dois aspectos:

- **Como o objeto é referenciado dentro do bloco**: como `it` (parâmetro implícito) ou como `this` (receptor do bloco).
- **O que a função retorna**: o próprio objeto (útil para encadear) ou o resultado do bloco (útil para calcular/transformar valores).

A seguir, há um resumo das funções mais comuns e situações típicas de uso.

#### `let`

`let` disponibiliza o objeto como `it` e retorna o **resultado do bloco**. Ela é muito usada para trabalhar com valores nulos de forma segura, combinando com `?.`.

```kotlin
val nome: String? = "Kotlin"

val tamanho: Int = nome?.let { it.length } ?: 0
println(tamanho)
```

#### `run`

`run` disponibiliza o objeto como `this` e retorna o **resultado do bloco**. É útil quando se deseja executar várias operações no mesmo objeto e produzir um valor final.

```kotlin
data class Usuario(val nome: String, val idade: Int)

val usuario = Usuario("Ana", 20)
val mensagem = usuario.run {
    "$nome tem $idade anos"
}
println(mensagem)
```

#### `apply`

`apply` disponibiliza o objeto como `this` e retorna o **próprio objeto**. É comum para inicialização e configuração de objetos, pois permite encadear a criação com a configuração.

```kotlin
class ContaBancaria {
    var saldo: Double = 0.0
}

val conta = ContaBancaria().apply {
    saldo = 100.0
}
println(conta.saldo)
```

#### `also`

`also` disponibiliza o objeto como `it` e retorna o **próprio objeto**. É útil para ações colaterais, como logs e depuração, sem alterar o fluxo do encadeamento.

```kotlin
val numeros = listOf(1, 2, 3)
    .also { println("Lista original: $it") }
    .map { it * 2 }
    .also { println("Lista dobrada: $it") }
```

#### `with`

`with` é uma função que recebe o objeto como argumento e disponibiliza-o como `this` dentro do bloco, retornando o **resultado do bloco**. Ela é útil quando não há interesse em encadear chamadas, apenas agrupar operações no mesmo objeto.

```kotlin
data class Produto(val nome: String, val preco: Double)

val produto = Produto("Café", 12.5)
val descricao = with(produto) {
    "$nome custa R$ $preco"
}
println(descricao)
```



### Tipos de dados básicos

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

## Strings e Templates

Kotlin oferece interpolação de strings com `$variavel` e `${expressao}`. Também existem *raw strings* com `"""` para textos longos.

```kotlin
val nome = "Ada"
val idade = 30
println("$nome tem $idade anos")
println("${nome.uppercase()}")

val texto = """
Linha 1
Linha 2
""".trimIndent()
```

## Coleções e Operações Comuns

As coleções mais usadas são `List`, `Set` e `Map`. Existem funções prontas para filtrar, mapear e ordenar dados.

```kotlin
val numeros = listOf(1, 2, 3, 4, 5)
val pares = numeros.filter { it % 2 == 0 }
val dobrados = numeros.map { it * 2 }

val nomes = listOf("Ana", "Bia", "Carlos")
nomes.forEach { println(it) }
```

## Tratamento de Erros

Kotlin usa `try/catch` e exceções como em Java. Também é possível usar `try` como expressão.

```kotlin
fun dividir(a: Int, b: Int): Int {
    return try {
        a / b
    } catch (e: ArithmeticException) {
        0
    }
}
```

---




## Controle de Fluxo

No que diz respeito a estruturas condicionais, o Kotlin utiliza `if` e `when`. A sintaxe do  `if` é semelhante a muitas outras linguagens, mas se destaca pela possibilidade de retornar valores, tal qual ocorre com o `when`. Este último, por sua vez, é um comando mais sofisticado, apresentando diversas variações.

```kotlin
    val numero = 10

    // Usando if-else
    val resultado = if (numero % 2 == 0) "Par" else "Ímpar"

    // Usando when (substituto do switch)
    val x = 6
    val feedback = when (x) {
        0 -> "Zero" // quando exatamente zero
        in 1..4 -> "Quatro ou menos" // quando entre 1 e 4
        5, 6, 7 -> "De cinco a sete" // se 5, 6 ou 7
        else -> "Outro número" // caso nenhuma das opções
    }
    println(feedback)
```

Os operadores lógicos mais comuns da linguagem são:

```kotlin
val x = 10
val y = -5

val eLogico = (x > 0) && (y > 0)
val ouLogico = (x > 0) || (y > 0)
val naoLogico = !(x > 0)
val ouExclusivo = (x > 0) xor (y > 0)
```



## Laços de Repetição

Os laços de repetição disponíveis são `for`, `while` e `do-while`, assim como em outras linguagens de programação. O laço `for` também permite percorrer coleções de dados de forma simplificada, tornando o código mais sucinto.


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

### Parâmetros nomeados e valores default

Kotlin permite valores padrão e chamada com parâmetros nomeados, deixando o código mais claro.

```kotlin
fun criarUsuario(nome: String, ativo: Boolean = true) {
    println("$nome - ativo: $ativo")
}

criarUsuario("Ana")
criarUsuario(nome = "Bia", ativo = false)
```

### Funções de extensão

Funções de extensão permitem adicionar comportamento a tipos existentes sem herança.

```kotlin
fun String.saudar(): String = "Olá, $this"

println("Kotlin".saudar())
```

### Funções lambdas

Funções lambda são funções anônimas (sem nome) que podem ser armazenadas em variáveis e passadas como argumento para outras funções. Elas são muito utilizadas para programação funcional e manipulação de coleções. Para criar uma variável que armazena uma função lambda, é necessário declarar algo nos moldes de `val nomeDaLambda: (TipoDoParametro) -> TipoDeRetorno = { parametro -> expressão }`. O mesmo vale para declarar parâmetros que aceitam tais funções (neste caso, a implementação da função depois do `=` é opcional).

Quando uma lambda tem apenas um parâmetro, é possível usar `it` para referenciá-lo implicitamente no código. Trata-se de uma convenção da linguagem.

```kotlin
val saudacao: (String) -> String = { "Olá, $it!" }
println(saudacao("Kotlin"))
```

Outro recurso interessante aplica-se quando uma função recebe uma lambda como seu último argumento. Nessa situação, é possível colocá-la fora dos parênteses da chamada da função utilizando uma sintaxe alternativa conhecida como `Trailing Lambda Syntax (Sintaxe de Lambda no Final)`.


```kotlin

fun calcular(a: Int, b: Int, operacao: (Int, Int) -> Int): Int {
    return operacao(a, b)
}

fun main() {
    // forma convencional
    val resultado = calcular(5, 3, { x, y -> x + y })
    println(resultado) 

    // trailing lambda syntax
    val resultado2 = calcular(5, 3) { x, y -> x + y }
    println(resultado2) 

}

```






## Orientação a Objetos

A **Programação Orientada a Objetos (POO)** é um paradigma de programação baseado no conceito de objetos, que encapsulam **dados (atributos)** e **comportamentos (métodos)**. Esses objetos representam entidades do mundo real ou do domínio do problema, permitindo modelar o software de forma mais próxima da realidade. A POO valoriza princípios como **encapsulamento** (proteger o estado interno), **abstração** (focar no essencial), **herança** (reaproveitar características) e **polimorfismo** (tratar objetos diferentes por uma interface comum), o que contribui para código mais organizado e mais fácil de manter. Kotlin é uma linguagem que suporta POO e oferece recursos úteis para facilitar o desenvolvimento de software.




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

### Visibilidade, herança e interfaces

Kotlin oferece modificadores de visibilidade: `public`, `private`, `protected` e `internal`. Para herança, a classe deve ser marcada como `open` (o padrão é `final`). Interfaces definem contratos.

```kotlin
open class Animal {
    protected var energia: Int = 100
}

interface Nadador {
    fun nadar()
}

class Pato : Animal(), Nadador {
    override fun nadar() {
        energia -= 10
        println("Pato nadando")
    }
}
```

### Construtores

Construtores são responsáveis por definir o estado inicial dos objetos. No Kotlin, existem **construtores primários** e **secundários**.

O construtor **primário** fica na declaração da classe e é usado quando os dados necessários são conhecidos no momento da criação do objeto. Ele permite inicializar propriedades diretamente e executar lógica adicional no bloco `init`.

Os construtores **secundários** ficam dentro da classe, com a palavra-chave `constructor`, e servem como formas alternativas de inicialização. Eles sempre delegam para o construtor primário usando `this(...)`.

```kotlin
// Construtor primário: dados essenciais na criação do objeto
class Produto(val nome: String, val preco: Double = 0.0) {
    init {
        println("Produto criado: $nome")
    }
}

fun main() {
    val p1 = Produto("Café", 12.5)
    val p2 = Produto("Água")
}
```

```kotlin
// Construtores secundários: formas alternativas de criar o mesmo objeto
class Usuario(val nome: String, val email: String) {
    var idade: Int? = null

    constructor(nome: String) : this(nome, "sem-email@exemplo.com")

    constructor(nome: String, idade: Int) : this(nome, "sem-email@exemplo.com") {
        this.idade = idade
    }
}

fun main() {
    val u1 = Usuario("Ana", "ana@exemplo.com")
    val u2 = Usuario("Bia")
    val u3 = Usuario("Caio", 20)
}
```

### Acessores e modificadores (getters e setters)

Em Kotlin, **propriedades** já possuem **getter** e **setter** gerados automaticamente. Para uma propriedade `val`, apenas o getter é criado (somente leitura). Para `var`, o getter e o setter são criados (leitura e escrita). Ao personalizar o acesso, o identificador `field` referencia o **backing field** (o valor armazenado internamente) daquela propriedade.

```kotlin
class ContaBancaria {
    var saldo: Double = 0.0
        set(value) {
            if (value >= 0) {
                field = value
            }
        }
}

fun main() {
    val conta = ContaBancaria()
    conta.saldo = 150.0
    conta.saldo = -50.0
    println(conta.saldo)
}
```

```kotlin
class Pessoa(val nome: String) {
    var idade: Int = 0
        private set
}

fun main() {
    val pessoa = Pessoa("Lia")
    // pessoa.idade = 30  // não permitido fora da classe
    println(pessoa.idade)
}
```





### Data Class

*Data classes* são usadas para representar **modelos de dados** de forma simples e objetiva. O compilador gera automaticamente métodos que seriam repetitivos de escrever manualmente, como `equals`, `hashCode`, `toString`, `componentN` (para *destructuring*) e `copy`. Para criar uma `data class`, basta declarar o nome e os atributos no construtor primário.

Principais funcionalidades:

- **Comparação por valor**: `equals` e `hashCode` usam os atributos do construtor primário.
- **Representação legível**: `toString` mostra o conteúdo do objeto.
- **Destructuring**: permite extrair atributos em variáveis.
- **Copy**: cria uma nova instância com algumas alterações.

```kotlin
data class Usuario(val nome: String, val idade: Int)

fun main() {
    val usuario1 = Usuario("Carlos", 28)
    val usuario2 = Usuario("Carlos", 28)

    println(usuario1 == usuario2)
    println(usuario1)
}
```

```kotlin
data class Usuario(val nome: String, val idade: Int)

fun main() {
    val usuario1 = Usuario("Carlos", 28)
    val usuario2 = usuario1.copy(idade = 30)

    val (nome, idade) = usuario2
    println("$nome - $idade")
}
```