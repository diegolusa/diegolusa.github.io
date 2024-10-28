---
title: "Desenvolvimento Android - Activities"
summary: "Conceitos básicos de programação Android"
tags:
 - Programação
 - Android
 - Kotlin
date: 2020-09-14 08:39:00
authors: Diego A. Lusa
---


Uma **Activity** é um componente fundamental do desenvolvimento de aplicativos Android, representando uma única tela com uma interface de usuário. Elas são os blocos de construção principais com os quais os usuários interagem em um aplicativo Android. O ciclo de vida de uma Activity descreve como ela passa por diferentes estados, desde sua criação até sua destruição.

## Ciclo de Vida de uma Activity

O ciclo de vida de uma Activity é gerenciado pelo sistema operacional Android e é composto por uma série de estados, que são eventos que ocorrem durante a execução da Activity. Aqui estão os principais estados do ciclo de vida de uma Activity:

1. **Created (Criado):** A Activity é criada, mas ainda não é visível ao usuário.
2. **Started (Iniciado):** A Activity se torna visível ao usuário, mas ainda não está interagindo ativamente com ele.
3. **Resumed (Resumido):** A Activity está em primeiro plano e está interagindo ativamente com o usuário.
4. **Paused (Pausado):** A Activity perde o foco, mas ainda é visível ao usuário. Nesse estado, ela ainda está visível, mas não está interagindo ativamente com o usuário.
5. **Stopped (Parado):** A Activity não está mais visível ao usuário e pode ser destruída pelo sistema se a memória estiver baixa.
6. **Destroyed (Destruído):** A Activity é destruída e removida da memória.

![Ciclo de Vida de uma Activity](https://developer.android.com/guide/components/images/activity_lifecycle.png)

### Principais Métodos do Ciclo de Vida

Cada estado do ciclo de vida é associado a métodos específicos que são chamados automaticamente pelo sistema Android. Aqui estão os principais métodos do ciclo de vida de uma Activity:

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


### Referências

- Documentação oficial do Android: [Activities](https://developer.android.com/guide/components/activities)
- Documentação oficial do Android: [Ciclo de Vida de uma Activity](https://developer.android.com/guide/components/activities/activity-lifecycle)

