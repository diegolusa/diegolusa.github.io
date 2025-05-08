O [**Firebase**](https://firebase.google.com/) é uma plataforma de desenvolvimento de aplicativos móveis e web oferecida pelo Google. Ele fornece ferramentas e serviços que ajudam desenvolvedores a criar, melhorar e escalar seus aplicativos. A plataforma foi projetada para simplificar tarefas comuns, como autenticação, armazenamento de dados em tempo real, armazenamento de arquivos e notificações, permitindo que os desenvolvedores foquem na criação de experiências de usuário e na lógica de negócios.


A integração do Firebase com uma aplicação Angular + Ionic habilita o uso de todas as funcionalidades do Firebase, como autenticação, banco de dados em tempo real, armazenamento e notificações push. Naturalmente alguns recursos estão disponíveis somente mediamente pagamento. Aqui nos interessam apenas os recursos que podem ser utilizados gratuitamente.


Antes de iniciarmos com os passos de instalação e configuração do projeto, você já deve ter providenciado uma conta no Firebase. Caso tenha uma conta Google, o processo é muito simples e rápido. Além disso, os passos que seguem irão considerar que você já tem um projeto Angular utilizando Ionic disponível.

Vamos para as etapas: 


####  Criar novo projeto Firebase

- Acesse o [console do Firebase](https://console.firebase.google.com/).
- Clique em "Adicionar projeto" e siga as etapas para criar um novo projeto Firebase.
- Após criar o projeto, clique em “Adicionar um aplicativo” e escolha “Web”.
- Registre seu aplicativo e copie as credenciais (chaves de configuração), que serão usadas na próxima etapa.

#### Instalar as dependências *firebase* e *angularfire*

No diretório raiz do projeto, via terminal, instale as dependências *firebase* e *angularfire* utilizando o *npm*:

```bash
npm install firebase @angular/fire
```

#### Configurar as credenciais do Firebase projeto

No arquivo `src/environments/environment.ts` do projeto, adicione as configurações do Firebase (as chaves que você copiou ao registrar o aplicativo). Caso você esteja utilizando um repositório Git, lembre-se de NÃO REALIZAR COMMIT do arquivo com as credenciais, pois isso representa uma brecha de segurança:

No trecho de código abaixo, os valores são apenas placeholders para indicar que você deve substuir pelos gerados para a sua aplicação.


```typescript
export const environment = {
  production: false,
  firebaseConfig: {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
  }
};
```



#### Importar o módulo AngularFire no projeto

No arquivo `src/app/app.module.ts`, devemos adicionar as importações necessárias e configurar o Firebase para ter acesso aos recursos em toda a aplicação Angular.

```typescript hl_lines="7 8 9 17 18"
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AngularFireModule } from '@angular/fire/compat';
import { AngularFireAuthModule } from '@angular/fire/compat/auth';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    AngularFireModule.initializeApp(environment.firebaseConfig),
    AngularFireAuthModule
  ],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

Aqui, o `AngularFireModule` é inicializado com as configurações do Firebase. Já o `AngularFireAuthModule` é adicionado para suporte à autenticação, caso necessário.

#### Interagindo com o Realtime Database

Aqui está um material didático com um guia completo para que seus estudantes possam realizar operações de CRUD (Criar, Ler, Atualizar e Excluir) no Firebase Realtime Database usando Angular e Ionic. Este exemplo prático simula um gerenciamento de itens de uma lista, como uma aplicação de "Lista de Tarefas".

### 1. Pré-requisitos

Antes de começar, verifique se o Firebase está integrado com seu projeto Angular + Ionic.

- **Instalar Firebase e AngularFire**:
  ```bash
  npm install firebase @angular/fire
  ```

- **Configurar o Firebase**: No Console do Firebase, crie um projeto e ative o Realtime Database em modo de teste.

- **Adicionar Configurações do Firebase**: No arquivo `src/environments/environment.ts`, configure as chaves do Firebase, que podem ser encontradas na seção "Configurações do Projeto" no Console do Firebase:

  ```typescript
  export const environment = {
    production: false,
    firebaseConfig: {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_AUTH_DOMAIN",
      databaseURL: "YOUR_DATABASE_URL",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_STORAGE_BUCKET",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID",
    },
  };
  ```

- **Configurar Firebase no AppModule**: No arquivo `src/app/app.module.ts`, importe e configure o AngularFireModule e o AngularFireDatabaseModule:

  ```typescript
  import { AngularFireModule } from '@angular/fire/compat';
  import { AngularFireDatabaseModule } from '@angular/fire/compat/database';
  import { environment } from '../environments/environment';

  @NgModule({
    imports: [
      AngularFireModule.initializeApp(environment.firebaseConfig),
      AngularFireDatabaseModule,
    ],
  })
  export class AppModule {}
  ```

### 2. Criar Serviço de CRUD

Crie um serviço para centralizar todas as operações de CRUD. No diretório `src/app/services/`, crie o arquivo `realtime-db.service.ts`:

```typescript
import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RealtimeDbService {
  private dbPath = '/items';

  constructor(private db: AngularFireDatabase) {}

  // Criar um novo item
  createItem(item: any): void {
    this.db.list(this.dbPath).push(item);
  }

  // Ler todos os itens
  getItems(): Observable<any[]> {
    return this.db.list(this.dbPath).valueChanges();
  }

  // Atualizar um item
  updateItem(key: string, value: any): Promise<void> {
    return this.db.list(this.dbPath).update(key, value);
  }

  // Excluir um item
  deleteItem(key: string): Promise<void> {
    return this.db.list(this.dbPath).remove(key);
  }

  // Excluir todos os itens
  deleteAll(): Promise<void> {
    return this.db.list(this.dbPath).remove();
  }
}
```

Neste serviço:
- `createItem` adiciona um novo item.
- `getItems` recupera todos os itens.
- `updateItem` atualiza um item existente usando sua chave.
- `deleteItem` exclui um item por chave.
- `deleteAll` exclui todos os itens.

### 3. Criar Componente para Exibir e Manipular Dados

Agora, vamos criar um componente em `src/app/pages/home/home.page.ts` para exibir a lista de itens e permitir operações de CRUD:

```typescript
import { Component, OnInit } from '@angular/core';
import { RealtimeDbService } from '../services/realtime-db.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})
export class HomePage implements OnInit {
  items: any[] = [];
  newItem: string = '';

  constructor(private dbService: RealtimeDbService) {}

  ngOnInit() {
    this.getItems();
  }

  // Criar item
  createItem() {
    if (this.newItem) {
      this.dbService.createItem({ name: this.newItem });
      this.newItem = '';
    }
  }

  // Obter todos os itens
  getItems() {
    this.dbService.getItems().subscribe((data) => {
      this.items = data;
    });
  }

  // Atualizar item
  updateItem(key: string, newValue: string) {
    this.dbService.updateItem(key, { name: newValue });
  }

  // Excluir item
  deleteItem(key: string) {
    this.dbService.deleteItem(key);
  }

  // Excluir todos os itens
  deleteAll() {
    this.dbService.deleteAll();
  }
}
```

### 4. Criar o Template HTML

No arquivo `src/app/pages/home/home.page.html`, crie o template para exibir e manipular a lista de itens:

```html
<ion-header>
  <ion-toolbar>
    <ion-title>Lista de Itens</ion-title>
  </ion-toolbar>
</ion-header>

<ion-content>
  <!-- Campo para adicionar novo item -->
  <ion-item>
    <ion-label position="stacked">Novo Item</ion-label>
    <ion-input [(ngModel)]="newItem" placeholder="Digite o nome do item"></ion-input>
  </ion-item>
  <ion-button expand="block" (click)="createItem()">Adicionar Item</ion-button>

  <ion-list>
    <!-- Exibir lista de itens -->
    <ion-item *ngFor="let item of items; let i = index">
      <ion-label>{{ item.name }}</ion-label>
      <ion-button fill="clear" color="danger" (click)="deleteItem(item.key)">
        Excluir
      </ion-button>
      <ion-button fill="clear" color="primary" (click)="updateItem(item.key, 'Novo Nome')">
        Editar
      </ion-button>
    </ion-item>
  </ion-list>

  <!-- Botão para excluir todos os itens -->
  <ion-button color="danger" expand="block" (click)="deleteAll()">Excluir Todos</ion-button>
</ion-content>
```

### 5. Explicação do Código

- **Adicionar Novo Item**: O botão "Adicionar Item" chama o método `createItem`, que usa o serviço para adicionar um novo item ao banco de dados.
- **Exibir Lista de Itens**: Cada item da lista é exibido dinamicamente usando o `*ngFor` e exibe o nome do item.
- **Editar Item**: Cada item possui um botão "Editar" que chama `updateItem` com um novo nome. Esse exemplo usa o valor `'Novo Nome'`, mas pode ser ajustado para uma entrada personalizada.
- **Excluir Item**: O botão "Excluir" exclui o item individualmente usando `deleteItem`.
- **Excluir Todos os Itens**: O botão "Excluir Todos" usa `deleteAll` para remover todos os itens do Realtime Database.

### 6. Executar o Projeto

Execute o comando abaixo para ver o projeto em execução:

```bash
ionic serve
```

Agora, seus alunos devem conseguir adicionar, listar, atualizar e excluir itens no Realtime Database usando Firebase, Angular e Ionic. Essa documentação oferece um exemplo prático de CRUD, que eles podem expandir conforme suas necessidades no desenvolvimento web.











Agora que o Firebase está configurado, você pode começar a utilizar seus serviços, como autenticação, Firestore (banco de dados), ou armazenamento.

##### Exemplo: Autenticação com Google

No arquivo `src/app/services/auth.service.ts`, crie um serviço de autenticação:

```typescript
import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import firebase from 'firebase/compat/app';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private afAuth: AngularFireAuth) {}

  // Login com Google
  loginWithGoogle() {
    return this.afAuth.signInWithPopup(new firebase.auth.GoogleAuthProvider());
  }

  // Logout
  logout() {
    return this.afAuth.signOut();
  }

  // Verificar estado do login
  isAuthenticated() {
    return this.afAuth.authState;
  }
}
```

##### Exemplo: Usando o serviço no componente

No arquivo `src/app/pages/home/home.page.ts`, injete o serviço de autenticação e use seus métodos:

```typescript
import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})
export class HomePage {
  user: any;

  constructor(private authService: AuthService) {
    this.authService.isAuthenticated().subscribe(user => {
      this.user = user;
    });
  }

  login() {
    this.authService.loginWithGoogle().then(res => {
      console.log('Logged in!', res);
    }).catch(err => {
      console.error('Login error:', err);
    });
  }

  logout() {
    this.authService.logout();
  }
}
```

##### Exemplo: Template HTML

No arquivo `src/app/pages/home/home.page.html`, adicione os botões de login/logout:

```html
<ion-header>
  <ion-toolbar>
    <ion-title>Ionic + Firebase</ion-title>
  </ion-toolbar>
</ion-header>

<ion-content>
  <div *ngIf="user; else loggedOut">
    <h2>Bem-vindo, {{ user.displayName }}</h2>
    <ion-button (click)="logout()">Logout</ion-button>
  </div>

  <ng-template #loggedOut>
    <ion-button (click)="login()">Login com Google</ion-button>
  </ng-template>
</ion-content>
```

#### 7. Testar a aplicação

Execute o projeto:

```bash
ionic serve
```

Agora, ao carregar sua aplicação, você deverá conseguir realizar login com o Google e ver o status do usuário autenticado.

### Conclusão

Você agora tem uma aplicação Ionic + Angular integrada com o Firebase, com suporte a autenticação via Google. Esse tutorial pode ser expandido para incluir outros serviços do Firebase, como Firestore, Storage e Messaging, dependendo das necessidades do seu aplicativo.