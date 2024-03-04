

Um dos princípios do paradigma da programação estruturada é o conceito de `sub-rotina`, também conhecidas como `função` e/ou `procedimento` (algumas linguagens de programação diferenciam um do outro). 

Criar `sub-rotinas` é essencial para administrar a complexidade do software. Não é incomum que softwares tenham milhares, ou mesmo milhões de linhas de código. Se todo esse código não for organizado em partes administráveis e compreensíveis, os programadores terão sérias dificuldades para dar sequência ao projeto.

O processo de criar sub-rotinas compreende, portanto, a divisão de um grande problema em partes menores, como se fossem blocos, por meio dos quais a solução final será construída. A esse processo chamamos de `modularização`, um conceito-chave em projetos de software.


Além de tornar a complexidade administrável por seres humanos, a modularização permite `reutilizar` código. Jamais esqueça desta palavra - `reutilizar` - pois ela é o *Santo Graal* da programação. Reutilizar significa reaproveitar código funcional, testado e validado, o que implica diretamente na redução do tempo e custos de desenvolvimento do projeto.

Falando especificamente da linguagem C++, podemos afirmar categoricamente que nenhum programa existe sem ter, ao menos, uma função. Se neste momento você pensou na função `main`, parabéns  &#x1F601;

Uma função é um conjunto de instruções agrupadas, comumente identificada por um nome, que são executadas sempre que uma operação de invocação está presente no código. É o meio que temos para `representar ações e computações em um programa`, de modo que sempre que queremos fazer algo no código para o qual é possível atribuir um nome, aí estaremos face a uma nova função [@stroustrup2014programming].

!!! note "Nota"
    *Invocar* uma função significa chamá-la pelo nome ou por seu endereço de memória no código.

Para criarmos funções é preciso conhecer as regras de sintaxe que a linguagem de programação aplica. Falando do C++, a sintaxe do comando envolve:

- **Tipo de retorno**: Especifica no cabeçalho da função (sua assinatura) que tipo de valor ela retorna ao chamador. Qualquer tipo disponível pode ser retornado e, para os casos onde o retorno deve ser desconsiderado, utilizamos o tipo especial `void`.
- **Identificador**: Assim como variáveis têm nomes, as funções também. As mesmas regras de nomenclatura se aplicam.
- **Argumentos formais (parâmetros)**: São variáveis definidas no cabeçalho da função por meio das quais podemos passar valores específicos a cada chamada. Ter parâmetros é algo opcional em uma função. 
- **Instruções**: É o que a função executa. Compreende seu corpo, sua lógica de operação interna.
- **Retorno**: Comando que finaliza a execução da função e devolve ao chamador o resultado do processamento. Em C++, o retorno é feito através do comando `return`. Toda função que indicar retornar um tipo diferente de `void` deve obrigatoriamente fazê-lo para todos os caminhos possíveis de finalização (ou gerar um erro). A exceção fica com a função `main`, que ao executar com sucesso todos os comandos automaticamente irá retornar `0`.

Vamos utilizar como estudo de caso a própria função `main`. Observe que começamos pela tipo `int`, indicando que seu retorno é um número inteiro. Na sequência, temos `main`, o nome da função. Os parâmetros são declarados no espaço contido entre os parênteses `()`. Cada declaração de parâmetro compreende seu tipo e nome, tal qual fazemos ao declarar variáveis. Se houver necessidade de mais de um parâmetro, devemos separá-los com vírgula. Por fim, as instruções ficam contidas entre as chaves `{}`.


=== "C++"

```c++
int main(int argc, char *argv[])
{
    /*instruções*/
}
```

Sabemos que a função `main` é obrigatória em qualquer programa escrito em C++. Caberá a nós, programadores, criamos as demais funções para nossos programas. Na sequência, apresento alguns exemplos de funções e comentários pertinentes.

### Retornando Valores

Tipicamente criamos funções que retornam algum valor ao chamador (`caller`). Sabemos que o tipo de retorno acompanha a declaração da função e que, por meio deste tipo, o compilador poderá aceitar a chamada da função em qualquer contexto que permita presença daquele tipo de dado.

No programa abaixo estamos utilizando uma função chamada `ler_idade()`. Perceba que o cabeçalho (assinatura) aparece antes da função `main`, enquanto que a implementação está posta após. Isso se faz necessário para atender um princípio básico de programação, que é: `somente podemos fazer uso, em uma instrução, de estruturas já disponíveis naquele momento`. Ou seja, precisamos orientar o compilador da existência de uma função chamada `ler_idade()`, que retorna valor inteiro, pois estamos chamando ela antes de propriamente implementá-la.

=== "C++"

```c++  linenums="1" hl_lines="5 9 10 13"
#include <iostream>

using namespace std;

int ler_idade();

int main(){
	int idade1, idade2;
	idade1 = ler_idade();
	idade2 = ler_idade();
}

int ler_idade(){
	int idade;

	while(true){		
		cout << "Informe a idade [13,59]: ";
		cin >> idade;
		if (idade <13 || idade > 59)		
			cout << endl << "Valor inválido" << endl;
		else
            return idade;
	}
}	
```

Nas linhas `9` e `10` temos a chamada para a função `ler_idade()`. Perceba que operação de invocação compreende indicar o nome e os argumentos entre `()`, quando existirem. Assim que a execução do código alcançar essa instrução, o fluxo de execução é desviado para a primeira linha da função, executando seu código interno até que ela finalize. O valor retornado via `return` será "substituído" no espaço em que ocorreu a chamada. Logo, as variáveis `idade1` e `idade2` irão receber a idade informada pelo usuário, adequadamente compreendida no intervalo $\left[13,59\right]$.

Mas afinal, qual é a vantagem de se utilizar a função `ler_idade()`? 

- **Abstração**: Abstrair significa reduzir complexidade a partir da elaboração de um conceito de alto nível sobre algo. Em nosso código, estamos deixando a carga da função estabelecer e executar todas as regras de validação e coleta de um valor de idade. Na perspectiva da instrução que chama a função, não há informação sobre como a função opera, apenas que ela irá retornar um valor inteiro que representa uma idade. É uma relação de confiança, em que delegamos a responsabilidade para a função e ficamos aguardando seu retorno. Ao fazer isso, não precisamos nos preocupar com todos os pequenos detalhes do código, permitindo ter uma visão de mais alto nível durante a codificação.

- **Reuso**: Todos os locais do código que demandam a leitura de uma idade farão chamada à função. Logo, não precisaremos repetir todo o código para cada situação em que uma idade for demandada.

- **Único ponto de alteração**: Mudou o critério para determinar uma idade válida? Sem problemas, basta alterar o código da função que todos os locais que fazem uso dela irão utilizar a versão atualizada. Escreva apenas uma vez, use em todo lugar! 

### Passando Argumentos

Muitas vezes precisamos passar valores específicos no momento em que a função é chamada. Estes valores recebem o nome de `argumentos`. Os argumentos são utilizados para alimentar os `parâmetros` da função, que são variáveis que permitem à função receber dados do mundo externo e utilizá-los em sua execução. 

Podemos passar argumentos de dois modos diferentes: `por valor` e `por referência`. Quando utilizamos a estratégia de passagem `por valor`, o parâmetro receberá uma cópia do valor informado. Lembre-se que um `parâmetro` é uma variável local da função, inicializada a cada chamada realizada[@stroustrup2014programming].

A passagem `por valor` de argumentos gera uma cópia, de modo que eventuais alterações realizadas pela função no parâmetro correspondente não terão impacto externo. Para ilustrar este comportamento iremos utilizar um programa muito simples, composto por duas funções: `main` e `substitui`. 



=== "C++"

```c++  linenums="1" hl_lines="7 13 14 15"

#include <iostream>

using namespace std;

void substitui(int a)
{
    a = 7;
}

int main()
{
    int a = 3;
    cout << a << endl;
    substitui(a);
    cout << a << endl;
}
```

A função `substitui` define um parâmetro, chamado de `a`, para receber um valor inteiro. Na linha \(14\), ela é chamada passando-se para o parâmetro `a` o argumento `a`. Mas espera aí: não é o mesmo `a` então?

Não, são posições de memória diferentes. Todo parâmetro representa uma variável local à função, cujo escopo de visibilidade é o corpo desta função. O fato de estarmos enviando um argumento, que é uma variável, com o mesmo nome representa uma simples coincidência. 

Então, se estamos falando de posições de memória diferentes, a atribuição realizada pela função na linha \(7\) não vai alterar o valor da variável `a` declarada na função `main`. Deste modo, ambos os comandos `cout` irão escrever o valor \(3\). Chamamos isso de passagem de argumento por cópia (*call by value*).

Agora vamos modificar nossa função `substitui` adicionando o operador `&` antes do nome do parâmetro. Nosso programa em sua versão alterada seria:

=== "C++"

```c++  linenums="1" hl_lines="7 13 14 15"

#include <iostream>

using namespace std;

void substitui(int &a)
{
    a = 7;
}

int main()
{
    int a = 3;
    cout << a << endl;
    substitui(a);
    cout << a << endl;
}
```
Estranhamente, o resultado desta versão do programa será \(3\) para o primeiro comando `cout` e \(7\) para o segundo. Por que isso ocorre? É que neste programa estamos utilizando passagem de argumento por referência (*call by reference*), ou seja, a função recebe **o endereço de memória** do argumento. Deste modo, as alterações realizadas dentro da função no valor do parâmetro serão diretamente aplicadas à variável informada como argumento.

Mas isso não pode gerar efeitos colaterais indesejados? Que benefícios há em se utilizar referências?

Bem, o programador deverá utilizar o recurso com prudência. Nem todo parâmetro deve ser *by reference*. O grande benefício está possibilidade de compartilhar áreas de memória, uma operação muito mais rápida se comparada a uma cópia de valores. Imagine se precisássemos informar um vetor de \(1000\) posições para um função e todos estes valores precisassem ser copiados para o parâmetro?

Logo, nesta perspectiva, qualquer `array` definido como parâmetro irá receber uma referência de memória e não uma cópia de valor. Podemos verificar isso no programa a seguir, construído para ler uma matriz \(M_{2 \times 2}\) e apresentar a média aritmética dos valores lidos.

=== "C++"

```c++  
#include <iostream>
#include <iomanip>

#define LINHAS 2
#define COLUNAS 2

using namespace std;

void ler_dados_matriz(int m[][COLUNAS]){
     for(int l=0;l < LINHAS;l++){
         for(int c=0;c < COLUNAS;c++ ){
               cout<<"M["<<l<<","<<c<<"]: ";
               cin >> m[l][c]; 
         }
     }   
}

void imprimir_matriz(int m[][COLUNAS]){
    cout <<"M: "<<endl;
    for(int l=0;l < LINHAS;l++){
        cout <<"| ";
        for(int c=0;c < COLUNAS;c++ ){
            cout << m[l][c] <<" ";
        }
        cout <<"|" << endl;
    }
    cout <<endl;
}

double calcular_media_matriz(int m[][COLUNAS]){
    double somatorio=0; 

    for(int l=0;l < LINHAS;l++)
         for(int c=0;c < COLUNAS;c++ )
            somatorio += m[l][c];

   return somatorio/(LINHAS * COLUNAS);     
}

int main(){
    int dados[LINHAS][COLUNAS]={{0},{0}};
    imprimir_matriz(dados);
    ler_dados_matriz(dados);
    imprimir_matriz(dados);
    double media = calcular_media_matriz(dados);
    cout <<"MEDIA: " <<setprecision(3)<<fixed << media << endl;
}

```



\bibliography