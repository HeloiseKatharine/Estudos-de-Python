import findspark
from pyspark import rdd

findspark.init() #D:\spark-3.1.2-bin-haddoop2.7

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Aula1") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()

#criando seção

###Extract###
sc = spark.sparkContext
rdd = sc.textFile('D:\scripts\Salary_Data.csv')
###Extract###


###Transform###
#puxa as duas primeiras linhas
#rdd.take(2)

#separa as linhas por vírgula
#map faz com que o dataset se comportem na mandeira que for especificada
rdd = rdd.map(lambda line: line.split(","))

rdd.take(5)

#retorna ao primeiro elemento
#rdd.first()

#criando um DataFrame
#Criando cabeçalho 
from pyspark.sql import Row
df = rdd.map(lambda line: Row(AnosExperiencia = line[0], Salario= line[1])).toDF()
#df.show()

#qual o tipo de dado de cada coluna
df.printSchema()

from pyspark.sql.types import *

#converte o tipo do dado da coluna
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas = ['AnosExperiencia','Salario']

df = converterColuna(df, colunas, FloatType())
#df.show()
df.printSchema()

#mostra os primeiros 5 itens da coluna salario
df.select('Salario').show(5)


#Agrupar salario por contagem e ordená-lo 
df.groupby('Salario').count().sort('Salario', ascending=False).show()

#contar somente
#df.select('Salario').count()

#Dados analiticos
print('describe\n')
df.describe().show()

df.describe('Salario').show()

print('collect\n')

#retorno de matrizes de coleções
df.collect()

print('salario 1 \n')
df.filter(df['Salario'] > 5000).show()
print('salario 2 \n')
df.select('Salario').filter(df['Salario'] < 500000).show



###Transform###