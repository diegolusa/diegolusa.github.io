---
title: "HTML5 - Formulários"
tags:
 - Programação
 - Linguagens de Programação
 - Web
 - Formulários
date: 2021-09-01 08:00:00
---

 

Os formulários em HTML5 são utilizados para coletar informações e interagir com os usuários em páginas da web. Com uma variedade de elementos e atributos, os formulários oferecem flexibilidade e controle sobre como os dados são coletados e processados. Para construir formulários, precisamos utilizar várias tags e conhecer seus atributos básicos. É o que veremos na sequência:

### Estrutura Básica:

Um formulário é definido pelo elemento `<form>`, que envolve os campos de entrada e os elementos de controle. Com os atributos `action` e `method`, podemos especificar para onde os dados serão enviados e como eles serão transmitidos.


O atributo `action` especifica para onde os dados do formulário serão enviados após o envio. Seu valor é geralmente é uma URL, que pode ser absoluta ou relativa. Quando o formulário é enviado, os dados são submetidos para o URL especificado no atributo `action`. Se o atributo `action` estiver vazio, os dados serão submetidos para a mesma página em que o formulário está localizado.

```html
<form action="/destino" method="post">
```
Já o atributo `method` especifica como os dados do formulário serão enviados ao servidor. Os dois valores possíveis são `GET` e `POST`. Quando o valor é `GET`, os dados do formulário são anexados à URL especificada no atributo `action`, tornando-os visíveis na barra de endereços do navegador. Esse método é mais comum para formulários que não enviam dados sensíveis e quando queremos que os dados sejam `bookmarkable`. Por sua vez, se valor for `POST`, os dados do formulário serão enviados no corpo da requisição HTTP, tornando-os não visíveis na URL. Esse método é mais seguro e adequado para o envio de dados sensíveis ou grandes quantidades de dados.

```html
<form action="/submit_form.php" method="post">
```

Os campos de entrada são elementos `<input>`, que podem assumir diversos tipos, como texto, email, senha, entre outros. Podemos controlar a validação dos dados usando atributos como `required`, `maxlength`, `pattern`, entre outros.

Para oferecer opções aos usuários, utilizamos os elementos `<select>`, `<option>`, `<optgroup>`, permitindo criar menus de seleção e listas suspensas. Além disso, temos os elementos `checkbox` e `radio` para seleções múltiplas e únicas, respectivamente.

Com o tipo de entrada `file`, os usuários podem enviar arquivos para o servidor. Isso é útil para formulários que requerem o upload de imagens, documentos, ou outros tipos de arquivos.



Podemos também utilizar elementos como `<label>` para associar rótulos aos campos de entrada, melhorando a acessibilidade e usabilidade. Também é possível agrupar campos relacionados usando `<fieldset>` e `<legend>`.

Veja um exemplo:


```html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo de Formulário HTML5</title>
</head>
<body>

<h2>Exemplo de Formulário HTML5</h2>

<form action="/submit_form.php" method="post" enctype="multipart/form-data">
  
  <fieldset>
    <legend>Dados Pessoais:</legend>
    <label for="fname">Primeiro Nome:</label><br>
    <input type="text" id="fname" name="firstname" required><br>
  
    <label for="lname">Sobrenome:</label><br>
    <input type="text" id="lname" name="lastname" required><br>
  
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br>
  
    <label for="password">Senha:</label><br>
    <input type="password" id="password" name="password" required><br>
  
    <label for="birthdate">Data de Nascimento:</label><br>
    <input type="date" id="birthdate" name="birthdate"><br>
  
    <label for="gender">Gênero:</label><br>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Masculino</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Feminino</label><br>
  
    <label for="photo">Foto de Perfil:</label><br>
    <input type="file" id="photo" name="photo"><br>
  </fieldset>
  
  <fieldset>
    <legend>Preferências:</legend>
    <label for="color">Cor Favorita:</label><br>
    <input type="color" id="color" name="color"><br>
  
    <label for="language">Idioma Preferido:</label><br>
    <select id="language" name="language">
      <option value="en">Inglês</option>
      <option value="es">Espanhol</option>
      <option value="pt">Português</option>
    </select><br>
  
    <label for="newsletter">Receber Newsletter:</label><br>
    <input type="checkbox" id="newsletter" name="newsletter" value="yes">
    <label for="newsletter">Sim</label><br>
  </fieldset>
  
  <input type="submit" value="Enviar">
  
</form>

</body>
</html>

```

### Referências

 - [Basic native form controls](https://developer.mozilla.org/en-US/docs/Learn/Forms/Basic_native_form_controls)
 - [The HTML5 input types](https://developer.mozilla.org/en-US/docs/Learn/Forms/HTML5_input_types)
 - [Other form controls](https://developer.mozilla.org/en-US/docs/Learn/Forms/Other_form_controls)
