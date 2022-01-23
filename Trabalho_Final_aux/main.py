# plotar um gráfico de mapa das 100 melhores faculdades do mundo
import pandas as pd
from pyspark.sql.session import SparkSession
from IPython.display import display 
import matplotlib.pyplot as plt 

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType)

import pyspark.sql.functions as F

#local[4] portas
spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

path = "D:\scripts\World_University_Rankings\cwurData.csv"

df = spark.read.load(path, format='csv', sep=',', inferSchema='true', header='true')

'''
print('printSchema')
print(df.printSchema())
print(type(df))
print(df.show(5))
'''
print(df.printSchema())

def paises(df):
    colunas = ['country', 'institution', 'world_rank', 'year']
    df_country = df.toPandas().filter(items = colunas)

    #print(type(df_country))
    print(df_country)

    #Retorna a lista de paises
    #graf = df_country.groupby('country').count()
    #print(graf)

    #retorna o numeor de linhas
    #print(df_country.count()) #2200

    #quantas vezes cada pais aparece
    #quant = (df_country["country"]).value_counts()
    #print(quant)

    #print(df.world_rank)
    #graf = df_country.groupby('world_rank').count()
    #print(graf)

    #mostra as que tem rank 1
    #print(df_country.loc[df_country['world_rank'] == 1])
    
    #imprime os anos
    #print((df_country["year"]).value_counts())
    '''
    2014    1000
    2015    1000
    2012     100
    2013     100
    '''

    print('teste')
    
    #aux = df_country[df_country.year == 2013].groupby('world_rank').count()
    #asa 100 melhores
    #ATÉ 60
    
    year_2015 = df_country[(df_country.year == 2015) & (df_country.world_rank <= 100)]
    year_2014 = df_country[(df_country.year == 2014) & (df_country.world_rank <= 100)]

    #display(year_2015)
    #print(year_2015.groupby('country').count())
    #print(df_country["country"].value_counts())
    #year_2014.plot.pie(subplots=True)
    
    melhores = df_country[(df_country.year == 2015) & (df_country.world_rank <= 5)]
    #print(melhores.groupby('institution').count())
    
    graf = melhores.groupby('institution').count()
    plt.style.use("ggplot")

    #print(df_country["institution"].value_counts())
    print('teste')
    tt = melhores.filter(items = ['institution', 'country']).groupby('institution').count()

    display(tt)
    
    #print((df_country["country"]).value_counts())
    #ax.set_yticks(y_pos)
    #ax.set_yticklabels(people)
    print(df_country['country'])
    
#tabelha que retorna o rank
def tabela_rank(df, quant):
    colunas = ['world_rank', 'institution', 'country', 'year']
    df_country = df.toPandas().filter(items = colunas)

    year_2015 = df_country[(df_country.year == 2015) & (df_country.world_rank <= quant)]
    year_2014 = df_country[(df_country.year == 2014) & (df_country.world_rank <= quant)]
    year_2013 = df_country[(df_country.year == 2015) & (df_country.world_rank <= quant)]
    year_2012 = df_country[(df_country.year == 2014) & (df_country.world_rank <= quant)]

    display(year_2015, year_2014, year_2013, year_2012)



#chamando as funções 
#paises(df)
tabela_rank(df, 60)


#https://www.youtube.com/watch?v=ncK5-nQS4lE


