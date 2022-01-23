import findspark
from pyspark import rdd
from pyspark.sql import Row
import matplotlib.pyplot as plt 
from pyspark.sql.types import (  IntegerType, StringType, TimestampType,StructType,  StructField, ArrayType, FloatType)

findspark.init() #D:\spark-3.1.2-bin-haddoop2.7

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("atividade") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()


schema = StructType([
      StructField("Country",StringType()),
      StructField("Gold Medal",IntegerType()),
      StructField("Silver Medal",IntegerType()),
      StructField("Bronze Medal",IntegerType()),
      StructField("Total",IntegerType()),
      StructField("Rank By Total",IntegerType())
])

path = "D:\scripts\Tokyo_Medals_2021.csv"

df = spark.read.format("csv") \
    .schema(schema) \
    .load(path) 

# Mudando o nome das colunas
df = df.toDF(*['Pais', 'Medalha de ouro', 'Medalha de prata', 'Medalha de bronze', 'Total', 'Rank By Total'])

df.show(5)
df.printSchema()

#imprime o país que ganhou em primeiro lugar e a quantidade total de medalhas
df.select('Pais', 'Total').filter(df['Rank By Total'] == 1).show()

#imprime o país que ganhou em segundo lugar e a quantidade total de medalhas
df.select('Pais', 'Total').filter(df['Rank By Total'] == 2).show()

#imprime o país que ganhou em terceiro lugar e a quantidade total de medalhas
df.select('Pais', 'Total').filter(df['Rank By Total'] == 3).show()

#imprime todos os países que possuem menos de 10 medalhas ao total
df.select('Pais', 'Total').filter(df['Total'] < 10).show()

#imprime todos os dados do Brasil 
df.select('Pais', 'Medalha de ouro', 'Medalha de prata', 'Medalha de bronze', 'Total', 'Rank By Total').filter(df['Pais'] == 'Brazil').show()

#imprime o DataFrame 
df.show()

#############################################################################

#Carregando outro dataset 
df2 = spark.read.load('D:\scripts\/athletes.csv', format='csv', sep=',', inferSchema='true', header='true') 

#Join
df_and_df2 = df.join(df2,  how ='left')
df_and_df2.limit(10).show()


