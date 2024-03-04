---
title: "Como surgiu a Web"
tags:
 - Programação
 - Linguagens de Programação
 - Web
date: 2021-09-01 08:00:00
---

A Web é um dos serviços mais importantes da Internet. Nela estão boa parte dos serviços que utilizamos em nosso dia-a-dia, como portais de notícias, serviços de streaming, jogos, sistemas bancários, educação, entre outros.

A história da Web inicia em 1989, com `Sir. Tim Berners-Lee`, um cientista da computação nascido em Londres. Após concluir a graduação na universidade de Oxford, Tim foi trabalhar no [CERN](https://home.cern/) como engenheiro de software [@webhistory2021]. 

O CERN é um dos mais importantes centros de pesquisa do mundo, motivo pelo qual cientistas de diversos países frequentavam (e ainda frequentam) suas instalações. Naquela época, Tim observou a dificuldade dos pesquisadores em compartilhar informações. Na maioria dos casos, os dados de pesquisa estavam armazenados em computadores específicos e não eram compartilhados. Desde modo, para utilizar os dados era preciso utilizar o equipamento específico que os armazenava. A ideia de Tim foi então permitir o compartilhamento de informações com uma tecnologia emergente da época, o *hipertexto*[@webhistory2021].

A ideia não foi implementada de imediado pelo CERN, mas garantiu a Tim a possibilidade de dedicar tempo ao projeto [@webhistory2021]. Com isso, no final de 1990, ele havia escrito três implementações que são pilares para a Web até os dias atuais:

- **Linguagem HTML (*HyperText Markup Language*)**: linguagem de marcação utilizada para atribuir estrutura e semântica aos documentos da Web.
- **URI (*Uniform Resource Identifier*)**: endereço único que cada recurso recebe na Web. O tipo mais comum de **URI** chama-se **URL** (*Uniform Resource Locator*).
- **Protocolo HTTP (*Hypertext Transfer Protocol*)**: protocolo que permite a recuperação de recursos vinculados na Web. 



Com estes recursos e uma primeira implementação de *web browser* e *web server* escritas por Tim, a primeira página tornou-se disponível na Internet no final de 1990. Em 1993, Tim e outros envolvidos lutaram para assegurar que o código-fonte fosse disponibilizado de forma aberta, sem qualquer cobrança de *royalties* por parte do CERN. Esse, certamente, representa o marco que tornou a Web o ambiente que conhecemos nos dias atuais [@webhistory2021].

!!! info "Dica"
    **Web Browser** é a designação utilizada para softwares utilizados no lado cliente (usuário) para navegar pela Web. Já **Web Servers** são os softwares instalados em servidores que fornecem aos clientes o conteúdo solicitado por meio das requisições.


Em 1994, Tim foi para o MIT (*Massachusetts Institute of Technology*) com a finalidade de criar o *World Wide Web Consortium* (W3C), uma comunidade internacional voltada a definição de padrões (abertos) para a Web [@webhistory2021].

O uso de padrões abertos permitiu que muitas empresas desenvolvessem produtos para este ecossistema. Os diferentes `web browsers`, popularmente conhecidos com navegadores, são resultado deste processo, por exemplo. Atualmente temos uma grande gama de opções, como *Google Chrome*, *Microsoft Edge*, *Mozilla Firefox*, *Opera*, *Safari*, entre outros. Lembre-se que são os navegadores que nós, clientes, utilizamos para navegar pela *Web*.

## Protocolo HTTP

O procolo [HTTP (Hypertext Transfer Protocol)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview) é um dos protocolos da pilha TCP/IP, presente na camada de **Aplicação**. Opera em um modelo de troca de mensagens entre cliente e servidor. 

Neste modelo, uma máquina (cliente) inicia a comunicação com outra (servidora) solicitando documentos e recursos. A cada requisição enviada, o servidor responde com o recurso solicitado. Deste modo, enquando houver recursos necessários para reconstruir o documento no cliente, a troca de mensagens irá continuar. 

Quando falamos em Web, o cliente normalmente executa um software chamado **web browser**[@mdnhowbrowserworks2024].


![](img/http_req_response.png)
<p><small>Fonte: <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview">Uma visão geral do HTTP - MDN </a></small></p>


## URI - Uniform Resource Identifiers

Conforme mencionamos anteriormente, uma **URI** identifica um recurso na Web de forma única. Assemelha-se ao endereço de sua residência, com alguns detalhes adicionais que permitiram, por exemplo, encontrar sua escova de dentes.

Uma URL (tipo mais comum de URI) é constituído de vários elementos. Geralmente segue o padrão `http://subdomínio.domínio.extensão-domínio/caminho-para-o-recurso?parâmetros` e está presente na barra de endereços do seu web browser enquanto você navega pela Web.

Veja alguns exemplos:

```
http://www.example.com/search?category=books&sort=price
http://www.example.com/login?redirect=http%3A%2F%2Fwww.example.com%2Fdashboard
https://www.example.com/product?id=12345
http://www.example.com/locations?latitude=40.7128&longitude=-74.0060
```



\bibliography