---
title: "Entrada e Saída em Console"
tags:
 - Programação
 - C++
 - I/O
 - Console
date: 2020-09-14 08:00:00
---
Programas de computador são criados basicamente para processar dados. Espera-se, portanto, que hajam meios do programa receber tais dados e devolver os resultados do processamento. Um destes meios são os `consoles`, ou seja, janelas do sistema operacional que permitem apenas comandos na forma de texto. Outra forma típica de coletar e apresentar dados são por interfaces gráficas baseadas em janelas. De qualquer modo, em todos os casos, estamos falando de operações de `input/output` (também conhecidas como `i/o`).

Neste artigo iremos explorar o processo de `i/o` em `console` do C++ por meio da biblioteça [`iostream`](http://www.cplusplus.com/reference/iostream/).


## Cin e cout

Em C++ utilizamos o objeto `cin` para ler valores do teclado, enquanto que utilizamos `cout` para imprimir valores em tela. Vamos começar nosso estudo pela entrada de dados.

Para lermos informações do teclado precisamos informar ao objeto `cin` a variável de destino. Deste modo, o valor informado será transferido (registrado) na variável para posteriormente ser utilizado. Neste processo, podemos informar uma ou mais variáveis na mesma instrução, logo após o operação de extração `>>`.


!!! warning "Atenção"
    Toda variável no C++, para ser utilizada, deve obrigatoriamente ter sido declarada em instruções anteriores. Somente podemos utilizar aquilo que já foi "criado". 


Supondo que quiséssemos ler o preço de determinado produto do supermercado para uma variável de nosso programa, primeiro deveríamos realizar a declaração da mesma e, após, a leitura. Considerando que *preço* refere-se a um conceito numérico com possibilidade de casas decimais, devemos utilizar, na declaração, tipos de dados de ponto flutuante, como `float` ou `double`. Logo, de forma bem resumida, teríamos no mínimo duas etapas em nosso programa relacionadas a este contexto:

- Declaração da variável: `float preco_produto;`
- Leitura de valor de produto do console: `cin >> preco_produto;`

Outro aspecto importante é que as duas instruções acima não podem ser invertidas, ou seja, a declaração deve ocorrer obrigatoriamente em linhas anteriores ao uso da variável.

Mas você há de concordar comigo que simplesmente ficar aguardando o usuário informar um valor pelo teclado, sem informá-lo do que o programa espera receber não parece ser adequado. O correto é apresentar mensagens para, posteriormente, aguardar o valor. Para esta finalidade precisamos recorrer ao objeto `cout`.

Voltando ao exemplo do preço do produto, seria mais conveniente realizar a seguinte sequência de instruções:

- Declaração da variável: `float preco_produto;`
- Apresentar mensagem em tela: `cout << "Informe o valor do produto:"`
- Leitura de valor do produto do console: `cin >> preco_produto;`


!!! warning "Atenção"
    Percebeu que o operador que acompanha o `cout` é oposto em sentido ao do `cin`? Pois é, enquanto o **operador de extração** `>>` é utilizado no objeto `cin`, o do `cout` chama-se **operador de inserção** e se opõem em sentido, apontando para a esquerda `<<`.

## Estudo de caso

Observe nosso programa exemplo abaixo. Tenha especial atenção aos tipos de dado utilizados na declaração das variáveis e aos usos dos objetos de entrada e saída. 

Execute o código com especial atenção às mensagens exibidas em tela, buscando relacionar com a instrução que as gera.
!!! example "Exemplo"

    ```c++

    #include <iostream>

    using namespace std;

    int main()
    {
        int ano_nascimento;
        float peso;
        string nome;
        
        cout << "Informe seu nome: ";
        cin >> nome;
        
        cout << "Informe seu peso: ";
        cin >> peso;
        
        
        cout << "Informe seu ano de nascimento: ";
        cin >> ano_nascimento;
        
        
        cout <<endl << nome <<", nascido em " <<ano_nascimento << " tem peso igual a "<< peso <<endl;
    }

    ```

## Formatando a saída de dados

A apresentação das informações ao usuário é muito importante, afinal estamos falado de tornar a experiência de uso do software o mais agradável possível. Na interação via console, podemos trabalhar a saída com auxílio de recursos da biblioteca [`iomanip`](https://en.cppreference.com/w/cpp/header/iomanip).

O primeiro passo para utilizar a biblioteca é incluí-la no programa através da diretiva `#include`. Feito isso, temos acesso aos seguintes recursos:

- `setfill`: permite definir o caractere utilizado para preencher espaços vazios.
- `setw`: especifica o número de colunas reservadas para impressão do valor que segue.
- `left`: alinhamento da saída em tela à esquerda.
- `right`: alinhamento da saída em tela à direita.
- `setprecision`: configura quantas casas decimais serão impressos na saída de números de ponto flutuante.
- `setiosflags`: ativa *flags* do mecanismo de io, como o tipo de representação numérica utilizada na saída, por exemplo.

Vejamos o exemplo a seguir:

!!! example "Exemplo"   
    ```c++

    #include <iomanip>

    using namespace std;

    int main()
    {
        float value =0.635987;
        double phi = 1.61803398874989484820;
        string hello = "hello";
        /*
            fixed: expressa um número de ponto flutuante com uma quantidade específica de dígitos após ou antes da vírgula
            setprecision(): método que especifica o número de casas decimais após a vírgula
        */
        cout << fixed << setprecision(4);
        cout << hello << " " << value <<endl;
        /*
            setiosflags(ios::right): alinhamento do texto à direita
            setw(50): reserva 50 caracteres de espaço em tela para a saída do próximo valor em tela
        */
        cout <<setiosflags(ios::right) <<setw(50);
        cout << hello << " h" << value <<endl;
        cout << setw(30) << setprecision(12);
        cout << phi <<endl;
        
        return 0;
    }
    ```
    