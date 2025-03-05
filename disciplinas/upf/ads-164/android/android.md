---
title: "Desenvolvimento de aplicativos para Android"
tags:
 - Programação
 - Plataforma
 - Android
date: 2024-02-26 08:00:00
---



---

## Jetpack Compose

O **Jetpack Compose** é o **kit de ferramentas para a criação de interfaces de usuário (UI)** no Android. Ele substitui o XML tradicional por uma abordagem declarativa, onde a interface é criada por meio de funções Kotlin anotadas com `@Composable`.

Os objetivos principais de aplicação do **Compose** podem ser resumidos a:

- Criar interfaces de forma mais concisa e intuitiva.
- Reutilizar componentes facilmente.
- Tornar a interface reativa, atualizando automaticamente conforme os estados mudam.
- Integrar padrões modernos como **Material Design 3**.

O uso de Jetpack Compose no desenvolvimento requer configurações específicas no projeto. Contudo, nas versões mais recentes do Android Studio tais configurações acabam sendo transparentes. 

De qualquer modo, é importante saber o que é necessário para utilizar os recursos de composição no projeto. Além de ter a versão do Android Studio mais atualizada, precisamos verificar se as dependências `androidx.compose.ui` e `androidx.compose.material3` estão presentes no arquivo `build.gradle.kts` na seção `dependencies`:

```kotlin

plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    compileSdk = 34

    defaultConfig {
        applicationId = "com.exemplo.composeapp"
        minSdk = 21
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }

    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.6.0"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    implementation("androidx.activity:activity-compose:1.8.2")
    implementation("androidx.compose.ui:ui:1.6.0")
    implementation("androidx.compose.material3:material3:1.2.0")
}


```



Feito isso, já é possível criar nossas activities aplicando funções de composição para criação das interfaces. É o que abordaremos a seguir.

### Criando Telas


No **Jetpack Compose**, a interface é definida por funções `@Composable`, as quais definem e integram as partes da interface gráfica. É o que demonstra o trecho de código a seguir, que apresentam uma `activity` simples utilizando `Composable` para criar a estrutura da tela.


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

No código acima, a construção da tela inicia a partir da função `setContent`. Observe que é realizado chamada para a função `MeuApp`, que possui anotação `@Composable`. Esta, por sua vez, utiliza a função `TelaInicial` para adicionar um texto e um botão à tela.

Quanto trabalhamos com Jetpack Compose, utilizamos as funções oferecidas pelo pacote para adicionar elementos básicos na tela (texto, campos de entrada, listas). E, para realizar a construção da tela, utilizamos funções anotadas com `@Compose` customizadas.

 
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
| Activity Context    | Contexto específico da Activity. Ele é destruído junto com a Activity. | `this` dentro de uma Activity |
| Application Context | Contexto global da aplicação. Vive enquanto o app estiver rodando.     | `applicationContext`          |
| Service Context     | Contexto dentro de um Service, usado para tarefas em background.       | `this` dentro de um Service   |
| Base Context        | Contexto que pode ser reutilizado ou modificado.                       |                               |


Para manter operações além do escopo de activities precisamos utilizar o `applicationContext`.




!!! Note "Exemplos de Uso"
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
            val sharedPref = getSharedPreferences("config", Context.MODE_PRIVATE)
            sharedPref.edit().putString("user", "João").apply()
        ```


### Unidades de Medida

No Jetpack Compose, usamos diferentes unidades para definir tamanhos, espaçamentos e dimensões da UI. As principais unidades são `dp`, `sp`, `em` e `%`. Vamos as detalhes de cada uma:

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
 
 
    === "em e ex (Relativos ao Texto)"

        Essas unidades são usadas para dimensionar elementos com base no tamanho da fonte.

        - **1em** = tamanho atual da fonte.
        - **1ex** = metade da altura da fonte.

        ```kotlin

        Text("Texto", letterSpacing = 0.1.em)
        ```
    === "percentual (%)"

        O Modifier.fillMaxWidth() e Modifier.fillMaxHeight() são usados para definir dimensões relativas ao tamanho da tela. Nestes métodos podemos atribuir valores percentuais, de modo a indicar uma porção do espaço relativo da tela.

        ```kotlin
            Modifier.fillMaxWidth(0.5f) // Ocupa 50% da largura
            Modifier.fillMaxHeight(0.75f) // Ocupa 75% da altura
        ```






### Gerenciamento de Estados


A UI (User Interface) no Compose é **reativa**, ou seja, ela muda automaticamente quando um **estado** muda. Por **estado** entendemos qualquer valor que muda ao longo do tempo. Sempre que um estado muda, os componentes que o utilizam são automaticamente atualizados.

Vamos utilizar um exemplo de um contador para ilustrar o conceito de estado. Observe o código:

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

A manutenção de estado é realizada de forma conjunta pelas funcões `mutableStateOf` e `remember`.  O uso de `remember` garante que o valor seja armazenado na memória durante a composição da interface e retornado durante a recomposição. Já `mutableStateOf` cria um objeto observável, cuja alteração é acompanhada pelos objetos da interface que o utilizam (ou seja, atualizam a tela quando o valor muda). Além do `remember`, temos o `rememberSaveable`, que persiste o estado mesmo após mudanças de configuração (girar a tela, por exemplo).

A função `mutableStateOf` não é a única do seu tipo. Veja a lista completa na tabela abaixo.

| Função               | O que faz?                               | Quando usar?                                     |
| -------------------- | ---------------------------------------- | ------------------------------------------------ |
| `mutableStateOf`     | Cria um estado simples reativo.          | Para variáveis comuns que mudam na UI.           |
| `mutableStateListOf` | Estado reativo para listas.              | Quando a UI precisa reagir a mudanças em listas. |
| `mutableStateMapOf`  | Estado reativo para mapas.               | Quando a UI precisa reagir a mudanças em mapas.  |
| `produceState`       | Estado baseado em operações assíncronas. | Para chamadas de API e carregamento de dados.    |
| `derivedStateOf`     | Cria um estado derivado de outro.        | Para evitar recomposições desnecessárias.        |


Outra forma de gerenciar estados é através de **ViewModel**, um componente da arquitetura do Android Jetpack que ajuda a gerenciar estados e preservar dados através do ciclo de vida de uma Activity ou Fragment. Ele evita a perda de dados ao longo de mudanças de configuração, como rotação da tela, por exemplo. No Jetpack Compose, o ViewModel é essencial para armazenar estados que precisam ser mantidos mesmo após recomposições.

A criação de um ViewModel é feita através da criação de uma classe derivada de `androidx.lifecycle.ViewModel`. 

```kotlin
import androidx.lifecycle.ViewModel
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class ContadorViewModel : ViewModel() {
    var contador by mutableStateOf(0)
        private set

    fun incrementar() {
        contador++
    }
}
```


### Navegação

Navegação é o recurso que permite alternar entre diferentes telas de um aplicativo. Quando desenvolvemos um app com Jetpack Compose, a navegação pode crescer rapidamente à medida que adicionamos novas telas. Para manter o código organizado, reutilizável e modular, é recomendado separar a navegação da definição das telas.


A estrutura do código é muito importante para manter a organização do projeto, que o permita evoluir ao longo do tempo mantendo a complexidade sob controle. Uma sugestão pode ser a estrutura abaixo, onde as telas ficam em um pacote chamado `ui.screens`, separadas da navegação e do código das activities.

<pre>
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
</pre>

Outro ponto importante é configurar a navegação de modo a deixá-la contida em um componente específico, a ser utilizado por todos os demais para determinar as rotas. No que se refere a operação, as rotas são `strings` que se associam a uma determinada função de composição. Assemelha-se com o funcionamento das URLs no protocolo HTTP. Observe a sequência de objetos  apresentados e observe como o sistema de rotas funciona.



- **Definição das strings de roteamento**


As strings de roteamento são paths cuja função é identificar a tela a ser carregada com a rota for solicitada. Aqui estamos criando uma `sealed class` para abstrair as rotas. Cada rota é representada por um objeto que deriva da classe `AppScreens`. Deste modo, evitamos erros de digitação e facilitamos a criação de rotas com parâmetros, como é o caso de `detalhe/{itemId}` no exemplo que segue.



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



Agora que criamos as representações de nossas rotas, o passo seguinte é definir a associação das rotas com as respectivas funções que geram as telas. Iremos utilizar os recursos `NavControler` e `NavHost`. Acompanhe o código.

```kotlin
import androidx.compose.runtime.Composable
import androidx.navigation.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument

@Composable
fun AppNavigation() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = AppScreens.Home.route) {
        composable(AppScreens.Home.route) { HomeScreen(navController) }
        composable(AppScreens.Profile.route) { ProfileScreen(navController) }
        composable(AppScreens.Settings.route) { SettingsScreen(navController) }
        composable(AppScreens.Detail.route, arguments = listOf(navArgument("itemId") { type = NavType.IntType })) {
            val itemId = it.arguments?.getString("itemId")?.toIntOrNull()
            itemId?.let { DetailScreen(navController, it) }
        }
    }
}
```

Perceba  que a função `composable` recebe a string que representa a rota. Contudo, não informamos um valor literal, mas utilizamos objetos criados a partir da `sealed class` criada anteriormente.

!!! note "Scope Functions"
    No código apresentando, você deve ter observado o comando `let` na instrução `itemId?.let { DetailScreen(navController, it) }`. Trata-se de uma scoped function, como `apply`, `run`, `also` e `with`. Acesse a [documentação oficial do Kotlin](https://kotlinlang.org/docs/scope-functions.html) para entender melhor o funcionamento das mesmas 


Cada rota chama uma função de composição específica, responsável por construir a tela para o usuário. Observe que estamos passando um objeto `NavController` para as mesmas, a fim de habilitar o roteamento a partir de eventos internos (como click de um botão, por exemplo).


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


E, por fim, precisamos inicializar nossa interface a partir de uma activity. Neste caso, na activity marcada como `launcher` adicionamos uma `lambda` à funcão `setContent` chamando a função de composição principal. Na função `App` chamamos `AppNavigation`, que por sua vez irá inicializar a rota inicial e sua respectiva tela.


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


## Activities



Uma **Activity** é um componente fundamental do desenvolvimento de aplicativos Android, representando uma única tela com uma interface de usuário. Elas são os blocos de construção principais com os quais os usuários interagem em um aplicativo Android. O ciclo de vida de uma Activity descreve como ela passa por diferentes estados, desde sua criação até sua destruição.

### Ciclo de Vida

O ciclo de vida de uma Activity é gerenciado pelo sistema operacional Android e é composto por uma série de estados, que são eventos que ocorrem durante a execução da Activity. Aqui estão os principais estados do ciclo de vida de uma Activity:

- **Created (Criado):** A Activity é criada, mas ainda não é visível ao usuário.
- **Started (Iniciado):** A Activity se torna visível ao usuário, mas ainda não está interagindo ativamente com ele.
- **Resumed (Resumido):** A Activity está em primeiro plano e está interagindo ativamente com o usuário.
- **Paused (Pausado):** A Activity perde o foco, mas ainda é visível ao usuário. Nesse estado, ela ainda está visível, mas não está interagindo ativamente com o usuário.
- **Stopped (Parado):** A Activity não está mais visível ao usuário e pode ser destruída pelo sistema se a memória estiver baixa.
- **Destroyed (Destruído):** A Activity é destruída e removida da memória.

![Ciclo de Vida de uma Activity](https://developer.android.com/guide/components/images/activity_lifecycle.png)

Cada estado do ciclo de vida é associado a métodos específicos que são chamados automaticamente pelo sistema operacional Android. Desta forma, o desenvolvedor pode executar instruções específicas para cada estado. Ao menos o estado `onCreate` apresenta implementação em todas as activities.

- `onCreate()`: Chamado quando a Activity está sendo criada.
- `onStart()`: Chamado quando a Activity está prestes a se tornar visível.
- `onResume()`: Chamado quando a Activity está em primeiro plano e interagindo com o usuário.
- `onPause()`: Chamado quando a Activity está prestes a perder o foco, geralmente quando outra Activity é iniciada.
- `onStop()`: Chamado quando a Activity não é mais visível ao usuário.
- `onDestroy()`: Chamado antes da Activity ser destruída.


```kotlin

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MinhaActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_minha)

        // Seu código de inicialização aqui
    }

    override fun onStart() {
        super.onStart()
        // A Activity está prestes a se tornar visível
    }

    override fun onResume() {
        super.onResume()
        //Está plano e interagindo com o usuário
    }

    override fun onPause() {
        super.onPause()
        // Está prestes a perder o foco
    }

    override fun onStop() {
        super.onStop()
        // Não é mais visível ao usuário
    }

    override fun onDestroy() {
        super.onDestroy()
        // Está prestes a ser destruída
    }
}
```


## Intents

Intents são uma parte essencial do desenvolvimento de aplicativos Android, assim como as activites. Permitem que os desenvolvedores criem interações entre diferentes componentes do sistema, como Activities, Services, Broadcast Receivers e Content Providers. Elas são uma forma flexível de realizar operações em um aplicativo Android, incluindo navegação entre telas, compartilhamento de dados, execução de ações específicas e muito mais.

Dentre as funcionalidades principais podemos citar:


- **Iniciar Componentes:** Uma das principais funcionalidades das *intents* é iniciar componentes do Android, como Activities, Services, Broadcast Receivers e Content Providers. 
   
- **Comunicar Dados:** As *intents* podem ser usadas para transmitir dados entre componentes do Android. Os desenvolvedores podem enviar dados, como strings, números, objetos Parcelable ou Serializable, e até mesmo arquivos, entre diferentes partes do aplicativo ou mesmo entre aplicativos diferentes.

- **Realizar Ações Explícitas e Implícitas:** As *intents* podem ser explícitas ou implícitas. Uma *intent* explícita especifica um componente de destino específico dentro do aplicativo usando o nome da classe. Por outro lado, uma *intent* implícita especifica uma ação geral e permite que o sistema Android escolha o componente apropriado para manipular a ação.

- **Responder a Intenções Externas:** Os aplicativos Android podem se registrar para responder a intenções externas, como abrir um tipo específico de arquivo ou lidar com solicitações de compartilhamento de conteúdo de outros aplicativos. Isso permite uma integração eficaz entre diferentes aplicativos no dispositivo.


### Componentes de uma Intent

Uma Intent no Android é composta por várias partes:

- **Ação (Action):** Define a ação a ser executada, como "ACTION_VIEW" para visualizar dados, "ACTION_SEND" para enviar dados ou "ACTION_DIAL" para fazer uma chamada telefônica.
- **Categoria (Category):** Define a categoria da Intent, como "CATEGORY_LAUNCHER" para uma Activity de lançamento ou "CATEGORY_DEFAULT" para uma ação padrão.
- **Componente (Component):** Especifica o componente de destino para a Intent, como uma Activity, Service ou Broadcast Receiver.
- **Dados (Data):** Representa os dados associados à Intent, como um URI para visualizar uma página da web ou um arquivo para enviar.

### Exemplos de Uso

As Intents são amplamente utilizadas em aplicativos Android para uma variedade de propósitos. Aqui estão alguns exemplos comuns de como as Intents podem ser usadas:

- **Navegação entre telas:** Abrir uma nova Activity para apresentar uma nova tela ao usuário.
- **Compartilhamento de conteúdo:** Enviar texto, imagens ou arquivos para outros aplicativos.
- **Iniciar serviços em segundo plano:** Iniciar um Service para executar operações em segundo plano, como baixar arquivos ou processar dados.
- **Receber transmissões:** Registrar Broadcast Receivers para responder a eventos do sistema ou de outros aplicativos.

```kotlin
package com.example.projetoupf

import android.app.Activity
import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.AlarmClock
import android.provider.MediaStore
import android.widget.ImageView
import android.widget.RadioGroup
import androidx.appcompat.app.AlertDialog

class Intents : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
            /* algum código que cria a tela via Compose*/
        }


    }

    private fun shareText() {
        val context = LocalContext.current
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_TEXT, "Confira este link: https://developer.android.com")
        }
        context.startActivity(Intent.createChooser(intent, "Compartilhar via"))

    }

    private fun startEmail() {
        val context = LocalContext.current
        val intent = Intent(Intent.ACTION_SENDTO).apply {
            data = Uri.parse("mailto:")
            putExtra(Intent.EXTRA_EMAIL, arrayOf("suporte@exemplo.com"))
            putExtra(Intent.EXTRA_SUBJECT, "Suporte Técnico")
            putExtra(Intent.EXTRA_TEXT, "Olá, preciso de ajuda com...")
        }
        context.startActivity(intent)

    }

    private fun startDial() {
        val context = LocalContext.current
        val intent = Intent(Intent.ACTION_DIAL).apply {
            data = Uri.parse("tel:123456789")
        }
        context.startActivity(intent)

    }

    private fun startNavigator() {
        val context = LocalContext.current
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
        context.startActivity(intent)
    }


    private fun startMaps(){
        val context = LocalContext.current
        val intent = Intent(
            Intent.ACTION_VIEW,
            Uri.parse("geo:0,0?q=Avenida+Paulista,+São+Paulo")
        )
        contexto.startActivity(intent)
    }

    private fun startClock() {
        val context = LocalContext.current
        val intent = Intent(AlarmClock.ACTION_SET_ALARM).apply {
            putExtra(AlarmClock.EXTRA_MESSAGE, "Hora de Acordar")
            putExtra(AlarmClock.EXTRA_HOUR, 8)
            putExtra(AlarmClock.EXTRA_MINUTES, 30)
        }
        contexto.startActivity(intent)

    }


}

```


### Enviar dados de uma Activity para outra via Intent

Para enviar dados a outra Activity é necessário criar a *intent* e adicionar os dados para serem enviados através do método  `putExtra()`. É possível enviar tipos primitivos e objetos, desde que sejam serializáveis. Após, basta iniciar a *intent* por meio do método `startActivity`.



```kotlin
val context = LocalContext.current
val intent = Intent(context, OutraActivity::class.java)
intent.putExtra("nome", "John")
intent.putExtra("idade", 30)
context.startActivity(intent)
```

Na *activity* destino, você precisa obter o Intent que iniciou a Activity. Isso geralmente é feito no método `onCreate()` usando o atributo `intent`.

A partir do objeto *intent*, utilizamos os métodos `getStringExtra()`, `getIntExtra()`, etc., para extrair os dados, com base nas chaves que fornecemos no momento do envio.


```kotlin
val nome = intent.getStringExtra("nome")
val idade = intent.getIntExtra("idade", 0)
```




## Referências

- Documentação oficial do Android: [Activities](https://developer.android.com/guide/components/activities)
- Documentação oficial do Android: [Ciclo de Vida de uma Activity](https://developer.android.com/guide/components/activities/activity-lifecycle)
- Documentação oficial do Android: [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)
- Android Developers Blog: [Understanding Android Intents](https://android-developers.googleblog.com/2009/11/intents-are-not-just-for-starting.html)

