
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

| **Operador** | **Descrição**           | **Exemplo**        | **Resultado** |
|--------------|-------------------------|--------------------|---------------|
| `+`          | Adição                  | `5 + 3`            | `8`           |
| `-`          | Subtração               | `5 - 3`            | `2`           |
| `*`          | Multiplicação           | `5 * 3`            | `15`          |
| `/`          | Divisão                 | `5 / 2`            | `2` (Inteiro) |
| `%`          | Módulo (resto da divisão) | `5 % 2`          | `1`           |


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





## Estruturas Condicionais

O Kotlin utiliza if e when para controle de fluxo.

val number = 10

// Usando if-else
val result = if (number % 2 == 0) "Par" else "Ímpar"

// Usando when (substituto do switch)
val grade = "A"
val feedback = when (grade) {
    "A" -> "Excelente"
    "B" -> "Bom"
    "C" -> "Satisfatório"
    else -> "Nota inválida"
}

## Laços de Repetição

Kotlin oferece laços como for, while e do-while.

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

## Funções

Funções em Kotlin podem ser declaradas de forma simples e suportam valores de retorno.

fun add(a: Int, b: Int): Int {
    return a + b
}

// Função de linha única
fun multiply(a: Int, b: Int) = a * b

println(add(3, 5))       // 8
println(multiply(4, 7))  // 28

Classes e Objetos

A orientação a objetos no Kotlin é simples e eficiente.

class Person(val name: String, var age: Int) {
    fun greet() = "Olá, meu nome é $name e tenho $age anos."
}

val person = Person("Alice", 30)
println(person.greet()) // Olá, meu nome é Alice e tenho 30 anos.

1. Principais Características do Kotlin

2. Null Safety

Evita erros de ponteiro nulo com tipos seguros.

var name: String? = null // Variável pode ser nula
println(name?.length)    // Safe call operator (?.)

2. Interoperabilidade com Java

Kotlin permite o uso de bibliotecas Java sem complicações.

val list = ArrayList<String>()
list.add("Kotlin")

3. Funções de Extensão

Adicione funcionalidades a classes existentes.

fun String.isPalindrome(): Boolean {
    return this == this.reversed()
}

println("level".isPalindrome()) // true

4. Data Classes

Simplifique a criação de classes para armazenar dados.

data class User(val name: String, val age: Int)

val user = User("Alice", 25)
println(user.name) // Alice

5. Expressões Lambda

Simplifique o uso de funções de ordem superior.

val numbers = listOf(1, 2, 3, 4)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6, 8]

6. Corrotinas

Gerencie operações assíncronas de forma eficiente.

import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)
        println("Corrotinas são incríveis!")
    }
    println("Olá,")
}

7. Delegação de Propriedades

Use delegados para simplificar a lógica de propriedades.

import kotlin.properties.Delegates

var observableValue: Int by Delegates.observable(0) { _, old, new ->
    println("Mudança de $old para $new")
}
observableValue = 10

8. Programação Funcional

Combine paradigmas orientados a objetos e funcionais.

val list = listOf(1, 2, 3, 4)
val evenNumbers = list.filter { it % 2 == 0 }
println(evenNumbers) // [2, 4]

3. Vantagens de Usar Kotlin no Android
	•	Menos Erros: Null safety reduz crashes.
	•	Alta Produtividade: Código mais conciso.
	•	Interoperabilidade: Suporte total a bibliotecas Java.
	•	Adotado pelo Google: Totalmente integrado ao Android Studio.

Referências
	•	Documentação Oficial do Kotlin
	•	Guia de Desenvolvimento Android

Este material cobre tanto a sintaxe básica quanto os recursos avançados do Kotlin, ajudando no aprendizado e na consulta durante o desenvolvimento mobile.

