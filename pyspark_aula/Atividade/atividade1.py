import findspark
from pyspark import rdd

from pyspark.sql.types import (  IntegerType, StringType, TimestampType,StructType,  StructField, ArrayType, FloatType)

findspark.init() #D:\spark-3.1.2-bin-haddoop2.7

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("atividade") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()

#criando seção

###Extract###
sc = spark.sparkContext
rdd = sc.textFile('D:\scripts\/adult_data.csv')
###Extract###



shema = StructType([StructField("id", IntegerType()),
                    StructField("age", IntegerType()),
                    StructField("workclass", StringType()),
                    StructField("fnlwgt", IntegerType()),
                    StructField("education", StringType()),
                    StructField("education_num", IntegerType()),
                    StructField("marital", StringType()),
                    StructField("occupation", StringType()),
                    StructField("relationship", StringType()),
                    StructField("race", StringType()),
                    StructField("sex", StringType()),
                    StructField("capital_gain", IntegerType()),
                    StructField("capital_loss", IntegerType()),
                    StructField("hours_week", StringType()),
                    StructField("native_country", StringType()),
                    StructField("label", StringType())
])

# Imprima o Schema final desse DF

path = "D:\scripts\/adult_data.csv"

print('testeeeeee')

df = spark.read.format("csv") \
    .schema(shema) \
    .load(path) 
df.printSchema()

# Imprima os 5 primeiros itens do DF.

df.show(5)

# Converta o campo idade do tipo inteiro para o tipo float.

def converterColuna(df, nomes, novotipo):
    for nome in nomes:
        df = df.withColumn(nome, df[nome].cast(novotipo))
    return df

colunas = ['age']
df = converterColuna(df, colunas, FloatType())
df.printSchema()

# Exiba somente 5 itens com os campos ‘age’ e ‘education’

print("Exiba somente 5 itens")
df.select('age', 'education').show(5)

# Agrupe a quantidade de itens em ‘education’ ordenados de maneira ascendente.

df.groupby('education').count().sort('count', ascending=True).show()

# Exiba um describe da tabela ‘capital_gain’

df.describe('capital_gain').show()
