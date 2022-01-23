# plotar um gráfico de mapa das 100 melhores faculdades do mundo
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
lst_log = "D:\scripts\lat_long\latitude_and_longitude_values.csv"

df_cwur = spark.read.load(cwur, format='csv', sep=',', inferSchema='true', header='true')
 
df_lst_log = spark.read.load(lst_log, format='csv', sep=',', inferSchema='true', header='true')



######################################### MongoDB ###################################################
def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/test"

    from pymongo import MongoClient

    client = MongoClient(CONNECTION_STRING)  #conexão com o cliente

    return client["localizacao"]  #base de dados
    
dbname = get_database()
collection_name = dbname["paises"]

detalhes_itens = collection_name.find()
# consulta o db no Mongo, coloca todos os dados do database nessa variavel.

df_localizacao = pd.DataFrame(list(detalhes_itens)) #criei um df com o banco de dados

######################################################################################################
'''
 |-- country_code: string (nullable = true)
 |-- latitude: double (nullable = true)
 |-- longitude: double (nullable = true)
 |-- country: string (nullable = true)
 |-- usa_state_code: string (nullable = true)
 |-- usa_state_latitude: double (nullable = true)
 |-- usa_state_longitude: double (nullable = true)
 |-- usa_state: string (nullable = true)
'''

############################# tabela que retorna o rank #############################

def tabela_rank(df, quant):
    colunas = ['world_rank', 'institution', 'country', 'year']
    df_rank = df.toPandas().filter(items = colunas)

    year_2015 = df_rank[(df_rank.year == 2015) & (df_rank.world_rank <= quant)]
    year_2014 = df_rank[(df_rank.year == 2014) & (df_rank.world_rank <= quant)]
    year_2013 = df_rank[(df_rank.year == 2013) & (df_rank.world_rank <= quant)]
    year_2012 = df_rank[(df_rank.year == 2012) & (df_rank.world_rank <= quant)]

    display(year_2015, year_2014, year_2013, year_2012)

    year_total =  df_rank[(df_rank.world_rank <= quant)]

    quant_rank_10 = year_total.filter(items = ['world_rank', 'institution']).groupby('institution').count()

    display(quant_rank_10)

    quant_rank_10.plot.bar()
    plt.title("Universidades que ocuparam o top 10 (2012, 2013, 2014, 2015)")
    plt.show()

#############################  #############################

def localizacao(df_localizacao, df):

    colunas = ['world_rank', 'institution', 'country', 'year']
    
    df_rank = df.toPandas().filter(items = colunas)

    df_localizacao = df_localizacao.drop(columns=["_id"])
    #print(df_localizacao.columns)

    year_2015 = df_rank[(df_rank.year == 2015) & (df_rank.world_rank <= 10)]
    year_2014 = df_rank[(df_rank.year == 2014) & (df_rank.world_rank <= 10)]
    year_2013 = df_rank[(df_rank.year == 2013) & (df_rank.world_rank <= 10)]
    year_2012 = df_rank[(df_rank.year == 2012) & (df_rank.world_rank <= 10)]


    lista = []
    lista_year_2015 = year_2015['institution'].values
    lista_year_2014 = year_2014['institution'].values
    lista_year_2013 = year_2013['institution'].values
    lista_year_2012 = year_2012['institution'].values

    print('----------------------------------------------')
    
   

    def list_add(va):
        for i in va:
            lista.append(i)

    list_add(lista_year_2015)
    list_add(lista_year_2014)
    list_add(lista_year_2013)
    list_add(lista_year_2012)

    lista = set(lista)
    lista = list(lista)
    print(lista)
  
    print('----------------------------------------------')


    #res = year_2015.assign(df_localizacao['name'])
    
    #result = pd.merge(year_2015, df_localizacao, how="outer")
    #result = year_2015.join(df_localizacao, lsuffix='_t1', rsuffix='_t2')

    #res = pd.concat([year_2015, df_localizacao])
    #res = pd.merge(year_2015, df_localizacao, how = 'outer')
    #print(result)

    '''
    res = pd.concat([df_rank, df_localizacao])
    print(df_rank['institution'].head(3))
    print(df_localizacao['name'].head(3))

    print(res['institution'].head(3))
    print(res['name'].head(3))
    '''


    #transformando em spark
    #df_localizacao =  spark.createDataFrame(df_localizacao.astype(str))

    #merge
    #res = pd.merge(left: df_localizacao, df, how = 'outer')
    #res = pd.concat([df, df_localizacao])

    #print(res.columns)
    #print(res['institution'], ['nome'])

    #res = spark.createDataFrame(res.astype(str))
    #res.show()
    #po = (res['institution'], ['nome'])
    
    #print(res['institution'].head(3))
    #print(res['name'].head(3))

    #print(res['institution'])
    #print(res['name'])
    #print(res)
   

    #df.show(truncate=False)
    #print(df_localizacao['name'])
    #print(df.toPandas()['institution'])

    #df.toPandas().drop(["usa_state"])
    #print(df)
    #print(df2['country'])
    #colunas = ['world_rank', 'institution', 'country', 'year']
    #df_rank = df.toPandas().filter(items = colunas)

#show(truncate=False)

#localizacao(df_localizacao, df_cwur)

    '''
    auxd.plot()
    graf.plot()	
    #criando um subplot 
    fig, ax = plt.subplots()
    graf.plot(ax = ax)
    grafd.plot(ax = ax)
    '''

    '''
    print((shanghaiData["year"]).value_counts())
    lista = []
    lista.append(index)
    print(index)
    print(len(index))
    print(type(index))
    print(index[10])
    print(lista)
    '''
     

tabela_rank(df_cwur, 10)


