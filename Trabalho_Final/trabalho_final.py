import pandas as pd
from pyspark.sql.session import SparkSession
from IPython.display import display 
import matplotlib.pyplot as plt 
from pymongo import MongoClient
plt.style.use("ggplot")
import pyspark.sql.functions as F
import re
from pymongo import collection
from pymongo.results import InsertManyResult

spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

cwur = "D:\scripts\World_University_Rankings\cwurData.csv"
shanghaiData = "D:\scripts\World_University_Rankings\shanghaiData.csv"

df_cwur = spark.read.load(cwur, format='csv', sep=',', inferSchema='true', header='true')

shanghaiData = spark.read.load(shanghaiData, format='csv', sep=',', inferSchema='true', header='true')


#print(shanghaiData.printSchema())

############################# função que retorna o rank #############################

#dataset da Arábia Saudita
def rank_df_cwur(df, quant):

    colunas = ['world_rank', 'institution', 'year']

    #converte para Pandas e filta as colunas
    df_rank = df.toPandas().filter(items = colunas)

    #função que retorna uma tabela do top 10 de CADA ano 
    def year(ano):
        year = df_rank[(df_rank.year == ano) & (df_rank.world_rank <= quant)]
        display(year)

    print("*** Top10 (2012) - Center for World University Rankings (Arábia Saudita) ***")
    year(2012)
    print("*** Top10 (2013) - Center for World University Rankings (Arábia Saudita) ***")
    year(2013)
    print("*** Top10 (2014) - Center for World University Rankings (Arábia Saudita) ***")
    year(2014)
    print("*** Top10 (2015) - Center for World University Rankings (Arábia Saudita) ***")
    year(2015)

    year_total =  df_rank[(df_rank.world_rank <= quant)]

    quant_rank_10 = year_total.filter(items = ['world_rank', 'institution']).groupby('institution').count()

    #ordenando
    quant_rank_10 = quant_rank_10.sort_values(by='world_rank')
    
    #retorna a tabela do top 10 de TODOS os anos
    print("############## Universidades que ocuparam o top 10 (2012, 2013, 2014, 2015) ##############")
    display(quant_rank_10)

    #gráfico do top 10 de TODOS os anos
    quant_rank_10.plot.barh()

    plt.title("\nUniversidades que ocuparam o top 10 (2012, 2013, 2014, 2015) \n")
    plt.xlabel("quantidade de vezes no top 10")
    plt.ylabel(" ")
    plt.show()

    return year_total

##########################################################

def rank_df_shanghaiData(df, quant):

    colunas = ['world_rank','institution', 'year']

    #converte para Pandas
    shanghaiData = df.toPandas()

    #renomeia a coluna
    shanghaiData = shanghaiData.rename(columns={'university_name':'institution'})

    #filtra as colunas
    shanghaiData = shanghaiData.filter(items = colunas)

    #substituindo o nome da faculdade para padronizar
    shanghaiData = shanghaiData.replace({'institution': {'University of California-Berkeley': 'University of California, Berkeley'}})
    
    #função que retorna uma tabela do top 10 de CADA ano 
    def year(ano):
        year = shanghaiData[(shanghaiData.year == ano)]
        year = year[0:100]
        year = year.astype({'world_rank' :'int'})
        year = year[(year.world_rank <= quant)]

        display(year)

        return year

    print("*** Top10 (2012) - Academic Ranking of World Universities- Shanghai ***")
    year_2012 = year(2012)
    print("*** Top10 (2013) - Academic Ranking of World Universities- Shanghai ***")
    year_2013 = year(2013)
    print("*** Top10 (2014) - Academic Ranking of World Universities- Shanghai ***")
    year_2014 = year(2014)
    print("*** Top10 (2015) - Academic Ranking of World Universities- Shanghai ***")
    year_2015 = year(2015)


    #join
    year_total = pd.concat([year_2012, year_2013, year_2014 , year_2015],ignore_index=True)
  
    #retorna a tabela do top 10 de TODOS os anos
    year_total =  year_total[(year_total.world_rank <= quant)]
    quant_rank_10 = year_total.filter(items = ['world_rank', 'institution']).groupby('institution').count()
    
    #ordenando
    quant_rank_10 = quant_rank_10.sort_values(by='world_rank')

    #retorna a tabela
    print("############## Universidades que ocuparam o top 10 (2012, 2013, 2014, 2015) ##############")
    display(quant_rank_10)

    #gráfico do top 10 de TODOS os anos
    quant_rank_10.plot.barh()

    plt.title("\nUniversidades que ocuparam o top 10 (2012, 2013, 2014, 2015) \n")
    plt.xlabel("quantidade de vezes no top 10")
    plt.ylabel(" ")
    plt.show()

    return shanghaiData


def df_shanghaiData(df):
    colunas = ['world_rank','institution', 'year', 'alumni', 'award', 'hici', 'ns', 'pub', 'pcp']

    #converte para Pandas
    shanghaiData = df.toPandas()

    #renomeia a coluna
    shanghaiData = shanghaiData.rename(columns={'university_name':'institution'})

    #substituindo o nome da faculdade para padronizar
    shanghaiData = shanghaiData.replace({'institution': {'University of California-Berkeley': 'University of California, Berkeley'}})

    #filtra as colunas
    shanghaiData = shanghaiData.filter(items = colunas) 

    #função que retorna as 100 melhores faculdades do ano especificado
    def year(ano):
        year = shanghaiData[(shanghaiData.year == ano)]
        year = year[0:100]
        year = year.astype({'world_rank' :'int'}) #mudando o tipo para int
        return year

    #lista de anos
    index = ((shanghaiData["year"]).value_counts()).index

    #100 melhores faculdades de todos os anos
    year_total = pd.DataFrame()
    for i in index:
        tabela = year(i)
        year_total = pd.concat([year_total, tabela],ignore_index=True)

    #5 melhores faculdades atuais(2015)
    melhores_2015_10 = year_total[(year_total.world_rank <= 10) & (year_total.year == 2015)]

    #ordenando o valores por rank mundial
    melhores_2015_10 = melhores_2015_10.sort_values(by='world_rank')

    #pegando o nome das 5 melhores faculdades atuais(2015)
    melhores_2015_10_name = ((melhores_2015_10["institution"]).value_counts()).index

    #pegando todos os anos
    year_total_name = ((year_total["institution"]).value_counts()).index

    #procurando as 5 melhores faculdades atuais(2015) nos anos anteriores
    melhores_universidades = pd.DataFrame()
    for i in melhores_2015_10_name:
        for j in year_total_name:
            if(i == j):
                uni = year_total[(year_total.institution == i)].sort_values(by='year')
                melhores_universidades = pd.concat([melhores_universidades, uni],ignore_index=True)
              

    #pegando os dados das 5 melhores faculdades atuais(2015)
    aux = melhores_universidades[ 
        (  melhores_universidades['institution'] == 'Harvard University') \
        | (melhores_universidades['institution'] == 'Stanford University') \
        | (melhores_universidades['institution'] == 'Massachusetts Institute of Technology (MIT)') \
        | (melhores_universidades['institution'] == 'University of California, Berkeley') \
        | (melhores_universidades['institution'] == 'University of Cambridge')
        | (melhores_universidades['institution'] == 'Princeton University')
        | (melhores_universidades['institution'] == 'California Institute of Technology	')
        | (melhores_universidades['institution'] == 'Columbia University')
        | (melhores_universidades['institution'] == 'University of Chicago')
        | (melhores_universidades['institution'] == 'University of Oxford')
        ] 
 
    #imprime tablela das 5 melhores faculdades atuais(2015) 
    print('***** 5 melhores faculdades atuais(2015) *****')
    display(melhores_2015_10.filter(items = ['world_rank', 'institution', 'year']))


    def grafico(colunas_graf, titulo, ylabel, xlabel):
        graf =  aux.filter(items=colunas_graf).groupby(['year', 'institution']).mean().unstack().plot(figsize = (5,5), colormap = 'Set1')

        #labels
        graf.set_ylabel(ylabel)
        graf.set_xlabel(xlabel)

        #titulo
        graf.set_title(titulo, fontsize=(20))

        #legenda
        handles, labels = graf.get_legend_handles_labels()
        new_legend = [re.search(',\s(.+?)\)', label).group(1) for label in labels]
        graf.legend(new_legend, bbox_to_anchor = (1,1), loc = 0)

        plt.show()

    #gráfico 10 melhores faculdades atuais(2015) 

    # colunas_graf | titulo | ylabel | xlabel
    grafico(['year', 'award', 'institution'],\
    'Funcionários que ganhou prêmios Nobel e medalhas Fields X Ano',\
    'Funcionários(prêmios Nobel e medalhas Fields)',\
    'Anos')

    grafico(['year', 'hici', 'institution'],\
    'Pesquisadores altamente citados X Ano',\
    'Pesquisadores altamente citados',\
    'Anos')

    grafico(['year', 'ns', 'institution'],\
    'Artigos publicados na Nature and Science X Ano',\
    'Artigos publicados',\
    'Anos')

    grafico(['year', 'pub', 'institution'],\
    'Artigos indexados X Ano \n(Science Citation Index-Expanded e Social Science Citation Index)',\
    'Artigos indexados',\
    'Anos')

    grafico(['year', 'alumni', 'institution'],\
    'Qualidade da Educação X Ano\n(Ex-alunos de uma instituição que ganha prêmios Nobel e medalhas Fields)',\
    'Ex-alunos (Nobel e/ou medalhas Fields)',\
    'Anos')
    
    grafico(['year', 'pcp', 'institution'],\
    'Desempenho acadêmico per capita X Ano',\
    'Desempenho acadêmico per capita',\
    'Anos')

    return shanghaiData


############################# Chamando as funções #############################

mongodb = MongoClient("mongodb+srv://admin:d7BCRVM11Exx99TF@cluster0.krmag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")['projeto-final']

# Center for World University Rankings
rank_df_cwur(df_cwur, 10)
#mongodb['df_cwur_rank_heloise'].insert_many(rank_df_cwur(df_cwur, 10).to_dict('records'))

# Academic Ranking of World Universities Shanghai
rank_df_shanghaiData(shanghaiData, 10)
#mongodb['df_shanghaiData_rank_heloise'].insert_many(rank_df_shanghaiData(shanghaiData, 10).to_dict('records'))

#datframe shanghai 
df_shanghaiData(shanghaiData)
#mongodb['df_shanghaiData_heloise'].insert_many(df_shanghaiData(shanghaiData).to_dict('records'))
