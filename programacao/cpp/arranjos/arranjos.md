---
title: "Arranjos"
excerpt: ""
tags:
 - Programação
 - Linguagens de Programação
date: 2021-07-31 21:21:00
toc: true
---

Os tipos primitivos de dados, como `int`, `double` e `char`, permitem armazenar um valor singular, único, na respectiva posição de memória. Há, contudo, situações em que se faz necessário armazenar a partir de uma única variável um conjunto de valores. Tais estruturas recebem o nome de `arrays` (arranjos).

Os `arrays`, junto a `enumerations`, `strings`, `ponteiros`, `ponteiros para membros`, `referencias` e `classes` são conhecidos como `tipos compostos` no C++. Os tipos compostos permitem combinar tipos e outros objetos para definir estruturas de armazenamento e manipulação de dados de alto nível. 


Vamos ao exemplo: imagine que uma escola de programação ofereça um curso de Introdução à Linguagem C++, dividido em 10 módulos. Ao final de cada módulo, o estudante deverá realizar uma avaliação. A nota final do curso será obtida a partir da média aritmética dentre todas as 10 avaliações realizadas pelo estudante. Em uma solução utilizando apenas tipos primitivos, poderíamos pensar em algo assim:

=== "C++"
    ```c++
    #include <iostream>

    using namespace std;

    int main()
    {
        float nt1, nt2, nt3, nt4, nt5, nt6, nt7, nt8, nt9, nt10;

        cin >> nt1 >> nt2 >> nt3 >> nt4 >> nt5 >> nt6 >> nt7 >> nt8 >> nt9 >> nt10;

        float nota_final = (nt1 + nt2 + nt3 + nt4 + nt5 + nt6 + nt7 + nt8 + nt9 + nt10) / 10;

        cout << "NF: " << nota_final << endl;
    }
    ```

Observe que criamos 10 variáveis do tipo `float` para armazenar as notas. No código, a grande quantidade de variáveis prejudica a legibilidade e torna a resolução do problema mais difícil. Mas se pudéssemos utilizar apenas uma variável e, nesta, armazenar 10 notas? Aí está o benefício de se utilizar os `arrays`. Observe a solução alternativa aplicando este conceito:

=== "C++"
    ```c++
    #include <iostream>

    using namespace std;



    int main(){
        float notas[10], nota_final=0;
        for(int i=0;i<10;i++){
            cin >> notas[i];
            nota_final+=notas[i];
        }

        nota_final/=10;
        cout << "NF: "<<nota_final <<endl;

    }
    ```

É nítida  diferença: nosso código ficou mais enxuto e legível. Além disso, adequá-lo para receber 100 notas distintas seria algo muito simples, bem diferente do primeiro exemplo.

Agora é momento de esmiuçar a declaração do `array` e as operações de leitura e escrita realizadas. No C++, declaramos o arranjo adicionando a quantidade de posições em cada dimensão. Logo, no trecho  `float notas[10]`, a variável `notas` terá uma única dimensão com `10` posições. Entendeu a ideia: cada dimensão é especificada entre `[]` e podemos ter quantas dimensões quisermos (até o limite da memória disponível!).

Ao declarar um `array` de `10` posições do tipo `float` estamos solicitando a alocação da quantidade de 40 bytes de memória (cada float requer 4 bytes). Em qualquer operação que demande a leitura ou escrita de algum valor na estrutura será preciso especificar o `índice`, ou seja, a posição  do `array` que deverá ser considerada. 

Se temos um `array` chamado `val` de `10` posições e gostaríamos de escrever o valor `15` na 5º posição, utilizaríamos a instrução `val[4] = 15;`. Percebeu que a 5º posição está no índice 4? Isso ocorre porque, no C++ e muitas outras linguagens, os índices começam em `0`. Para ler o valor de uma determinada posição, utilizamos a mesma sintaxe, especificando o respectivo índice.


Quando pensamos em termos matemáticos, costumamos chamar `arrays` de única dimensão de `vetores` e de duas dimensões, `matrizes`. Aos demais, denominamos `arrays multidimensionais`. 


## Inicialização de Arrays

Assim como variáveis escalares, `arrays` também podem ser inicializados. Observe o programa de exemplo a seguir:

=== "C++"

    ```c++
        #include <iostream>

        using namespace std;

        int main()
        {
            float   notas[2][4] = {{0}, {0}}, 
                    pesos[4] = {3.0, 2.0, 4.0, 1.0}, 
                    media = 0;

            for (int a = 0; a < 2; a++)
            {
                cout << "ALUNO " << a + 1 << endl;
                media=0;
                for (int n = 0; n < 4; n++)
                {
                    cout << "...NOTA " << n + 1 << ": ";
                    cin >> notas[a][n];
                    media += notas[a][n]*pesos[n];
                }
                cout <<"MEDIA: "<< (media/10.0) <<endl;
            }
        }
        ```             

Perceba que a variável `notas` é uma `matriz`, uma vez que contém duas dimensões. Inicializamos todas as posições com zero. Perceba que, para cada dimensão, devemos utilizar um par de `{}`. Já o vetor `notas` foi inicializado com valores correspondentes aos pesos das avaliações. Observe também que a instrução `cin >> notas[a][n];` utiliza dois índices, uma para cada dimensão. 

Podemos ilustrar a estrutura da matriz `notas` pela tabela abaixo, em termos dos 8 valores de notas. A primeira linha e primeira coluna são apenas cabeçalhos e servem apenas para facilitar a compreensão. Ao ler a posição `notas[1][3]` obteríamos `7` com base nos dados apresentados.

<table style="border-collapse:collapse;border-color:#aaa;border-spacing:0;border:none" class="tg"><thead><tr><th style="background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"></th><th style="background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Nota 1</th><th style="background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Nota 2</th><th style="background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Nota 3</th><th style="background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Nota 4</th></tr></thead><tbody><tr><td style="background-color:#fff;border-color:#aaa;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Aluno 1</td><td style="background-color:#FCFBE3;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">5</td><td style="background-color:#fff;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">6</td><td style="background-color:#FCFBE3;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">9</td><td style="background-color:#fff;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">6</td></tr><tr><td style="background-color:#fff;border-color:#aaa;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Aluno 2</td><td style="background-color:#FCFBE3;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">9</td><td style="background-color:#fff;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">8</td><td style="background-color:#FCFBE3;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">7.9</td><td style="background-color:#fff;border-color:inherit;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">7</td></tr></tbody></table>





## Arrays e Laços de Repetição

É extramente comum utilizarmos laços de repetição para percorrer `arrays`, mesmo em códigos triviais. E o motivo é óbvio: é a forma mais simples de fazê-lo. Além de reduzir a quantidade de linhas de código (instruções), o uso de laços de repetição facilita eventuais adaptações no código, como mudança do tamanho do `array`, por exemplo.

Mas atenção: a regra não vale para todos os casos, apenas para àqueles em que o uso de laços de repetição trouxer algum benefício.


Interessante observar também que a quantidade de laços utilizados corresponde ao número de dimensões na maioria dos casos. E os laços são aninhados, ou seja, postos um dentro do outro.




## Arrays de Caracteres


O tipo `char` permite armazenar um caractere específico, como uma letra, símbolo ou meta-caractere. Se observamos com atenção, um texto qualquer corresponde a um vetor de caracteres, onde cada índice armazena um caractere deste texto. Este forma de manipular texto é justamente o que chamamos de `cstring` no C++, uma alusão à forma de representação de texto típica da linguagem C.

Embora possamos utilizar `cstrings` no C++, devemos considerar o uso do tipo abstrato `string`, que nos oferece maior simplicidade de uso e recursos associados que um simples vetor de caracteres. Observe o exemplo a seguir:


=== "C++"

    ```c++
    #include <iostream>
    #include <limits>
    using namespace std;

    int main()
    {
        int idade;
        char nome[200];
        cout << "Nome: ";
        cin.getline(nome, 200);
        if (cin.fail()){
            cin.clear();
            cin.ignore( numeric_limits<streamsize>::max(), '\n');
        }
        cout << endl
            << "Idade: ";
        cin >> idade;
        cout << endl
            << nome << " tem " << idade << " anos.  ";
    }

    ```

A variável `nome` foi declarada como sendo um `array` de 200 posições. Isso significa que podemos armazenar, no máximo, 200 caracteres. O comando `cin.getline(nome, 200);` irá aguardar o usuário digitar um valor, para então armazená-lo no `array`, limitando a captura de 200 caracteres para não causar erro de `overflow`.

Observe que logo após a leitura via `cin` estamos realizando um teste lógico, utilizando `cin.fail()`. Este teste irá retornar `verdadeiro` quando ocorrer algum problema de leitura, como exceder o número máximo de 200 caracteres estabelecido. Ocorrendo tal situação, limpamos o *status* via `cin.clear()` e, na sequencia, removemos todos os caracteres que permaneceram no `input stream` através do comando `cin.ignore( numeric_limits<streamsize>::max(), '\n')`. Isso deve ser feito para garantir que o próximo comando `cin` capture o valor informado, visto que mantido o status de erro, o valor seria desconsiderado.


Outro ponto interessante sobre arrays de caracteres é que eles devem ser finalizados através do meta-caractere `\0`. Por exemplo, se quiséssemos inicializar um array com o texto `Olá, mundo!`, poderíamos fazê-lo da seguinte forma:

=== "C++"

    ```c++
    #include <iostream>
    using namespace std;

    int main()
    {
        char mensagem[] = {'O','l','a',' ', 'm','u','n','d','o','!','\0'};
        cout << mensagem ;
    }

    ```

O tipo `string` diferencia-se de um simples array por ser uma `classe`, ou seja, um tipo abstrato de dados associado ao paradigma da orientação a objetos. Contudo, podemos utilizar o tipo sem nos preocuparmos com estes detalhes. Veja como seria o código para solicitarmos o nome e idade de uma pessoa. Atente-se ao fato de que não estamos informando limite de caracteres, justamente porque o tipo `string` é dinamicamente expansível.

=== "C++"

    ```c++
    #include <iostream>

    using namespace std;

    int main()
    {
        int idade;
        string nome;
        cout << "Nome: ";
        getline(cin,nome);    
        cout << endl
            << "Idade: ";
        cin >> idade;
        cout << endl
            << nome << " tem " << idade << " anos.  ";
    }

    ```

Além de ter tamanho dinâmico, variáveis do tipo `string` (objetos, no termo correto) permitem operações interessantes, como comparações, indexação, *substring*, entre outros. Observe o exemplo a seguir:


=== "C++"

    ```c++
    #include <iostream>
    using namespace std;

    int main()
    {
        string mensagem="Consideramos estas verdades como evidentes por si mesmas, que todos os homens são criados iguais, dotados pelo Criador de certos direitos inalienáveis, que entre estes estão a vida, a liberdade e a procura da felicidade.";

        cout <<"Primeiro caractere: " << mensagem[0] << endl;
        cout <<"Total de caracteres: " << mensagem.length() <<endl;
        cout <<"Índice em que se encontra 'inalienáveis': " << mensagem.find("inalienáveis") <<endl;
        cout <<"A partir da posição 123, 4 caracteres: " << mensagem.substr(123,4) <<endl;

    }

    ```