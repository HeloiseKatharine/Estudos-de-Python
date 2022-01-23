
#
from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType, DoubleType)

import pyspark.sql.functions as F

spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '2gb') \
    .config('spark.shuffle.sql.partitons', 2) \
    .getOrCreate()

schema = StructType([StructField("target", StringType()),
                   StructField("_id", IntegerType()),
                   StructField("date", StringType()),
                   StructField("flag", StringType()),
                   StructField("user", StringType()),
                   StructField("text", StringType()),
                  ])
#extract                  
path = 'D:\scripts\/training.1600000.processed.noemoticon.csv'

df = spark.read.format("csv") \
    .schema(schema) \
    .load(path)
#extract

#transform

# Deleta as colunas "target" e "flag"
df = df.drop("target", "flag")

df = df.withColumn("day_week", df.date.substr(1,3)) \
    .withColumn("day", df.date.substr(9,2)) \
    .withColumn("month", df.date.substr(5,3)) \
    .withColumn("time", df.date.substr(12,8)) \
    .withColumn("year", df.date.substr(25,4)) \
    .drop("date")

#.withColumn("year", df.date.substr(25,4).cast(coloca o tipo da coluna))
 
#mudando o tipo da coluna 
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes: 
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe 

#nomes
colunas_iteiro = ['day']
colunas_item = ['time']

df = converterColuna(df, colunas_iteiro, IntegerType())
#df = converterColuna(df, colunas_item, TimestampType())
#transform

#load 

df = df.limit(20)

#df.write.format('json').save('meuDF2.json')
'''
print("Json gerado com sucesso!!")
df.write.format("json").mode("overwrite").save("teste.json")
#df.show(5)
'''


def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/myFirstDatabase"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['Banco_teste2']#Base de dados

dbname = get_database()
collection_name = dbname["Atividades"]

df = df.limit(20)

df = df.toPandas() #transforma em data frame do pandas (para depois transforma em dict)
data_dict = df.to_dict('records')#transforma em dict
collection_name.insert_many(data_dict) #importa 
print("DF importado")
