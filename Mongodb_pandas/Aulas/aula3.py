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

    return client['Banco_teste2']#Base de dados

dbname = get_database()

collection_name = dbname["Atividades"]

detalhes_itens = collection_name.find()#aqui pode ser qualquer consulta

df = pd.DataFrame(list(detalhes_itens))
#display(df.head(4))
#display(df.head(4).dtypes)
print(df.head(4).dtypes)