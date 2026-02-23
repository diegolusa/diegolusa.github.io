---
title: "Jetpack Compose"
tags:
 - Programação
 - Plataforma
 - Android
 - Jetpack Compose
date: 2024-02-26 08:00:00
---



## Jetpack Compose

O **Jetpack Compose** é o **kit de ferramentas para a criação de interfaces de usuário (UI)** no Android. Ele substitui o XML tradicional por uma abordagem declarativa, onde a interface é criada por meio de funções Kotlin anotadas com `@Composable`.

Os objetivos principais de aplicação do **Compose** podem ser resumidos a:

- Criar interfaces de forma mais concisa e intuitiva.
- Reutilizar componentes facilmente.
- Tornar a interface reativa, atualizando automaticamente conforme os estados mudam.
- Integrar padrões modernos como **Material Design 3**.

O uso de Jetpack Compose requer configurações específicas no projeto. Contudo, nas versões mais recentes do Android Studio, essas configurações tendem a ser automatizadas pelos templates.

De qualquer modo, é importante saber o que é necessário para utilizar os recursos de composição no projeto. Uma forma comum de gerenciar versões é utilizar o **Compose BOM**, evitando inconsistências entre bibliotecas Compose.

```kotlin
android {
    buildFeatures {
        compose = true
    }
}

dependencies {
    val composeBom = platform("androidx.compose:compose-bom:2024.02.00")
    implementation(composeBom)
    androidTestImplementation(composeBom)

    implementation("androidx.activity:activity-compose:1.8.2")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-tooling-preview")
    debugImplementation("androidx.compose.ui:ui-tooling")
}
```


Após essa configuração, já é possível criar Activities aplicando funções de composição para construir as interfaces. Isso é abordado a seguir.

### Criando Telas


No **Jetpack Compose**, a interface é definida por funções `@Composable`, as quais declaram como a UI deve ser exibida para um determinado estado. O trecho a seguir apresenta uma Activity simples chamando uma função `@Composable` para construir a tela.


```kotlin
package com.exemplo.composeapp

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MeuApp()
        }
    }
}

@Composable
fun MeuApp() {
    MaterialTheme {
        TelaInicial()
    }
}

@Composable
fun TelaInicial() {
    val contexto = LocalContext.current
    
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Olá, Jetpack Compose!", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = {
            Toast.makeText(contexto, "Botão clicado!", Toast.LENGTH_SHORT).show()
        }) {
            Text("Clique Aqui")
        }
    }
}
```

No código acima, a construção da tela inicia a partir da função `setContent`. A função `MeuApp()` aplica um tema e delega a construção da interface para `TelaInicial()`.

Quando se trabalha com Jetpack Compose, utiliza-se um conjunto de componentes (como `Text`, `Button`, `Column`) e funções `@Composable` próprias (componentes reutilizáveis) para compor a interface. Um ponto importante é que a UI pode ser **recomposta** automaticamente quando o estado muda.

#### Composição e recomposição

Uma forma prática de entender Compose é considerar que:

- **Composição**: primeira montagem da UI.
- **Recomposição**: reexecução de funções `@Composable` afetadas por mudanças de estado.

Por isso, recomenda-se evitar efeitos colaterais diretos durante a composição (por exemplo, iniciar requisições de rede em cada recomposição). Para efeitos controlados, utilizam-se APIs como `LaunchedEffect`.

 
### Context

No Android, o **Context** é uma classe essencial que fornece acesso a recursos globais da aplicação, como arquivos, bancos de dados, serviços do sistema, preferências compartilhadas e a interface gráfica. Ele é fundamental para muitas operações no desenvolvimento de aplicativos.


Normalmente o *context* é usado para:

- Acessar recursos (strings, cores, dimensões, imagens, etc.).
- Gerenciar arquivos e banco de dados internos.
- Criar e iniciar Intents para abrir telas ou serviços.
- Exibir Toasts e Dialogs.
- Obter serviços do sistema (como ClipboardManager, Vibrator, WifiManager, etc.).


Existem diferentes formas de obter um Context, dependendo do escopo onde ele será usado. Na tabela a seguir colocamos um resumo de tais opções.



| Tipo de Context     | Descrição                                                              | Como obter                    |
| ------------------- | ---------------------------------------------------------------------- | ----------------------------- |
| Activity Context    | Contexto específico da Activity. É destruído junto com a Activity.     | `this` dentro de uma Activity |
| Application Context | Contexto global da aplicação. Vive enquanto o app estiver em execução. | `applicationContext`          |
| Service Context     | Contexto dentro de um Service.                                         | `this` dentro de um Service   |
| Compose Context     | Contexto acessado dentro de uma função `@Composable`.                  | `LocalContext.current`        |


Para operações que precisam sobreviver ao ciclo de vida de uma Activity (por exemplo, inicialização de bibliotecas globais), costuma-se usar o `applicationContext`. Ainda assim, ações de UI (como abrir telas e exibir diálogos) normalmente requerem um contexto associado a uma tela.




!!! Note "Exemplos de uso"
    === "Exibição de Toasts"
        ```kotlin
            val contexto = LocalContext.current
            Toast.makeText(contexto, "Olá, Jetpack Compose!", Toast.LENGTH_SHORT).show()
        ```
    === "Acesso à resources"
        ```kotlin
            val corPrimaria = ContextCompat.getColor(this, R.color.primary)
            val texto = getString(R.string.app_name)
        ```
    === "Iniciar Activity"
        ```kotlin
            val contexto = LocalContext.current
            val intent = Intent(contexto, NovaActivity::class.java)
            contexto.startActivity(intent)
        ```

    === "SharedPreferences"
        ```kotlin
            val contexto = LocalContext.current
            val sharedPref = contexto.getSharedPreferences("config", Context.MODE_PRIVATE)
            sharedPref.edit().putString("user", "João").apply()
        ```


### Unidades de Medida

No Jetpack Compose, as unidades mais comuns para definir dimensões e tipografia são `dp` e `sp`. Para alguns casos tipográficos, existe também `em` (relativo ao tamanho da fonte). Já dimensões relativas à tela normalmente são representadas por **frações** (por exemplo, `fillMaxWidth(0.5f)` ocupa metade da largura disponível).

!!! info "Unidades de Medida"
    === "dp (Density-independent Pixels)"

        O dp (dip - density-independent pixel) é a unidade principal para dimensões de layouts, garantindo que a interface seja escalável em diferentes tamanhos de tela e densidades de pixel.

        ```kotlin

        Modifier.padding(16.dp)
        Modifier.width(200.dp) 

        ```
        O dp é recomendado para largura, altura, margens e espaçamentos.

    === "sp (Scale-independent Pixels)"

        O sp (scale-independent pixel) é usado para tamanho de texto, garantindo que ele respeite as preferências do usuário em relação ao tamanho da fonte.

        ```kotlin

        Text("Texto em 20sp", fontSize = 20.sp)
        ```
 
 
    === "em (Relativo ao texto)"

        Essa unidade é usada para dimensionar atributos tipográficos com base no tamanho da fonte.

        - **1em** = tamanho atual da fonte.

        ```kotlin

        Text("Texto", letterSpacing = 0.1.em)
        ```
    === "Dimensões relativas (frações)"

        `Modifier.fillMaxWidth()` e `Modifier.fillMaxHeight()` podem receber uma fração (`0f` a `1f`) para definir dimensões relativas ao espaço disponível.

        ```kotlin
            Modifier.fillMaxWidth(0.5f) // Ocupa 50% da largura
            Modifier.fillMaxHeight(0.75f) // Ocupa 75% da altura
        ```






### Gerenciamento de Estados


A UI (User Interface) no Compose é **reativa**, ou seja, ela muda automaticamente quando um **estado** muda. Por **estado** entendemos qualquer valor que muda ao longo do tempo. Sempre que um estado muda, os componentes que o utilizam são automaticamente atualizados.

O exemplo a seguir utiliza um contador para ilustrar o conceito de estado:

```kotlin
@Composable
fun Contador() {
    var contador by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Contador: $contador", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = { contador++ }) {
            Text("Incrementar")
        }
    }
}
```

A manutenção de estado é realizada de forma conjunta pelas funções `mutableStateOf` e `remember`. O uso de `remember` garante que o valor seja armazenado na memória durante a composição da interface e preservado durante recomposições. Já `mutableStateOf` cria um estado observável: quando o valor muda, a UI que o lê é automaticamente atualizada. Além do `remember`, existe `rememberSaveable`, que persiste o estado mesmo após mudanças de configuração (como rotação da tela).

Um padrão importante é o **state hoisting**: quando um componente recebe o valor do estado e callbacks para alterá-lo, em vez de manter estado internamente. Isso facilita reuso e testes.

```kotlin
@Composable
fun Contador(valor: Int, onIncrementar: () -> Unit) {
    Column {
        Text("Contador: $valor")
        Button(onClick = onIncrementar) { Text("Incrementar") }
    }
}

@Composable
fun TelaContador() {
    var contador by remember { mutableStateOf(0) }
    Contador(valor = contador, onIncrementar = { contador++ })
}
```

A função `mutableStateOf` não é a única do seu tipo. A tabela a seguir resume algumas opções.

| Função               | O que faz?                               | Quando usar?                                     |
| -------------------- | ---------------------------------------- | ------------------------------------------------ |
| `mutableStateOf`     | Cria um estado simples reativo.          | Para variáveis comuns que mudam na UI.           |
| `mutableStateListOf` | Estado reativo para listas.              | Quando a UI precisa reagir a mudanças em listas. |
| `mutableStateMapOf`  | Estado reativo para mapas.               | Quando a UI precisa reagir a mudanças em mapas.  |
| `produceState`       | Estado baseado em operações assíncronas. | Para chamadas de API e carregamento de dados.    |
| `derivedStateOf`     | Cria um estado derivado de outro.        | Para evitar recomposições desnecessárias.        |


Outra forma de gerenciar estados é através de **ViewModel**, um componente do Android Jetpack que ajuda a preservar dados ao longo do ciclo de vida de uma Activity ou Fragment, incluindo mudanças de configuração. Em aplicações reais, é comum manter o estado no ViewModel e expô-lo para a UI como `State` ou `StateFlow`.

A criação de um ViewModel é feita através da criação de uma classe derivada de `androidx.lifecycle.ViewModel`. 

```kotlin
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

class ContadorViewModel : ViewModel() {
    var contador by mutableStateOf(0)
        private set

    fun incrementar() {
        contador++
    }
}
```


### Navegação

Navegação é o recurso que permite alternar entre diferentes telas de um aplicativo. Quando se desenvolve um app com Jetpack Compose, a navegação pode crescer rapidamente à medida que novas telas são adicionadas. Para manter o código organizado, reutilizável e modular, é recomendado separar a navegação da definição das telas.


A estrutura do código é importante para manter a organização do projeto, permitindo que ele evolua ao longo do tempo mantendo a complexidade sob controle. Uma sugestão é a estrutura abaixo, onde as telas ficam em um pacote chamado `ui.screens`, separadas da navegação e do código das Activities.

```text
📂 app/src/main/java/com/exemplo/app
 ┣ 📂 ui
 ┃ ┣ 📂 screens
 ┃ ┃ ┣ 📜 HomeScreen.kt
 ┃ ┃ ┣ 📜 ProfileScreen.kt
 ┃ ┃ ┣ 📜 SettingsScreen.kt
 ┃ ┃ ┣ 📜 DetailScreen.kt
 ┃ ┣ 📜 Navigation.kt   
 ┃ ┣ 📜 App.kt
 ┣ 📂 data
 ┃ ┣ 📜 Repository.kt
 ┣ 📜 MainActivity.kt
```

Outro ponto importante é configurar a navegação de modo a deixá-la contida em um componente específico, a ser utilizado pelos demais para determinar as rotas. No que se refere à operação, as rotas são `strings` que se associam a uma determinada função de composição. Isso se assemelha ao funcionamento das URLs no protocolo HTTP.



- **Definição das strings de roteamento**


As strings de roteamento são *paths* cuja função é identificar a tela a ser carregada quando uma rota é solicitada. No exemplo a seguir, uma `sealed class` abstrai as rotas. Cada rota é representada por um objeto que deriva da classe `AppScreens`. Desse modo, evitam-se erros de digitação e facilita-se a criação de rotas com parâmetros, como `detalhe/{itemId}`.



```kotlin
sealed class AppScreens(val route: String) {
    object Home : AppScreens("home")
    object Profile : AppScreens("perfil")
    object Settings : AppScreens("configuracao")
    object Detail : AppScreens("detalhe/{itemId}") {
        fun createRoute(itemId: Int) = "detalhe/$itemId"
    }
}
```

!!! info "Sealed Class"

    Sealed classes possuem todas as extensões conhecidas em tempo de compilação. Além disso, suas extensões precisam se manter no pacote em que a `sealed class` foi criada. Por definição, uma `sealed class` é abstrata, o que impede criar instâncias diretamente dela. Uma das grandes vantagens de tais classes é a possibilidade de utilizar objetos das mesmas no comando `when` sem a necessidade de utilizar `else`. Ainda, é preciso considerar a segurança de que não haverão classes derivadas desconhecidas, o que pode ser interessante em alguns cenários.



Agora que as rotas estão representadas, o passo seguinte é associá-las às respectivas funções `@Composable`. Para isso, utiliza-se `NavController` e `NavHost`.

```kotlin
import androidx.compose.runtime.Composable
import androidx.navigation.compose.composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import androidx.navigation.NavType

@Composable
fun AppNavigation() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = AppScreens.Home.route) {
        composable(AppScreens.Home.route) { HomeScreen(navController) }
        composable(AppScreens.Profile.route) { ProfileScreen(navController) }
        composable(AppScreens.Settings.route) { SettingsScreen(navController) }
        composable(
            route = AppScreens.Detail.route,
            arguments = listOf(navArgument("itemId") { type = NavType.IntType })
        ) { backStackEntry ->
            val itemId = backStackEntry.arguments?.getInt("itemId")
            if (itemId != null) {
                DetailScreen(navController, itemId)
            }
        }
    }
}
```

Nota-se que a função `composable` recebe a string que representa a rota. Contudo, em vez de informar um valor literal, utilizam-se objetos criados a partir da `sealed class` criada anteriormente.

!!! note "Scope Functions"
    Em exemplos de navegação, é comum observar o uso de *scope functions* como `let`, `apply`, `run`, `also` e `with` para trabalhar com valores nulos e encadear operações. A [documentação oficial do Kotlin](https://kotlinlang.org/docs/scope-functions.html) detalha essas funções.


Cada rota chama uma função de composição específica, responsável por construir a tela. Neste exemplo, um objeto `NavController` é passado para essas funções, a fim de habilitar o roteamento a partir de eventos internos (como o clique de um botão).


```kotlin
import androidx.compose.runtime.Composable
import androidx.navigation.NavController
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*

@Composable
fun HomeScreen(navController: NavController) {
    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Text(text = "Tela Inicial", style = MaterialTheme.typography.headlineMedium)
        Button(onClick = { navController.navigate(AppScreens.Profile.route) }) {
            Text("Ir para Perfil")
        }
        Button(onClick = { navController.navigate(AppScreens.Settings.route) }) {
            Text("Ir para Configurações")
        }
        Button(onClick = { navController.navigate(AppScreens.Detail.createRoute(42)) }) {
            Text("Ver Detalhes do Item 42")
        }
    }
}

@Composable
fun DetailScreen(navController: NavController, itemId: Int) {
    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Text(text = "Detalhes do Item $itemId", style = MaterialTheme.typography.headlineMedium)
        Button(onClick = { navController.popBackStack() }) {
            Text("Voltar")
        }
    }
}

```

Para visualizar o fluxo de forma mais concreta, o diagrama abaixo representa uma navegação simples:

```mermaid
flowchart LR
    Home[HomeScreen] --> Profile[ProfileScreen]
    Home --> Settings[SettingsScreen]
    Home --> Detail[DetailScreen (itemId)]
    Detail --> Home
```


Por fim, a interface é inicializada a partir de uma Activity. Neste caso, na Activity marcada como `launcher` adiciona-se uma `lambda` à função `setContent`, chamando a função de composição principal. Na função `App`, chama-se `AppNavigation`, que inicializa a rota inicial e a sua respectiva tela.


```kotlin
@Composable
fun App() {
    MaterialTheme {
        AppNavigation()
    }
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { App() }
    }
}

```
