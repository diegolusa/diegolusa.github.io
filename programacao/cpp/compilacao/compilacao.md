---
title: "Compilando o Primeiro Programa"
excerpt: ""
tags:
 - Programação
 - Linguagens de Programação
date: 2020-01-02 23:01:00
toc: true
order: 3
sidebar:
  nav: "cplusplus"
---

Após escrito o código-fonte de um programa, precisamos convertê-lo em código de máquina, para que o processador tenha condições de executá-lo. Esse processo de "tradução" pode ser realizado de duas formas diferentes: **compilação** e **interpretação**.

A **compilação** é o processo em que submetemos o código-fonte do programa a um software chamado **compilador**. O compilador deve estar disponível no sistema e corretamente configurado. No processo, o compilador realiza verificações sintáticas (uso correto da sintaxe da linguagem) e semânticas (interpretação do significado de instruções para detectar erros). Não havendo erros, o código de alto nível é traduzido para código de baixo nível (máquina) direcionado à plataforma (sistema operacional + arquitetura de máquina) alvo. É criado então um **executável**.

A compilação ocorre apenas uma vez, sendo que o produto final é o programa que o usuário irá utilizar. Podemos citar as seguintes vantagens do processo:

- Não há custo de tradução em tempo de execução
- O código-fonte é preservado, não sendo distribuído para o cliente
- Possibilidade de otimizações aprimoradas, visto que um maior tempo de compilação é aceitável

Contudo também existem desvantagens, como:

- Dificuldade no diagnóstico de erros
- Testar o software torna-se mais oneroso, porque requer vários ciclos de compilação
- Algumas validações são difíceis de executar em tempo de compilação
- Construir bons compiladores é algo muito complexo

Já a **interpretação** é o processo em que o cód
igo-fonte é traduzido a cada execução (*on the fly*). O **interpretador** é o software que realiza tal tarefa e ele sempre trabalha com dois elementos: programa e o código-fonte. O código é gerado sob demanda, seguindo o fluxo de execução do algoritmo. Existem interpretadores que otimizam o processo, mantendo trechos de código frequentemente acessados já compilados.

A interpretação tem benefícios interessantes. Podemos citar, por exemplo:

- Facilidade em *debugar* o código
- Interpretadores são mais simples de desenvolver, se comparados à compiladores
- Testar o software torna-se mais simples
- O interpretador pode ser incorporado ao software para fins de implantação
- É possível avaliar código em tempo de execução

Como desvantagens do processo de interpretação, podemos citar:

- Necessidade de tradução a cada execução, que implica em maior custo computacional
- Dificuldades em se proteger o código-fonte
- Interpretadores eficientes são complexos para desenvolver

Você pode saber mais sobre estes processos de tradução no excelente material produzido para a disciplina [*COMP 524: Programming Language Concepts*, por *Björn B. Brandenburg* da *University of North Carolina*](https://wwwx.cs.unc.edu/~bbb/comp524/doc/03CompilationAndInterpretation.pdf)
  
!!! info "Dica"
    Lembre-se que a linguagem C++ é compilada!

