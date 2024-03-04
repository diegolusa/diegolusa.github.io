---
title: "Laços de Repetição"
tags:
 - Programação
 - Linguagens de Programação
date: 2020-01-02 23:00:00
---

Os `laços de repetição` são comandos que permitem **iterar (repetir)** um conjunto de instruções sob determinadas condições. Junto com os comandos de desvio condicional, integram os comandos de controle de fluxo e são imprescindíveis na programação estruturada (e em outros paradigmas também).

Temos três laços de repetição na linguagem C++: `for`, `while` e `do while`. Todos eles servem ao mesmo propósito, apresentando sutis diferenças entre si. 

## For
Começaremos nossa análise pelo laço `for`. Podemos dividir sua estrutura em um *cabeçalho* e um *corpo*. No *cabeçalho* temos três segmentos separados por ponto-e-vírgula. Vamos chamá-los de  `s1`, `s2` e `s3`, que irão compor o cabeçalho da seguinte forma: `for(s1;s2;s3)`.

O segmento `s1` representa o espaço para inicialização/declaração das variáveis de controle. Executa somente uma vez, no início da execução do laço. Pode ser omitido, caso o programador assim deseje. 

O segmento `s2` representa a condição de parada do laço, avaliada antes de cada iteração iniciar. Caso o retorno da expressão lógica seja `false`, as instruções do corpo do laço não serão executas e o controle de execução avança para o comando imediatamente posterior o fechamento do laço. O segmento pode ser omitido, indicando que o laço irá repetir indefinidamente (*looping*). **Se a condição especificada for falsa na primeira avaliação, então o laço não irá executar nenhuma vez as instruções contidas no corpo.**

O terceiro segmento, `s3`, corresponde ao espaço para incremento/decremento das variáveis de controle. A execução das instruções nele contidas se dá ao final de cada iteração. Assim como os demais,  o segmento `s3` pode ser omitido.

O `corpo` do laço é composto por uma ou mais instruções delimitadas por `{ }`. Assim como comandos de seleção, podemos aninhar um laço dentro do corpo de outro laço de repetição. Logo, qualquer instrução é aceita.

Vejamos um programa exemplo que imprime no console números inteiros de 1 a 10, construído com auxílio do laço `for`. No segmento `s1` temos a instrução `int i=1`, que corresponde à declaração e inicialização de uma variável chamada `i` com valor `1`. Esta variável tem escopo restrito ao laço, não sendo "visível" fora dele. A condição `i<=10` indica que o laço irá repetir as instruções do corpo enquanto o valor da variável `i` for inferior ou igual a `10`. Já a instrução `i++` indica que a variável `i` aumentará em uma unidade a cada iteração.

```c++
#include <iostream>

using namespace std;

int main()
{
    for(int i=1; i<=10; i++){
        cout << i << endl;
    }
}
``` 

!!! Info
    O operador `++` é chamado de **incremento**. Aplica-se a variáveis inteiras, aumentando seu valor em 1. Pode ser utilizado pré-fixado (antes da variável) ou pós-fixado (após a variável). [link para diferença]()
    A instrução `i++` é equivalente a `i=i+1`. 


Este mesmo programa, com poucas alterações, poderia contar de 10 a 1. Todas as adequações seriam realizadas no cabeçalho, modificando as instruções dos três segmentos. Observe o resultado:

```c++
#include <iostream>

using namespace std;

int main()
{
    for(int i=10; i>=1; i--){
        cout << i << endl;
    }
}
``` 

!!! Info
    O operador `--` é chamado de **decremento**. Aplica-se a variáveis inteiras, diminuindo seu valor em 1. Pode ser utilizado pré-fixado (antes da variável) ou pós-fixado (após a variável). [link para diferença]()
    A instrução `i--` é equivalente a `i=i-1`. 


O laço `for` permite compor instruções de cabeçalho mais complexas. Podemos ter múltiplas inicializações e múltiplos controles de incremento/decremento de variáveis de controle. Ainda sobre a questão do "pulo" da variável de controle, podemos utilizar qualquer quantidade; não estamos limitados a `+1` ou  `-1`.

```c++
#include <iostream>

using namespace std;

int main()
{
    int f = 0;
    for (int i = 4, j = -2, l = 6; l > j && i < l; i += 2, l++, j--)
        f += i + j + l;
    cout << f;
}
``` 

## While

O laço `while` difere do `for` por apresentar apenas a condição de parada em seu cabeçalho. Neste aspecto, sua sintaxe é mais simples. Contudo, os demais controles devem ser realizados pelo programador no corpo do laço (ou fora dele), de modo evitar estados de *looping* não planejados.

Para demonstrar seu funcionamento, reutilizaremos o programa que exibe números de 10 a 1 no console. Comparando com a versão utilizando `for` percebemos que a declaração da variável de controle ocorreu antes da instrução `while` para garantir que a variável exista na interpretação da condição lógica `i<=10`. Já o decremento `i--` precisou ser adicionado após a última instrução, para garantir que toda iteração irá reduzir o valor da variável em 1 unidade.

Assim como o laço `for`, o `while` pode vir a não executar nenhuma vez caso a condição seja falsa na primeira avaliação.

```c++
#include <iostream>

using namespace std;

int main()
{
    int i=10;
    while (i>=1){
      cout << i << endl;
      i--;
    }
}
``` 



## Do While

A construção do `do while` difere do `while` unicamente pela avaliação da condição de parada ser realizada ao final da iteração. **Portanto, este laço irá garantir, no mínimo, uma execução das instruções em seu corpo**. É justamente esta peculiaridade que utilizamos como critério para sua escolha no código. 

Aplicaremos o laço `do while` em nosso já conhecido programa para contar números entre 10 e 1. Faça a comparação com as versões utilizando `while` e `for` para fins de estudo.

```c++
#include <iostream>

using namespace std;

int main()
{
    int i=10;

    do {
        cout << i << endl;
        i--;
    }
    while (i>=1);
}
``` 



## Break

O comando `break` é utilizado para interromper a execução de laços de repetição e o comando `switch`. Sempre que, em um destes comandos, houver um `break`, a execução finaliza naquele ponto e a próxima instrução será aquela imediatamente posterior ao final do bloco.

Utilizamos `break` quando  temos intenção de finalizar o laço mesmo que a condição especificada em sua construção ainda permita novas iterações.

```c++
#include <iostream>

using namespace std;

int main()
{
    for(int i=0;i < 20; i++){
        if (i>14){
            break;
            
        }
        cout << i <<endl;
    }
    
    cout <<"FIM" <<endl;
}

``` 


## Continue


O comando `continue` diferencia-se do `break` porque seu efeito é ignorar as demais instruções que sucedem o comando no corpo do laço. Sempre que executado, uma nova iteração inicia, como é o caso do programa abaixo.

```c++
#include <iostream>

using namespace std;

int main()
{
    for(int i=0;i < 20; i++){
        if (i%2==0){
            cout << i << " PAR" <<endl;
            continue;
        }
        cout << i << " ÍMPAR" <<endl;
    }
}
``` 

# Goto

O comando `goto` permite realizar um desvio incondicional no fluxo de execução das instruções. Seu uso deve restrito àquelas situações em que nenhum outro comando pode ser utilizado,  sendo, portanto, excepcional.

Para utilizar o comando `goto` é preciso marcar instruções com rótulos (*labels*). Com isso é possível "saltar" para qualquer linha rotulada. No programa abaixo definimos o rótulo `fim` para a instrução `cout <<"FIM" <<endl;`, de modo que a linha `goto fim;` levará a execução do programa imediatamente a este ponto.

```c++
#include <iostream>

using namespace std;

int main()
{
    for(int i=0;i < 20; i++){
        
        for(int x=0; x< 15;x++){
            
            for (int y=0; y < 100; y++){
                cout << i <<" - " << x <<" - " << y << endl;
                if (y ==10)
                    goto fim;
            }
        }
        cout << i <<endl;
    }
    
    fim: cout <<"FIM" <<endl;
}
```