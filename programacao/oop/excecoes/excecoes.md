---
title: Tratamento de Exceções
summary: 
date: 2021-09-13 08:39:00
authors:
    - Diego A. Lusa
---

As exceções representam eventos que comprometem o fluxo normal de execução dos programas. Embora consideradas uma situação anômala, as exceções são comuns e precisam ser consideradas no código em tempo de implementação.

Nas linguagens orientadas a objetos, o evento de *runtime* lança um objeto que representa a exceção que ocorreu. A partir deste objeto podemos então realizar o tratamento, representado por instruções que representam as ações de contorno.

O recurso que boa parte das linguagens de programação oferece é envolver as instruções passíveis de erros em *runtime* com um bloco de tratamento. É comum que este bloco utilize as palavras reservadas `try` e `catch`. Vamos analisar o funcionamento a partir de um exemplo escrito em Java.

Nosso código faz a leitura de um arquivo *README.md*, imprimindo na saída padrão cada linha de conteúdo. A leitura de arquivos é suscetível a diversos problemas: falta de permissão, arquivo inexistente, arquivo corrompido, entre outros. Sabendo disso, é prudente (e mandatório no Java) construirmos o código pensando na possibilidade do erro. 

O primeiro passo compreende envolver as instruções do fluxo normal de execução com `try`. Após, criamos um ou mais blocos `catch` para tratar a possível ocorrência da exceção indicada pelo tipo (*FileNotFoundException* e *IOException* ).

Se, ao executar uma das instruções dentro do bloco `try` ocorrer algum erro, o fluxo é desviado para o bloco de tratamento (`catch`) que melhor adere ao tipo de evento ocorrido. Tal mecanismo de *match* faz uso do relacionamento de herança para determinar o tipo mais específico compatível com a exceção gerada.

=== "Java"
    ```java linenums="1" hl_lines="1 6 8"
        try {
            File arq = new File("README.md");
            BufferedReader reader = new BufferedReader(new FileReader(arq));
            reader.lines().forEach(System.out::println);
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado. Informe o caminho correto");
        } catch (IOException e) {
            System.out.println("Problema geral de entrada e saída");
        }
    ```

Observe como é semelhante em Python. A construção e operação são equivalentes, mudando apenas a palavra reservada de `catch` para `except`.

=== "Python"
    ```python linenums="1" hl_lines="1 4 6"
        try:
            arquivo = open('READMEs.md')
            [print(line) for line in arquivo.readlines()]
        except FileNotFoundError:
            print('Arquivo não encontrado')
        except Exception:
            print('Erro genérico')
    ```

As linguagem de programação apresentam taxionomias de exceções no *core* de suas APIs. Elas normalmente representam situações de erro genéricos e podem ser utilizadas para mapear as exceções mais frequentes que um programa incorre [@psfexceptions2021] [@tutpointsjavaexceptions21]. Outras exceções específicas podem ser criadas pelo desenvolvedor a partir da derivação das genéricas, a fim de representar erros de mais alto nível (como notificar um CPF inválido). Veja na sequência a hierarquia de exceções nativas da linguagem Java.

![Hierarquia de exceções no Java](img/java-exceptions-hierarchy-example.png)
<small>Fonte: <a href="https://rollbar.com/blog/java-exceptions-hierarchy-explained/">https://rollbar.com/blog/java-exceptions-hierarchy-explained/</a></small>

Há uma terceira seção, opcional, que podemos agregar ao tratamento de exceções chamada `finally`. É aplicada para comandos que devem ser executadas em qualquer circunstância, tanto no fluxo normal quanto na eventual ocorrência de exceções.




=== "Python"
    ```python linenums="1" hl_lines="8"
        try:
            arquivo = open('README.md')
            [print(line) for line in arquivo.readlines()]
        except FileNotFoundError:
            print('Arquivo não encontrado')
        except Exception:
            print('Erro genérico')
        finally:
            print('Processamento concluído')
    ```
=== "Java"
    ```java linenums="1" hl_lines="10"
        try {
            File arq = new File("README.md");
            BufferedReader reader = new BufferedReader(new FileReader(arq));
            reader.lines().forEach(System.out::println);
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado. Informe o caminho correto");
        } catch (IOException e) {
            System.out.println("Problema geral de entrada e saída");
        } finally {
            monitor.notificarProcessamento("README.md");
        }
    ```

## Unchecked exceptions e checked exceptions

É uma subdivisão das exceções utilizada na linguagem Java. `Checked exception` é toda aquela exceção verificada em tempo de compilação. Para estas, é exigido que seja feito tratamento via  `try-catch` ou que o método seja declarado com a cláusula `throws`. `Checked exception` são classes derivadas de `Exception`.

`Unchecked exceptions`, por sua vez, não são verificadas em tempo de compilação. Podem ocorrer durante a execução do programa, pois dependem de situações do ambiente e do próprio estado de execução. Acesso a índices inexistentes em arrays, divisão por zero, chamada de método em referências nulas são exemplos deste tipo de exceção. `Unchecked exception` são classes derivadas de `RuntimeException`.


## Exceções customizadas

Quando precisamos notificar os usuários de nossos métodos acerca de uma situação considerada inválida, é boa prática criarmos uma exceção customizada para tal finalidade. A nova exceção deve ser derivada de outra existente, normalmente uma das nativas conforme determina a boa prática. 

No código que segue está sendo definida a classe `SaldoInsuficienteException`, que irá representar um novo tipo de exceção no programa.

=== "Java"
    ```java linenums="1"
        public class SaldoInsuficienteException extends Exception {
            private static final long serialVersionUID = 1L;
            public SaldoInsuficienteException(String mensagem) {
                super(mensagem);
            }
        }	

        public class Conta{
            //...atributos e métodos anteriores...
            public void sacar(double valor) throws SaldoInsuficienteException{
                if ((this.saldo + this.limite) >= valor)
                    this.saldo -= valor;
                else
                    throw new SaldoInsuficienteException(String.format("Não é possível retirar %f da conta %s", valor, this));
            }
        }
    ```


\bibliography