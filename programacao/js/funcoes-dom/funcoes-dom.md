




# Objeto Document

O objeto `document` representa o modelo de objeto do documento HTML, que é a representação de seu conteúdo HTML carregado pelo navegador.

Algumas propriedades úteis deste objeto são:

- `document.URL`: retorna a URL do documento.
- `document.title`: permite obter ou definir o título do documento.
- `document.body`: retorna a referência ao elemento `<body>` do documento.
- `document.head`: retorna a referência ao elemento `<head>` do documento.
- `document.documentElement`: retorna o elemento `<html>` do documento.
- `document.domain`: Retorna o domínio do servidor que serve o documento.
- `document.referrer`: retorna a URL do documento que levou o usuário a este documento.
- `document.forms`: retorna uma coleção de todos os elementos `<form>` no documento.
- `document.images`: retorna uma coleção de todos os elementos `<img>` no documento.
- `document.links`: retorna uma coleção de todos os elementos `<a>` que têm um atributo `href` no documento.
- `document.scripts`: retorna uma coleção de todos os elementos `<script>` no documento.

Outros atributos estão a disposição além destes citados. Você pode encontrar mais detalhes no site [Developers Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Document).



## Métodos:

### 1. `document.getElementById(id)`
   - Retorna uma referência ao elemento que possui o atributo `id` especificado.

### 2. `document.getElementsByClassName(className)`
   - Retorna uma coleção de elementos que têm a classe CSS especificada.

### 3. `document.getElementsByName(name)`
   - Retorna uma coleção de elementos com o atributo `name` especificado.

### 4. `document.getElementsByTagName(tagName)`
   - Retorna uma coleção de todos os elementos com o nome da tag especificada.

### 5. `document.querySelector(selector)`
   - Retorna o primeiro elemento que corresponde ao seletor CSS especificado.

### 6. `document.querySelectorAll(selector)`
   - Retorna todos os elementos que correspondem ao seletor CSS especificado, em uma NodeList.

### 7. `document.createElement(tagName)`
   - Cria um novo elemento HTML especificado pelo nome da tag.

### 8. `document.createTextNode(text)`
   - Cria um novo nó de texto com o texto especificado.

### 9. `document.createDocumentFragment()`
   - Cria um novo DocumentFragment vazio.

### 10. `document.write(text)`
   - Escreve texto HTML no documento.

### 11. `document.writeln(text)`
   - Escreve texto HTML no documento, seguido de uma nova linha.

### 12. `document.addEventListener(event, function, useCapture)`
   - Adiciona um ouvinte de evento a um elemento do documento.

### 13. `document.removeEventListener(event, function, useCapture)`
   - Remove um ouvinte de evento de um elemento do documento.

## Eventos:

Alguns dos eventos mais comuns associados ao objeto `document` incluem:

- `DOMContentLoaded`: É acionado quando o HTML do documento foi completamente carregado e analisado, sem aguardar por folhas de estilo, imagens e subframes para concluir o carregamento.
- `load`: É acionado quando todo o conteúdo do documento, incluindo imagens e folhas de estilo, foi completamente carregado.
- `click`: É acionado quando um elemento é clicado pelo usuário.
- `keydown`, `keyup`, `keypress`: São acionados quando uma tecla é pressionada e liberada.

## Observações:

- O objeto `document` fornece uma interface para interagir com o conteúdo HTML de uma página da web.
- Ele permite acessar e manipular elementos HTML, criar novos elementos, adicionar ou remover eventos, entre outras funcionalidades.
- As propriedades e métodos do objeto `document` são amplamente utilizadas no desenvolvimento de scripts JavaScript para manipular o conteúdo e o comportamento de páginas da web em tempo de execução.

Esta documentação abrange as propriedades, métodos e eventos mais comuns associados ao objeto `document` em JavaScript.




## Função `document.querySelector()` 


É uma função que permite selecionar um elemento HTML em uma página usando um seletor CSS válido. O primeiro elemento encontrado, que condiz com o seletor será retornado pelo método.  

O método `querySelector()` aceita um parâmetro, que é uma string que representa o seletor CSS. Este seletor pode ser um ID, uma classe, um tipo de elemento, um seletor de atributo ou uma combinação deles. 

No exemplo abaixo, estamos buscando a primeira ocorrência de elemento da classe `importante` no documento.


```javascript
var elemento = document.querySelector(".importante");
```

Se houver interesse em retornar todos os elementos que atendem ao seletor, devemos utilizar o método `document.querySelectorAll()`, iterando sobre o retorno.





=====================


# Objeto Window

O objeto `window` é um dos principais objetos do navegador da web e representa a janela do navegador que contém o documento HTML.

## Propriedades:

### 1. `window.document`
   - Retorna o documento HTML carregado na janela.

### 2. `window.location`
   - Retorna um objeto contendo informações sobre a URL da página.

### 3. `window.navigator`
   - Retorna um objeto contendo informações sobre o navegador.

### 4. `window.innerWidth` e `window.innerHeight`
   - Retornam a largura e a altura internas (em pixels) da janela do navegador, incluindo barras de rolagem, mas excluindo a moldura do navegador.

### 5. `window.outerWidth` e `window.outerHeight`
   - Retornam a largura e a altura externas (em pixels) da janela do navegador, incluindo barras de rolagem e a moldura do navegador.

### 6. `window.screen`
   - Retorna um objeto contendo informações sobre a tela do dispositivo.

### 7. `window.history`
   - Retorna o objeto de histórico do navegador, permitindo navegação entre as páginas visitadas.

### 8. `window.localStorage` e `window.sessionStorage`
   - Oferecem acesso aos mecanismos de armazenamento local e de sessão do navegador, respectivamente, permitindo armazenar dados localmente no navegador do usuário.

### 9. `window.frames`
   - Retorna uma coleção de objetos representando todas as frames contidas na janela.

### 10. `window.parent`
   - Retorna a janela pai da janela atual, útil quando uma janela abre outra.

## Métodos:

### 1. `window.alert(message)`
   - Exibe um diálogo de alerta com o texto especificado.

### 2. `window.confirm(message)`
   - Exibe um diálogo de confirmação com o texto especificado, retornando `true` se o usuário clicar em "OK" e `false` se clicar em "Cancelar".

### 3. `window.prompt(message, default)`
   - Exibe um diálogo solicitando que o usuário insira um texto, com uma mensagem opcional e um valor padrão opcional.

### 4. `window.open(url, name, features)`
   - Abre uma nova janela do navegador com o URL especificado.

### 5. `window.close()`
   - Fecha a janela do navegador atual.

### 6. `window.setTimeout(function, milliseconds)`
   - Executa uma função depois de um certo número de milissegundos.

### 7. `window.setInterval(function, milliseconds)`
   - Executa uma função repetidamente, com um intervalo de tempo especificado entre cada execução.

### 8. `window.clearTimeout(timeoutID)` e `window.clearInterval(intervalID)`
   - Cancelam a execução de uma função agendada com `setTimeout()` ou `setInterval()`.

## Eventos:

Alguns dos eventos mais comuns associados ao objeto `window` incluem:

- `load`: É acionado quando o documento e todos os recursos associados foram completamente carregados.
- `resize`: É acionado quando a janela do navegador é redimensionada.
- `scroll`: É acionado quando o usuário rola a página.
- `beforeunload` e `unload`: São acionados quando o documento está prestes a ser descarregado ou completamente descarregado, respectivamente.

## Observações:

- O objeto `window` é a raiz do modelo de objeto do navegador e fornece acesso a várias funcionalidades do navegador e do ambiente de execução JavaScript.
- Ele representa a janela do navegador e oferece acesso ao documento carregado, à localização, ao histórico de navegação, aos mecanismos de armazenamento local, entre outras funcionalidades.
- As propriedades, métodos e eventos do objeto `window` são fundamentais para o desenvolvimento de aplicativos web dinâmicos e interativos.

Esta documentação abrange as propriedades, métodos e eventos mais comuns associados ao objeto `window` em JavaScript.




================


O objeto `navigator` é um dos principais objetos fornecidos pelo navegador da web em JavaScript. Ele fornece informações detalhadas sobre o navegador e o ambiente em que o código JavaScript está sendo executado. Aqui está uma descrição detalhada deste objeto:

### Propriedades Principais:

1. **`navigator.userAgent`**:
   - Retorna a string do agente do usuário, que contém informações sobre o navegador, versão e sistema operacional.

2. **`navigator.appName`**:
   - Retorna o nome do navegador.

3. **`navigator.appVersion`**:
   - Retorna a versão completa do navegador.

4. **`navigator.platform`**:
   - Retorna a plataforma do sistema operacional em que o navegador está sendo executado.

5. **`navigator.language`**:
   - Retorna o idioma preferido do usuário, normalmente definido nas configurações do navegador.

6. **`navigator.cookieEnabled`**:
   - Retorna um booleano indicando se os cookies estão habilitados no navegador.

7. **`navigator.onLine`**:
   - Retorna um booleano indicando se o navegador está online ou offline.

8. **`navigator.plugins`**:
   - Retorna uma lista de plugins instalados no navegador.

### Métodos Principais:

1. **`navigator.geolocation.getCurrentPosition()`**:
   - Retorna a localização atual do usuário.

2. **`navigator.getBattery()`**:
   - Retorna uma promessa que resolve com informações sobre o estado da bateria do dispositivo.

3. **`navigator.mediaDevices.getUserMedia()`**:
   - Permite acessar a câmera e o microfone do dispositivo.

4. **`navigator.vibrate()`**:
   - Ativa a vibração do dispositivo.

### Exemplo de Uso:

```javascript
console.log("Nome do navegador: " + navigator.appName);
console.log("Versão do navegador: " + navigator.appVersion);
console.log("Plataforma: " + navigator.platform);
console.log("Idioma: " + navigator.language);
console.log("Cookies habilitados: " + navigator.cookieEnabled);
console.log("Online: " + navigator.onLine);
```

### Observações:

- O objeto `navigator` é uma parte essencial do desenvolvimento de aplicativos web, pois fornece informações sobre o ambiente do usuário, como o navegador e o sistema operacional.
- Ele pode ser usado para personalizar a experiência do usuário com base em suas preferências e configurações de navegador.
- Além disso, o objeto `navigator` oferece acesso a recursos do dispositivo, como geolocalização, câmera e microfone, permitindo a criação de aplicativos web mais interativos e sofisticados.


===========


O objeto `screen` é uma propriedade do objeto `window` em navegadores da web, fornecendo informações sobre a tela do dispositivo em que a janela do navegador está sendo exibida. Aqui está uma descrição detalhada deste objeto:

### Propriedades Principais:

1. **`screen.width`**:
   - Retorna a largura da tela em pixels.

2. **`screen.height`**:
   - Retorna a altura da tela em pixels.

3. **`screen.availWidth`**:
   - Retorna a largura disponível da tela em pixels, excluindo barras de ferramentas do sistema, como a barra de tarefas do Windows.

4. **`screen.availHeight`**:
   - Retorna a altura disponível da tela em pixels, excluindo barras de ferramentas do sistema.

5. **`screen.orientation`** (propriedade somente leitura):
   - Retorna um objeto `ScreenOrientation` que descreve a orientação da tela.

### Exemplo de Uso:

```javascript
console.log("Largura da tela: " + screen.width + " pixels");
console.log("Altura da tela: " + screen.height + " pixels");
console.log("Largura disponível da tela: " + screen.availWidth + " pixels");
console.log("Altura disponível da tela: " + screen.availHeight + " pixels");
console.log("Orientação da tela: " + screen.orientation.type);
```

### Observações:

- O objeto `screen` fornece informações úteis sobre as características físicas da tela do dispositivo, como largura, altura e disponibilidade de espaço.
- Essas informações podem ser usadas para criar layouts responsivos e adaptar o conteúdo da página com base nas dimensões da tela do usuário.
- A propriedade `screen.orientation` fornece informações sobre a orientação atual da tela, permitindo ajustar o layout e o conteúdo da página de acordo com a orientação do dispositivo.