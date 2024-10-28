---
title: "Linguagens de Programação"
summary: "Programar softwares requer o uso de alguma linguagem de programação, e, em alguns casos, de várias delas. Mas, afinal, o que são linguagens de programação?"
tags:
 - Programação
 - Linguagens de Programação
date: 2020-09-14 08:39:00
authors: Diego A. Lusa
---

A comunicação humana é possível por meio de diferentes linguagens. No caso do computador, o mesmo se aplica, pois fazemos uso de uma linguagem de programação para elaborar rotinas de computação, ensinando o passo-a-passo para o computador.


!!! info "Importante"
    Programar é a arte de escrever sequências de instruções (comandos) para, computacionalmente, resolver problemas do mundo real por meio de uma linguagem de programação.



O programador converte problemas do mundo real em **algoritmos** através do processo de abstração. O algoritmo representa a solução computacional do problema, que irá se tornar operacional a partir do momento em que for **codificado** por meio de uma linguagem de programação. Só então o usuário final terá condições de utilizar o **programa** (que é resultado da compilação ou interpretação da codificação) para atender suas necessidades.

!!! note "Do problema ao programa"
    **Problema > Algoritmo > Código-Fonte > Programa**

As linguagens de programação podem ser classificadas sob diferentes perspectivas. É possível agrupá-las quanto à:

- *Geração*
- *Domínio da Aplicação*
- *Implementação*
- *Paradigma*

A classificação acima, contudo, não é consenso. De qualquer forma, vamos tentar explorar as linguagens de programação a partir da ótica das gerações e paradigmas.


## Linguagens de Máquina

Interpretada diretamente pelo hardware. É a linguagem que o processador reconhece. Compiladores, interpretadores e montadores convertem linguagens de mais alto nível para linguagem de máquina. Representa a **1º geração das linguagens de programação**.

Código em linguagem de máquina é normalmente representado em hexadecimal para tornar a leitura mais simples. Contudo, sua codificação original é binária. Programar neste nível é complexo e exige do profissional profundo conhecimento da arquitetura do hardware em que o programa irá executar. Este tipo de código só é portável para arquiteturas idênticas, uma vez que é altamente dependente do hardware que executa.


```
8B542408 83FA0077 06B80000 0000C383
FA027706 B8010000 00C353BB 01000000
B9010000 008D0419 83FA0376 078BD989
```

## Linguagem Assembly


A interpretação de código de máquina por seres humanos é extremamente difícil. Reconhecer a funcionalidade do código a partir de sequências de códigos hexadecimais é praticamente uma odisséia. Isso porque o código de máquina não se preocupa com questões de legibilidade,  afinal o processador não precisa desta _feature_. 

A fim de tornar a programação uma atividade mais amigável para seres humanos, desenvolveu-se uma linguagem cuja sintaxe era mais próxima da escrita em inglês, com as devidas restrições para tornar o código não ambíguo. Além de facilitar a compreensão do algoritmo, a linguagem Assembly trouxe recursos de abstração que permitiram manter a complexidade do programa sob controle (até certo ponto, é claro).

A Linguagem Assembly foi a primeira tentativa de adicionar abstrações (símbolos chamado de mnemônicos) sobre a linguagem de máquina na esperança de que a programação de software não fosse equiparável a um dos 
<a href="http://www.perseus.tufts.edu/Herakles/labors.html" target="_blank">Doze Trabalhos de Hércules</a>. Ela representa a **2ª geração das linguagens de programação**.

!!! note "Nota"
    Perceba que tornou-se necessário "passar" o código-fonte para um software chamado <a href="https://en.wikipedia.org/wiki/Comparison_of_assemblers" target="_blank">Assembler</a> (montador) para gerar o código em linguagem de máquina (executável).


```
;---------------------------------------------------------------------;

START:
;---------------------------------------------------------------------;
;    TEST FOR PRESENCE OF CALCULATOR                      ;
;---------------------------------------------------------------------;
           SUB     AX,AX
           MOV     ES,AX
           SUB     BH,BH
           MOV     BL,INT_NUMBER
           SHL     BX,1
           SHL     BX,1
           MOV     DI,ES:[BX]
           MOV     ES,ES:[BX+Lógica2]
           ADD     DI,4
           LEA     SI,TAG
           MOV     CX,TAG_LEN
     REPE  CMPSB
           JE      CALL_CALC
           MOV     BX,SCREEN_HANDLE
           MOV     CX,MESSAGE_LEN
           LEA     DX,MESSAGE
           MOV     AH,40h
           INT     21h
           JMP     SHORT CALC_EXIT
;---------------------------------------------------------------------;
;    CALL CALCULATOR                              ;
;---------------------------------------------------------------------;
CALL_CALC:
           MOV     AL,INT_NUMBER
           MOV     BYTE PTR INT_CODE,AL
           DB      0CDh      ; INT
```
Código-fonte extraído de [https://assembly.happycodings.com/code13.html](https://assembly.happycodings.com/code13.html).


## Linguagens de Alto Nı́vel


A escrita do algoritmo é feita utilizando-se um conjunto de comandos (palavras reservadas) em inglês que determinam as ações que o computador deve realizar. Se na linguagem Assembly, os comandos representam "apelidos" para instrução de máquina, nas linguagens de alto nível, os comandos representam ações abstratas. Tais linguagens abrangem diferentes paradigmas, como estruturado, orientado a objetos, funcional e lógico, por exemplo. 

Ao utilizar linguagens de alto nível, o programador aumenta significativamente a portabilidade de seu código dentre as diferentes <a href="https://www.tecmundo.com.br/historia/2157-a-historia-dos-processadores.htm" target="_blank">arquiteturas de máquina</a> existentes, diferentemente da linguagem assembly ou de máquina, que são altamente acopladas ao <a href="https://www.gta.ufrj.br/ensino/EEL580/apresentacoes/Parte2.pdf" target="_blank">conjunto de instruções da CPU</a>.


Em termos de geração, as linguagens de alto nível podem enquadrar-se como sendo de **3ª, 4ª ou 5ª geração**.

Veja abaixo um trecho de código escrito na linguagem C++.

```c++
#include <iostream>

using namespace std;

int saldo;//variável global

int main(){
    int parcela1, parcela2;//variáveis locais
    parcela1 =10, parcela2 = 12;
    saldo = parcela1 + parcela2;

    {//início de bloco
        cout<< saldo << endl;
        int saldo = 14; //variavel local
        cout<< saldo << endl;
    }//fim de bloco
    cout<< saldo << endl ;
    return 0;
}
```

## Linguagens de Sistema

São linguagens de alto nível utilizadas para programação de sistemas. Caracterizam-se por oferecer acesso facilitado ao hardware, ao mesmo tempo que oferecem recursos típicos de linguagens de próposito geral, como estruturas de seleção, laços de repetição e blocos, por exemplo. Uma destas linguagens chama-se [Rust](https://www.rust-lang.org/pt-BR/learn).


```rust

fn main() {    
    println!("Hello World!");
}

```


## Linguagens de Domínio Específico

De alto nı́vel, aplicada a um contexto específico, com expressividade limitada. Expressões regulares são exemplos desta categoria. [Saiba mais sobre DSL](http://www.dcc.ufrj.br/~fabiom/dsl/Aula02.pdf).


## Linguagens Visuais

Toda linguagem que não é baseada em texto. Exemplos deste tipo de linguagem são o [Scratch](https://scratch.mit.edu/) e o [Blockly](https://developers.google.com/blockly/).

## Linguagens Esotéricas

Linguagens que não tem propósito de uso, especificamente. [Neste link você encontrará algumas delas](https://exame.abril.com.br/tecnologia/conheca-10-linguagens-bizarras-nas-quais-voce-nunca-vai-ter-que-programar/).

Ficou curioso sobre a classificação das linguagens de programação? Que tal ler o conteúdo [deste link](http://cs.lmu.edu/~ray/notes/pltypes/) para começar :)