from pymongo import collection
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

#Situação financeira em relação à educação (6, 7)
def financeira_educacao(df):
    #cria um DataFrame com duas colunas
    df_new = df[['financial_situation', 'education', '_id', 'do_children_have_internet_connection']]
    
    #gráfico em barras
    '''
    y = df_new["education"]
    x = df_new["financial_situation"]
    plt.bar(x, y)
    plt.title('Situação financeira em relação à educação')
    plt.show()
    '''

    #gráfico de pizza da educação
    '''
    graf = (df_new["education"]).value_counts()
    graf.plot.pie(autopct='%1.1f%%', shadow=True) 
    plt.show()
    '''
    
    #mostra todos que tenham determinada situação financeira
    '''
    teste = df_new[(df_new['financial_situation'] == "I can comfortably afford food, clothes, and furniture, and I have savings")]
    #print(teste)
    '''

    #mostra todos tenham determinada situação financeira e educaçã e conexão com a internet 
    '''
    teste3 = df_new[(df_new['financial_situation'] == "I can comfortably afford food, clothes, and furniture, and I have savings") & (df_new['education'] == "University or college degree completed") & (df_new['do_children_have_internet_connection'] == '1')]
    #print(type(teste3))
    '''

#chamando a função e passando como parâmetro do DataFrame
financeira_educacao(df)