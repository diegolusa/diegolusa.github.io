---
title: "Desenvolvimento Android - Intents"
summary: "Conceitos básicos de programação Android"
tags:
 - Programação
 - Android
 - Kotlin
date: 2020-09-14 08:39:00
authors: Diego A. Lusa
---


Intents são uma parte essencial do desenvolvimento de aplicativos Android, assim como as activites.Permitem que os desenvolvedores criem interações entre diferentes componentes do sistema, como Activities, Services, Broadcast Receivers e Content Providers. Elas são uma forma flexível e poderosa de realizar operações em um aplicativo Android, incluindo navegação entre telas, compartilhamento de dados, execução de ações específicas e muito mais.

## Funcionalidades Principais

As Intents no Android oferecem várias funcionalidades principais:

1. **Iniciar Componentes:** Uma das principais funcionalidades das Intents é iniciar componentes do Android, como Activities, Services, Broadcast Receivers e Content Providers. 
   
2. **Comunicar Dados:** As Intents podem ser usadas para transmitir dados entre componentes do Android. Os desenvolvedores podem enviar dados, como strings, números, objetos Parcelable ou Serializable, e até mesmo arquivos, entre diferentes partes do aplicativo.

3. **Realizar Ações Explícitas e Implícitas:** As Intents podem ser explícitas ou implícitas. Uma Intent explícita especifica um componente de destino específico dentro do aplicativo usando o nome da classe. Por outro lado, uma Intent implícita especifica uma ação geral e permite que o sistema Android escolha o componente apropriado para manipular a ação.

4. **Responder a Intenções Externas:** Os aplicativos Android podem se registrar para responder a Intenções externas, como abrir um tipo específico de arquivo ou lidar com solicitações de compartilhamento de conteúdo de outros aplicativos. Isso permite uma integração eficaz entre diferentes aplicativos no dispositivo.

## Componentes de uma Intent

Uma Intent no Android é composta por várias partes:

- **Ação (Action):** Define a ação a ser executada, como "ACTION_VIEW" para visualizar dados, "ACTION_SEND" para enviar dados ou "ACTION_DIAL" para fazer uma chamada telefônica.
- **Categoria (Category):** Define a categoria da Intent, como "CATEGORY_LAUNCHER" para uma Activity de lançamento ou "CATEGORY_DEFAULT" para uma ação padrão.
- **Componente (Component):** Especifica o componente de destino para a Intent, como uma Activity, Service ou Broadcast Receiver.
- **Dados (Data):** Representa os dados associados à Intent, como um URI para visualizar uma página da web ou um arquivo para enviar.

## Exemplos de Uso

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

class CallActivities : AppCompatActivity() {
    private val REQUEST_IMAGE_CAPTURE = 1
    private lateinit var rbgChoices: RadioGroup
    private lateinit var imgViewer: ImageView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_call_activities)
        rbgChoices = findViewById(R.id.rg_choices)
        imgViewer = findViewById(R.id.img_viewer)
        rbgChoices.setOnCheckedChangeListener { _: RadioGroup, i: Int ->
            when (i) {
                R.id.rb_create_alarm -> startClock()
                R.id.rb_abrir_navegador -> startNavigator()
                R.id.rb_enviar_email -> startEmail()
                R.id.rb_dial -> startDial()
                R.id.rb_share_text -> shareText()
                R.id.rb_camera -> startCamera()
            }

        }


    }

    private fun startCamera() {


        val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        if (takePictureIntent.resolveActivity(packageManager) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
        }
    }


    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == Activity.RESULT_OK) {

            val imagemCapturada = data?.extras?.get("data") as? Bitmap
            imgViewer.setImageBitmap(imagemCapturada)

        }

    }


    private fun shareText() {
        val intent = Intent(Intent.ACTION_SEND)
        intent.type = "text/plain"
        intent.putExtra(Intent.EXTRA_TEXT, "Texto para compartilhar")
        startOrNotifyIntent(Intent.createChooser(intent, "Compartilhar via..."))

    }

    private fun startEmail() {
        val intent = Intent(Intent.ACTION_SEND)
        intent.type = "text/plain"
        intent.putExtra(Intent.EXTRA_EMAIL, arrayOf("email@example.com"))
        intent.putExtra(Intent.EXTRA_SUBJECT, "Assunto do Email")
        intent.putExtra(Intent.EXTRA_TEXT, "Corpo do Email")
        startActivity(Intent.createChooser(intent, "Enviar email..."))
        startOrNotifyIntent(intent)

    }

    private fun startDial() {
        val intent = Intent(Intent.ACTION_DIAL).apply {
            data = Uri.parse("tel:123456789")
        }
        startOrNotifyIntent(intent)

    }

    private fun startNavigator() {
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.google.com"))
        startOrNotifyIntent(intent)
    }

    private fun startOrNotifyIntent(intent: Intent) {
        if (intent.resolveActivity(packageManager) != null) {
            startActivity(intent)
        } else {
            val alert = AlertDialog.Builder(this)
            alert.setTitle("Atenção")
            alert.setMessage("Nenhum aplicativo pode responder sua requisição")

        }
    }

    private fun startClock() {
        val intent = Intent(AlarmClock.ACTION_SET_ALARM).apply {
            putExtra(AlarmClock.EXTRA_MESSAGE, "Hora de Acordar")
            putExtra(AlarmClock.EXTRA_HOUR, 8)
            putExtra(AlarmClock.EXTRA_MINUTES, 30)
        }
        startOrNotifyIntent(intent)


    }


}

```


## Enviar dados de uma Activity para outra via Intent

Para enviar dados a outra Activity é necessário criar a *intent* e adicionar os dados para serem enviados através do método  `putExtra()`. É possível enviar tipos primitivos e objetos, desde que sejam serializáveis.

Após, basta usar o método `startActivity()` para iniciar a Activity destino, passando o *intent* que contém os dados como parâmetro.

```kotlin
val intent = Intent(this, OutraActivity::class.java)
intent.putExtra("nome", "John")
intent.putExtra("idade", 30)
startActivity(intent)
```

Na *activity* destino, você precisa obter o Intent que iniciou a Activity. Isso geralmente é feito no método `onCreate()` usando o atributo `intent`.

A partir do objeto *intent*, utilizamos os métodos `getStringExtra()`, `getIntExtra()`, etc., para extrair os dados do Intent, com base nas chaves que fornecemos no momento do envio.


```kotlin
val nome = intent.getStringExtra("nome")
val idade = intent.getIntExtra("idade", 0)
```

## Recuperando valores retornados de uma activity


O método `onActivityResult()` é utilizado na captura de retornos de outras Activities em aplicativos Android. Vamos ao passo-a-passo:

### Passo 1: Iniciar uma Activity com `startActivityForResult()`

Para capturar um retorno de outra Activity, devemos iniciar a Activity usando o método `startActivityForResult()` em vez do `startActivity()`. Isso permite que a Activity de destino envie dados de volta para a Activity de origem.


```kotlin
val intent = Intent(this, OutraActity::class.java)
startActivityForResult(intent, REQUEST_CODE)
```

### Passo 2: Implementar o Método `onActivityResult()`

Na Activity de origem, precisamos implementar o método `onActivityResult()`. Este método será chamado automaticamente quando a Activity de destino for encerrada e retornar um resultado.

```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    
    if (requestCode == REQUEST_CODE) {
        if (resultCode == Activity.RESULT_OK) {
            //obtendo o retorno
            val retorno = data?.getStringExtra("chave_retorno")
            
        } else if (resultCode == Activity.RESULT_CANCELED) {
            //tratamento para quando a activity foi cancelada
        }
    }
}
```

### Passo 3: Enviar Dados de Retorno da Activity Destino

Na Activity de destino, quando estiver pronta para enviar os dados de retorno, devemos usar o método `setResult()` antes de encerrar a Activity.

Exemplo em Kotlin para enviar dados de retorno da Activity de destino:
```kotlin
val intent = Intent()
intent.putExtra("chave_retorno", "dados_de_retorno")
setResult(Activity.RESULT_OK, intent)
finish()
```

### Passo 4: Lidar com Resultados e Exceções

É importante lidar com diferentes resultados e exceções ao receber dados de retorno de uma Activity. Logo, verificar se o resultado é `RESULT_OK` ou `Activity.RESULT_CANCELED`, por exemplo, é algo necessário.




### Referências

- Documentação oficial do Android: [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)
- Android Developers Blog: [Understanding Android Intents](https://android-developers.googleblog.com/2009/11/intents-are-not-just-for-starting.html)