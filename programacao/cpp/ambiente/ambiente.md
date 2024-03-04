---
title: "Ambiente de Desenvolvimento"
summary: ""
tags:
 - Programação
 - POO
 - Lógica
date: 2020-02-14 15:34:00
---

Para codificar em C++ é preciso minimamente do compilador e de um editor de texto. A instalação do compilador apresenta diferenças de acordo com a plataforma. Já o editor de texto pode ser qualquer um disponível no mercado.

Quando falamos de codificação profissional de software, os editores de texto são substituídos por IDEs (*Integrated Development Environment*) com a finalidade de aumentar a produtividade e a qualidade do código-fonte. As IDEs agregam diversos _plugins_ que auxiliam o desenvolvedor na tarefa de codificação.

Na sequência apresento a configuração do ambiente mínimo para desenvolvimento em C++ nas plataformas Linux (*Debian based*) e Windows.

## Plataforma Linux

Normalmente as distribuições Linux já possuem o compilador g++ instalado. Para verificar se o compilador está corretamente instalado, podemos abrir o terminal e executar o comando abaixo, que solicita a versão do mesmo.


```bash 
g++ --version
```

Uma vez instalado, esperamos que a saída seja semelhante ao trecho abaixo:

```bash 
g++ (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Caso o compilador não esteja instalado no sistema, será preciso utilizar a ferramenta de gestão de pacotes da distribuição para instalação. Em distribuições baseadas no Debian (Ubuntu, por exemplo), o comando apt-get install realiza a instalação do compilador via terminal. A checagem da instalação pode ser realizada utilizando o comando g++ --version, conforme demonstrando anteriormente.
```
Caso o compilador não esteja disponível no sistema, será preciso utilizar a ferramenta de gestão de pacotes da distribuição para instalação. Em distribuições baseadas no Debian (Ubuntu, por exemplo), o comando `sudo apt-get install g++` realiza a instalação do compilador via terminal. A checagem da instalação pode ser realizada utilizando o comando `g++ --version`, conforme demonstrando anteriormente.





## Windows Plataforma Windows

Assim como na plataforma Linux, no Windows temos diferentes opções de editores e IDEs para desenvolvimento em C++. Uma destas soluções é o [DevC++](https://sourceforge.net/projects/orwelldevcpp/files/latest/download), uma ferramenta gratuita e com bons recursos para quem está iniciando na linguagem. Outras opções também podem ser consideradas, como *Code::Blocks*,  *Netbeans*, *Eclipse*, *Clion* e *Visual Studio Code*. Basicamente, a diferença entre uma IDE e outra refere-se ao conjunto de ferramentas e recursos oferecidos pelas mesmas.

Interessante observar que boa parte destas ferramentas vem com o compilador integrado, o que facilita o processo de instalação. Dos listados abaixo, a exceção fica para o Visual Studio Code.


1. [DevC++](https://sourceforge.net/projects/orwelldevcpp/files/latest/download)
1. [**Visual Studio**](https://visualstudio.microsoft.com/)
1. [Visual Studio Code](https://code.visualstudio.com/)
1. [NetBeans](https://netbeans.org/downloads/index.html)
1. [Eclipse](https://www.eclipse.org/downloads/packages/)
1. [CLion](https://www.jetbrains.com/clion/)
1. [CodeBlocks](http://www.codeblocks.org/)

Dentre as ferramentas que citei, tenho preferência pelo [**Visual Studio Code**](https://code.visualstudio.com/).  O processo de instalação do editor é simples, compreendendo o download do arquivo de pacote (.deb ou .rpm) ou do instalador (conforme sistema operacional escolhido).


O *VS Code*, como também é conhecido, é um editor avançado com suporte para inúmeras linguagens e tecnologias. Apresenta interface intuitiva, baixo consumo de memória e terminal integrado. Não posso deixar de comentar que a ferramenta é gratuita, estando o usuário livre de qualquer cobrança/restrição em relação ao seu uso.

A tela inicial do software contém à esquerda o *Explorer*, no qual apresentam-se os arquivos e diretórios do projeto, ferramenta de *Busca*, integração com ferramenta de *Versionamento de Código*, *Debug* e *Extensões* . A parte central da tela é ocupada pelos diferentes arquivos em edição e na parte inferior constam o *Terminal Integrado*, saída de logs, erros, entre outros.



![Tela inicial do VS Code](/img/cpp/vscode-tela.png)


Programas escritos em C++ podem compreender um ou mais arquivos de código-fonte. Ao conjunto de arquivos que formam o programa chamamos de **projeto**. No VS Code podemos mapear o projeto abrindo a pasta raiz que contém os arquivos. Ainda, para deixar o ambiente completo, podemos instalar uma extensão específica para a linguagem C++, que irá nos auxiliar nas tarefas relacionadas à codificação. Existem inúmeras extensões, mas recomendo a [C/C++ for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools). É possível instalar a extensão diretamente pelo VS Code procurando pela mesma na tela *Extensions* (observe a imagem a seguir).



![Extensão C++ para VS Code](/img/cpp/vscode-extension-c++.png)



## Execução


Com a extensão *C/C++ for Visual Studio Code* instalada, o VS Code já tem condições de compilar o código-fonte e executar o programa gerado de forma integrada. O processo é muito simples! Utilize o botão direito do mouse na tela de edição do código-fonte e escolha a opção *Run Code*.

![Execução de código C++ no VS Code](/img/cpp/vscode-extension-c++-run.png)

!!! warning "Atenção"
    Como o VS Code não possui compilador C++ integrado, é preciso instalar separadamente. [Neste endereço](https://code.visualstudio.com/docs/languages/cpp) você irá encontrar informações de como realizar o procedimento.