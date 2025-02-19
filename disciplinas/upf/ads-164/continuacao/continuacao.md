
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

