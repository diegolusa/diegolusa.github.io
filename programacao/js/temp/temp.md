# Objecto Navigator

O objeto `navigator` é um dos principais objetos fornecidos pelo navegador da web em JavaScript. Ele fornece informações detalhadas sobre o navegador e o ambiente em que o código JavaScript está sendo executado. Aqui está uma descrição detalhada deste objeto:

## Propriedades Principais:

### 1. **`navigator.userAgent`**:
   - Retorna a string do agente do usuário, que contém informações sobre o navegador, versão e sistema operacional.

### 2. **`navigator.appName`**:
   - Retorna o nome do navegador.

### 3. **`navigator.appVersion`**:
   - Retorna a versão completa do navegador.

### 4. **`navigator.platform`**:
   - Retorna a plataforma do sistema operacional em que o navegador está sendo executado.

### 5. **`navigator.language`**:
   - Retorna o idioma preferido do usuário, normalmente definido nas configurações do navegador.

### 6. **`navigator.cookieEnabled`**:
   - Retorna um booleano indicando se os cookies estão habilitados no navegador.

### 7. **`navigator.onLine`**:
   - Retorna um booleano indicando se o navegador está online ou offline.

### 8. **`navigator.plugins`**:
   - Retorna uma lista de plugins instalados no navegador.

## Métodos Principais:

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



https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events

https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events

https://www.aleksandrhovhannisyan.com/blog/javascript-promise-tricks/