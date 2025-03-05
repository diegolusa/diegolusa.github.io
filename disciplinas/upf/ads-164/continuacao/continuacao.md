
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


Os construtores definidos nas classes podem ser




1

4. Encapsulamento

Encapsulamento é o princípio que protege os dados dentro de uma classe. Em Kotlin, usamos modificadores de visibilidade:
	•	private: Acesso apenas dentro da própria classe.
	•	protected: Acesso dentro da classe e subclasses.
	•	internal: Visível dentro do mesmo módulo.
	•	public: Acesso de qualquer lugar (padrão).

Exemplo:

class ContaBancaria(private var saldo: Double) {
    fun depositar(valor: Double) {
        saldo += valor
        println("Depósito realizado! Saldo atual: R$ $saldo")
    }

    fun sacar(valor: Double) {
        if (valor <= saldo) {
            saldo -= valor
            println("Saque realizado! Saldo atual: R$ $saldo")
        } else {
            println("Saldo insuficiente!")
        }
    }
}

fun main() {
    val conta = ContaBancaria(1000.0)
    conta.depositar(500.0)
    conta.sacar(200.0)
}

5. Herança

A herança permite que uma classe herde características de outra classe.

Criando uma Superclasse

open class Animal(val nome: String) {
    fun dormir() {
        println("$nome está dormindo...")
    }
}

Criando uma Subclasse

A subclasse herda da superclasse usando :.

class Cachorro(nome: String, val raca: String) : Animal(nome) {
    fun latir() {
        println("$nome está latindo!")
    }
}

fun main() {
    val meuCachorro = Cachorro("Rex", "Labrador")
    meuCachorro.dormir()
    meuCachorro.latir()
}

Saída:

Rex está dormindo...
Rex está latindo!

6. Polimorfismo

O polimorfismo permite que um método tenha diferentes comportamentos dependendo do tipo do objeto.

Sobrescrita de Métodos

Podemos sobrescrever métodos da superclasse usando override.

open class Forma {
    open fun desenhar() {
        println("Desenhando uma forma genérica.")
    }
}

class Circulo : Forma() {
    override fun desenhar() {
        println("Desenhando um círculo.")
    }
}

fun main() {
    val formas: List<Forma> = listOf(Forma(), Circulo())
    for (forma in formas) {
        forma.desenhar()
    }
}

Saída:

Desenhando uma forma genérica.
Desenhando um círculo.

7. Classes e Métodos Abstratos

Classes abstratas não podem ser instanciadas diretamente e servem como modelos para outras classes.

abstract class Veiculo(val nome: String) {
    abstract fun mover()
}

class Carro(nome: String) : Veiculo(nome) {
    override fun mover() {
        println("$nome está se movendo sobre rodas.")
    }
}

fun main() {
    val carro = Carro("Fusca")
    carro.mover()
}

8. Interfaces

Interfaces definem contratos que outras classes devem seguir.

interface Trabalhavel {
    fun trabalhar()
}

class Engenheiro : Trabalhavel {
    override fun trabalhar() {
        println("Projetando um edifício.")
    }
}

fun main() {
    val trabalhador: Trabalhavel = Engenheiro()
    trabalhador.trabalhar()
}




