---
title: "Structured Query Language - SQL"
excerpt: ""
tags:
 - Banco de Dados
 - SQL
date: 2020-02-14 18:00:00
toc: true
order: 2
sidebar:
  nav: "db"
---



## Data Definition Language

## Data Manipulation Language

### Comando INSERT
{: .notice--info}

Responsável por adicionar novas linhas a uma tabela, o comando INSERT apresenta sintaxe muito simples, embora com algumas variações. A forma trivial de escrevê-lo é especificando todas as colunas da tabela e os seus respectivos valores. Observe o trecho de código a seguir:

```sql
INSERT INTO quote
            (id,
             entrance_exam_id,
             NAME,
             reference_code,
             description,
             comment,
             is_universal_access)
VALUES      (1,
             1,
             'ACESSO UNIVERSAL',
             '1',
             'Vagas de acesso universal',
             '',
             true); 
```
Para ter sucesso na execução, o comando `insert` deve respeitar a sintaxe e as `constraints` definidas para as colunas da tabela. **Todas** as colunas obrigatórias (`not null`) devem aparecer no comando, com exceção daquelas que possuem valor `default`, que podem ser omitidas. 

Ainda, quando a(s) coluna(s) representam chaves estrangeiras, os valores informados devem respeitar a *integridade referencial*, ou seja, devem estar presentes como valores de chave primária na tabela referenciada. E, para não esquecer, os valores informados devem respeitar o *domínio* de dados da coluna.

Quando há necessidade de adicionar múltiplas linhas em uma tabela não precisamos repetir diversas vezes o comando `insert`. Nestes casos, é possível informar vários valores de tupla (linha) na cláusula **VALUES**. No exemplo abaixo, o resultado da execução será a inserção de duas linhas na tabela `produto`.

```sql
INSERT INTO produto 
        (id, 
        nome                    
        )
VALUES
        (default,'Lápis'), 
        (default,'Caneta');
```

Outra variação de grande utilidade é a possibilidade de substituir **VALUES** por um comando de **SELECT**. Observe:


```sql
INSERT INTO produto 
        (
        nome                    
        )
SELECT 
    item_nome 
FROM
    item_nota_fiscal
WHERE 
    tipo = 'P';
```

Por fim, o PostgreSQL possibilita o retorno de valores em comandos de `insert` através da cláusula `returning`. Esse recurso é especialmente útil para obter valores de colunas configuradas como `default`, incluíndo tipos seriais utilizados em chaves primárias, bem como para comandos de PL/SQL que envolvem a atribuição de variáveis ([Vide Documentação](https://www.postgresql.org/docs/current/sql-insert.html)).

No exemplo abaixo, o comando `insert` irá retornar o valor gerado para a coluna `id`, tal qual faria um comando `select` análogo.
```sql
INSERT INTO produto 
        (id,
        nome                    
        ) 
VALUES
      (default,
      'Pão')
RETURNING id;
```

### Comando DELETE
{: .notice--info}

A exclusão de linhas de uma tabela é realizada pelo comando `delete`. Não confunda, portanto com o comando `drop`, cuja finalidade é remover do dicionário (schema) a definição e dados (se houver) de um objeto existente na base de dados.


O comando `delete` não requer a especificação de filtros. Neste caso, **todas** as linhas da tabela serão removidas, o que pode ser imprudente. Normalmente todo comando `delete` acompanha condições que determinam quais linhas devem ser excluídas dentre todas as existentes. Tais condições são expressas na cláusula **WHERE**, na forma de condições lógicas.

```sql

--irá excluir todas as linhas da tabela estudante
DELETE FROM estudante;

/*irá excluir somente as linhas 
cujas condições forem satisfeitas*/

DELETE FROM estudante 
  WHERE
      cpf = '012365478963' or
      status = 'C';
```

A exclusão das linhas somente ocorre quando nenhuma `constraint` for violada. Casos típicos são linhas referenciadas em chaves estrangeiras, as quais não podem ser excluídas pois implicaria na violação da **restrição de integridade referencial**. 

Um meio de contornar a restrição e permitir a exclusão da linha com dependência é valer-se da cláusula **ON DELETE CASCADE** no momento de criar a chave estrangeira. Isso, contudo, irá depender das regras do negócio, que por vezes tornam inviável o uso de tal recurso. Pense, por exemplo, se ao excluir o registro de uma cidade, todos os dados de habitantes a ela associados fossem excluídos automaticamente. Certamente não parece ser a melhor estratégia.


Da mesma forma que ocorre com o comando **INSERT**, o PostgreSQL possibilita o retorno de valores em comandos de `delete` através da cláusula `returning`. Observe o comando abaixo ([Vide Documentação](https://www.postgresql.org/docs/current/sql-delete.html)):


```sql
DELETE FROM produto 
WHERE data_validade > current_date - interval '10 days' 
returning id, nome;
```

### Comando UPDATE
{: .notice--info}

Para realizar modificações em dados armazenados, utilizamos o comando **UPDATE**. Por meio dele é possível alterar valores de uma ou mais colunas da linha (ou linhas) de uma tabela.

Se definido sem filtros, a alteração solicitada será efetivada em todas as linhas, contudo nos cenários triviais de uso, este não é o objetivo pretendido. Normalmente utilizamos condições que restringem o efeito da atualização para uma quantia menor de linhas.


```sql
--Todas as linhas de produto terão o valor da coluna nome alterado para Feijão
UPDATE produto SET nome = 'Feijão';

--O mesmo comando, agora com filtro
UPDATE produto SET nome = 'Feijão' 
        WHERE codigo = 25;
```

No comando `update` podemos especificar apenas uma tabela. A partir da cláusula `set` informamos qual será o novo valor das colunas que desejamos modificar. É possível informar uma ou mais colunas na mesma instrução, assim como utilizar o valor atual de colunas para compor novos. Observe:

```sql
--Modificando várias colunas em uma única instrução

UPDATE produto 
SET nome = 'Feijão', preco=4.86, peso=2000 
WHERE codigo = 25;

--Novos valores de coluna com base nos atuais

UPDATE produto 
SET preco= preco+ preco * 0.05 
WHERE codigo = 25;
```

Você deve ter observado que a cláusula `set` é uma sequência de pares de coluna/valor separados por vírgula. Utilizando o trecho `preco= preco + preco * 0.05` como exemplo, percebemos que à esquerda da igualdade temos o nome da coluna que terá o valor modificado, enquanto que na direita encontramos o novo valor. Quando o nome de uma coluna aparece na direita (nosso exemplo), estamos lendo o valor atual para utilizá-lo de alguma forma na composição do novo. Assim, supondo que a coluna `preco` tenha por valor atual `2.40`, o novo valor será o resultado da expressão `2.40 + 2.40 * 0.05`, ou seja, `2.52`.



O PostgreSQL possibilita o retorno de valores em comandos `update` através da cláusula `returning`. Observe o comando abaixo ([Vide Documentação](https://www.postgresql.org/docs/current/sql-update.html)):


```sql
UPDATE produto 
SET nome = 'Feijão', preco = preco * 0.15 
WHERE codigo = 25 RETURNING preco;
```

### Comando SELECT
{: .notice--info}

Certamente podemos afirmar que o comando [**select**](https://www.postgresql.org/docs/current/sql-select.html) é um dos mais importantes da linguagem SQL. Isso porque através dele temos condições de recompor as informações do mundo fragmentados nas diferentes tabelas da base, respondendo às consultas dos usuários. A informação é, portanto, o que se busca apresentar nos diferentes softwares que construímos para interagir com bases de dados. 

Proporcional a importância do comando **select** é a sua complexidade e variação de sintaxe. Logo, extrair todo potencial do comando pode levar certo tempo de estudo e dedicação.

Em termos gerais, o comando **select** representa o meio que temos, em bases relacionais, para recuperar dados. O seu retorno representa uma **relação** (nome formal dado às tabelas), uma vez que falamos em um retorno estruturado em linhas e colunas.

Vamos começar nosso estudo entendendo as principais seções que compõem o comando **select**. Para tal, considere o código SQL abaixo:

```sql
select medico_id,
       paciente_id,
       anamnese,
       data_hora_alta
from
        internacao
```

Observe a cláusula **from**. Nela especificamos a(s) relação(ões) que iremos consultar. A tabela `internacao` é nossa relação e estamos interessados em recuperar as linhas que ela contém. 

Sabemos que relações são segmentadas em colunas e, na consulta, podemos limitar a quais delas gostaríamos de receber no retorno. Portanto, somente as colunas `medico_id`, `paciente_id`, `anamnese` e `data_hora_alta` de todas as linhas armazenadas em `internacao` serão retornadas. Perceba que a lista de colunas deve ser expressa entre as cláusulas **select** e **from**, utilizando vírgula como caractere separador e respeitando a nomenclatura utilizada no momento da criação da tabela. Para os casos onde todas as colunas devem estar presentes na saída, utilizamos um asterisco para simplificar a escrita da consulta. Neste caso, teríamos:

```sql
select * from internacao
```

Bem, e se você preferir mudar o nome de saída da coluna...como faria? Neste caso, basta utilizar o recurso de troca de nomes (*rename*). Veja:


```sql
select medico_id as "codigo do médico",
       paciente_id paciente,
       anamnese,
       data_hora_alta as saida_paciente
from
        internacao
```

Ao optar por renomear colunas, quando utilizamos nomes compostos com espaços entre as palavras, será preciso envolver com aspas duplas (`medico_id as "codigo do médico"`). O operador **as** é opcional, logo fica a seu critério utilizá-lo ou não. Apenas mantenha um padrão de escrita, aderindo a uma das formas apenas.

**Atenção:** A operação *rename* não realiza alterações de schema. Seu efeito vale apenas no contexto da query.
{: .notice--warning}

Além de nomes de colunas, podemos solicitar saída de expressões. É possível, por exemplo, realizar chamadas de funções, cálculos matemáticos e até fazer uso de *subqueries* no espaço reservado às colunas. Contudo, precisamos utilizar tais liberdades com moderação, pois em alguns casos podemos comprometer o desempenho da consulta (veremos estas situações em outro post). 


```sql
select 
       upper(anamnese),
       age(data_hora_alta) as tempo_de_saida,
       3*9 as calculo   
from
        internacao
```

Até o momento sabemos como especificar as colunas (ou expressões) e a relação para nossas consultas via **select**. Da forma que apresentamos até então, **todas** as linhas da relação serão retornadas, uma vez que não definimos **filtros** para os dados. É pouco provável que suas *queries* considerem a integralidade de linhas de uma tabela, logo saber restringir o retorno apenas as linhas de interesse é de fundamental importância. 

A cláusula que nos permite condicionar linhas ao retorno chama-se **where**. Nela, expressamos as restrições na forma de condições lógicas, elaboradas por meio de operadores de comparação (`< > = <= >= <>`) e conectores lógicos (`NOT AND OR`) envolvendo colunas e/ou expressões.

```sql
select 
        * 
from
   internacao
where
   data_hora_internacao > 
        current_timestamp - interval '3 days'
   and tipo_clinica = 'M'
```

Na query acima, condicionamos ao retorno linhas da tabela `internacao` que possuem valor igual a `M` na coluna `tipo_clinica` e cuja `data_hora_internacao` registra uma estampa de tempo de até 3 dias. 

## Junções Internas