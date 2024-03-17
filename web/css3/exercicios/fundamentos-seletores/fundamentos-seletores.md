---
title: "CSS3 - Exercício 1 - Fundamentos de Regras de Estilo"
tags:
 - Programação
 - Linguagens de Programação
 - Web
 - CSS3
date: 2024-03-17 08:00:00
---

Vamos desenvolver nosso primeiro exercício sobre regras de estilo do CSS3. Na sequência você irá encontrar um documento HTML5 fictício, que deverá ser utilizado como base para aplicar as regras de estilo solicitadas.


```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício de Seletores CSS</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Bem-vindo ao Exercício de Seletores CSS</h1>
    </header>
    <main>
        <div class="container">
            <p>Este é um <a href="#">documento HTML fictício</a> para praticar seletores CSS.</p>
            <ul>
                <li>Item 1</li>
                <li class="destaque">Item 2</li>
                <li>Item 3</li>
                <li>Item 4</li>
                <li class="destaque">Item 5</li>
                <li>Item 6</li>
                <li>Item 7</li>
                <li>Item 8</li>
                <li class="destaque">Item 9</li>
                <li>Item 10</li>
            </ul>
        </div>
    </main>
    <footer>
        <p>&copy; 2024 Exercício de Seletores CSS</p>
    </footer>
</body>
</html>
```

Agora, no arquivo **estilos.css**, adicione uma regra para cada questão solicitada. Quanto às propriedades de estilo, você tem a liberdade de escolhar qualquer uma que queira.

1. Elabore uma regra de estilo para todos os elementos `<h1>` do documento.
2. Elabore uma regra de estilo para todos os elementos vinculados à classe `destaque`.
3. Elabore uma regra de estilo o elemento de id `container`.
4. Elabore uma regra de estilo para a primeira linha do primeiro parágrafo filho do elmento cujo identificador é `container`.
5. Elabore uma regra de estilo para o item de lista adjacente àqueles de classe `destaque`.
6. Elabore uma regra de estilo para todos os item de lista ímpares na sequência de aparição no documento.
7. Elabore uma regra de estilo para todos os hiperlinks aplicada quando o mouse passa sobre o elemento.
8. Elabore uma regra de estilo para adicionar o texto `Lista: ` a frente de toda lista não ordenada presente no documento.

Lembre-se de adicionar propriedades que alteram as [medidas](../unidades-medidas.md) dos elementos para exercitar a compreensão do tópico.