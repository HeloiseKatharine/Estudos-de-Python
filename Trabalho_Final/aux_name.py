# plotar um gráfico de mapa das 30 melhores faculdades do mundo
import pandas as pd
from pyspark.sql.session import SparkSession
from IPython.display import display 
import matplotlib.pyplot as plt 
from pymongo import MongoClient
#sql
import pyspark.sql.functions as F

spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

cwur = "D:\scripts\World_University_Rankings\cwurData.csv"

df_cwur = spark.read.load(cwur, format='csv', sep=',', inferSchema='true', header='true')

#função que retorna um arquivo txt com a estrutura do dataset maps
def tabela_rank(df):
    colunas = ['world_rank', 'institution', 'country', 'year']
    df_rank = df.toPandas().filter(items = colunas)

    df_rank = df_rank[(df_rank.world_rank <= 30) & (df_rank.year == 2015)]


    lista = df_rank['institution']
    lista = list(lista)

    arquivo = open('dfaculdade.txt','w')

    for linha in range (len(lista)):

        arquivo.write(f"\nitem_{linha} =" + " {\n   'name' :" + f" '{lista[linha]}',"  + "\n    'location': { 'type': 'Point', 'coordinates': [ , ]}\n}" )
    
    arquivo.close()





