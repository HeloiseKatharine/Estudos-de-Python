#https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie
# https://cadernoscicomp.com.br/tutorial/matplot-e-pandas/matplot-e-pandas-em-estatistica-basica-boxplot-e-graficos-pizza-ou-setores/

from pymongo import ASCENDING, collection
from pymongo.results import InsertManyResult
import pandas as pd
import matplotlib.pyplot as plt 
from IPython.display import display 

plt.style.use("ggplot")

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/myFirstDatabase"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['socioeconomico']#Base de dados

dbname = get_database()
collection_name = dbname["venezuela2021"]

detalhes_itens = collection_name.find()#aqui pode ser qualquer consulta

df = pd.DataFrame(list(detalhes_itens))


def educacao(df):
    df_new = df[['education']]
    
    #destaca a coluna com o maior valor
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0)
    colors = ['#FFFF00', '#800080','#B22222','#483D8B','#FA8072','#CD853F','#2E8B57', '#FF4500']
    
    labels = ['Graduação em faculdade completa','Segundo grau (Ensino médio) completo', 'Diploma de escola técnica ou algum título completo','Possui alguma educação universitária','Possui alguma educação técnica','Possui alguma educação secundária/ensino médio', 'Pós-graduação completa','Outros']

    #gráfico de pizza da educação
    graf = (df_new["education"]).value_counts()
    
    # autopct = rotular as fatias com seu valor numérico
    # shadow = sombra | 
    #textprops=dict(color="w")
    graf2 = graf
    soma = sum(graf2.iloc[[12, 13, 14, 15, 8, 11, 10, 7, 9]]) 
    graf2 = graf2.drop(graf2.index[[12, 13, 14, 15, 8, 11, 10, 7, 9]])   
    graf2.loc['Others'] = soma

    graf2.plot.pie(autopct='%1.1f%%', explode= explode, shadow=True, startangle = 90, labels=labels, ylabel='', colors = colors) 
    
    plt.title('Educação na Venezuela')
    plt.show()

def financial_situation_education(df):

    colunas = ['financial_situation', 'education']
    df_new = df.filter(items = colunas)
    
    aux = df_new[(df_new['education'] == 'University or college degree completed') | (df_new['education'] == 'Secondary school/ high school completed') | (df_new['education'] ==  'Technical school diploma or degree completed')]
    
    graf = aux.groupby('financial_situation').count()

    graf.plot.pie(autopct='%1.1f%%', shadow=True, startangle = 90, subplots=True, ylabel='', labeldistance = None)

    L=plt.legend(bbox_to_anchor=(1.1,1.0),\
    bbox_transform=plt.gcf().transFigure)

    #L.get_texts()[0].set_text('Consigo custear alimentos e despesas regulares, mas nada além disso.','Consigo custear alimento, mas nada além disso.','Consigo custear alimentos, despesas regulares e roupas, mas nada além disso', 'Consigo confortavelmente comprar alimentos, roupas e móveis e tenho economias. ', 'Consigo confortavelmente comprar alimentos, roupas e móveis, mas não tenho economias.','Não consigo comprar comida suficiente para a minha família.', 'Prefiro não responder')

    plt.savefig('temp.png') 
    plt.title('Situação finaceira X Educação')
    plt.show()

#financial_situation_education(df) #OK
#educacao(df) #OK





'''
#Situação financeira em relação à educação (6, 7)
def financeira_educacao(df):
    #cria um DataFrame com duas colunas
    df_new = df[['financial_situation', 'education', '_id', 'do_children_have_internet_connection']]
    
    #gráfico em barras
    y = (df_new["education"])
    x = (df_new["financial_situation"])
    plt.bar(x, y)
    plt.title('Situação financeira em relação à educação')
    plt.show()
'''


def funcao_teste(df):
    colunas = ['education','financial_situation', 'do_children_have_internet_connection']
    df_new = df.filter(items = colunas)
    #print(df_new.head())

    '''
    coluna_educacao = df_new['education']#séries
    coluna_finaceira = df_new['financial_situation']#séries
    coluna_internet = df_new['do_children_have_internet_connection']

    coluna_educacao_num = coluna_educacao.value_counts()#quantidade 
    coluna_finaceira_num = coluna_finaceira.value_counts()#quantidade
    coluna_internet_num = coluna_internet.value_counts()
    '''
    
    #print(df_new.groupby('do_children_have_internet_connection').count())
    (df_new.groupby('do_children_have_internet_connection').count()).hist()
    plt.show()


def teste2(df):

    colunas = ['financial_situation', 'do_children_have_internet_connection']
    df_new = df.filter(items = colunas)

    #coluna_educacao = df_new['education']#séries
    coluna_finaceira = df_new['financial_situation']#séries
    coluna_internet = df_new['do_children_have_internet_connection']

    #coluna_educacao_num = coluna_educacao.value_counts()#quantidade 
    coluna_finaceira_num = coluna_finaceira.value_counts()#quantidade
    coluna_internet_num = coluna_internet.value_counts()



    #criando as novas colunas 
    #print(df_new.head())

    #print((df_new.do_children_have_internet_connection == "0").value_counts)
    #print((df_new.do_children_have_internet_connection == "0").count())
    #print(df_new.do_children_have_internet_connection == 1)
    
    #0 = não
    aux = df_new[(df_new['do_children_have_internet_connection'] == "0")]
    
    graf = aux.groupby('financial_situation').count().sort_values(by='do_children_have_internet_connection', ascending = False)
    
    
    graf.plot.pie(subplots=True, ylabel='')
    plt.show()
    #print(graf)
    #graf.plot()
    #aux.groupby('financial_situation').count().hist()




#teste2(df)
#chamando a função e passando como parâmetro do DataFrame
#funcao_teste(df)

