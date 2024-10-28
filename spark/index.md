
Spark é uma biblioteca de processamento paralelo de dados. Escrita em Scala. Pode ser utilizada em Python, Scala e Java.

Resilient Distributed DataSets são um dos conceitos chave. Core object que permite distribuir dados em um cluster. Trata falhas automaticamente. É criado pelo programa Driver por meio do objeto SparkContext.

```python

#sc means SparkContext

nums = parallelize ([5,52,3,6])

rddLines = sc.textFile("file:///c:/dados.txt")
hiveCtx = HiveContext(sc)

#could be use JDBC, CSV, JSON, ElasticSearch, etc.

```


Para transformar em RDDs:

- **map**: Transforma de um tipo de RDD para outro por meio de uma função. A mesma quantidade de dados do RDD original terá no RDD resultante do map

```python
rdd = sc.parallelize([5,6,7,8])
rdd.map(lambda y: y*y)
```

- **flatmap**: É similar ao map, mas pode gerar n valores a partir de um único de entrada.
- filter
- distinct
- sample
- union, insersection, subtract, catersian



Acões sobre RDD:

- collect
- count
- countByValue
- take
- top
- reduce


Nada acontece no *driver program* até que uma *action* seja solicitada.


Para iniciar um *driver program* precisamos importar:

```python

from pyspark import SparkConf, SparkContext
import collections
```

Na linha a seguir criamos o objeto de configuração

```python
conf = SparkConf().setMaster("local").setAppName("myApp")
```

O método `setMaster` informa o endereço master para se conectar. Pode ser `local` ou um endereço do cluster. Já o `setAppName` permite localizar as aplicações no Spark Web UI


Verificar:

#https://docs.python.org/3/library/collections.html

spark-submit


Key-Value RDD

RDD somente podem armazenar pares de chave-valor

Para construir podemos utilizar a transformação map:

```python

totalByAge = rdd.map(lambda x: (x,1))

```

O que podemos fazer (transformations):

- mapValues
- flatMapValues

O que podemos fazer (actions):

- reduceByKey
- groupByKey
- sortByKey
- keys
- values


Filtering RDDs

Utilizamos filter para remover dados dos RDDs que não são de interesse a partir de uma função que retorna um valor boleano.


O spark realiza as ações somente ao encontrar o collect().