from pandas.core.frame import DataFrame
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

df = pd.DataFrame(list(detalhes_itens))#criando um DataFrame com o dataset 

#imprime o nome da coluna zero 
'''
print(df.columns[0])
'''

#quantidade de colunas do DataFrame
'''
tam = len(df.columns)  
print(tam)
'''

'''
print(df[df['are_there_children_0_to_2_yrs_out_of_educational_system'] == "0"])
'''

#imprime os valores da coluna 'are_there_children_0_to_2_yrs_out_of_educational_system'

'''
print(df['are_there_children_0_to_2_yrs_out_of_educational_system'])
'''

#retorna True se o resultado for zero ou False se o resultado for diferente de zero
'''
print(df['are_there_children_0_to_2_yrs_out_of_educational_system'] == "0")
'''

#retorna as respostas da coluna e a quantidade 
#Ex:
#True     3128
#False    1308
'''
teste = (df['are_there_children_0_to_2_yrs_out_of_educational_system'] == "0").value_counts()
print(teste)
'''

#imprime as repostas da coluna 'submission_state'

teste = (df['education']).value_counts()
print(teste)



#imprime o índice e os nomes das colunas 
'''
for i in range(tam):
    #if df.columns[]
    print(f'{i} = {df.columns[i]}')
    print('\n')
'''


#print(df['are_there_children_0_to_2_yrs_out_of_educational_system'] == "0")

#lista = list(df['are_there_children_0_to_2_yrs_out_of_educational_system'])
#print(lista)
#print(type(lista))
#print(lista[0])
#print(type(lista[0]))

#print(df)
#print(df.info)

##############################Transformando um dataFrame em lista e mudando o tipo dos dados ########################### 
'''

lista = []
lista.append(df['are_there_children_0_to_2_yrs_out_of_educational_system'])

lista_int = []

for i in range(len(lista[0])):
    lista_int.append(int(lista[0][i]))

#print(lista_int)
#print(lista_int[0])
print(type(lista_int[0]))

#transforma lista em DataFrame | tem que colocar em um acoluna 
df_teste = pd.DataFrame(lista_int)

#print(df_teste)
#print(df_teste.dtypes)
#print(df_teste.info)

#print(df_teste[0][1])

#print(df_teste[0].dtypes)

'''
#########################################################
'''
teste = (df['do_children_have_internet_connection'] == "0").value_counts()
print(teste)
'''

'''
teste = df['are_there_children_0_to_2_yrs_out_of_educational_system']
#print(teste)
print(teste.info())

'''
#########################################################

#df.convert_dtypes()
#print(df.dtypes)

#np.dtype("O"))
#astype(str)

#imprime o tipo da coluna _id
#print(df['_id'].dtypes)

#imprime o dados de todo o df 
#print(df.info())

#mudar o tipo da coluna
#print(df['_id'].astype(int64))

#df = df.astype({"a": int, "b": complex})
#print(df.astype({"financial_situation": str}).dtypes)

#df.astype({"do_school_and_the_teachers_have_internet_connection": int})
#df.infer_objects()
#print(df.dtypes)

#print(df['financial_situation'].dtypes
#print(df['financial_situation'].dtypes)

##########################tipos##########################
#print(teste.columns)
#print(teste['financial_situation'])
    
#teste['financial_situation'] = teste['financial_situation'].astype(str)
#print(teste['financial_situation'].dtypes)
    
    
#teste = teste.astype(str)
#teste = teste.infer_objects()
#print(teste['financial_situation'].dtypes)
#print(teste.dtypes)


#print(df.columns.values)
#print(df['financial_situation'])
'''
lala = df['financial_situation'].head()
print(lala)
for i in lala:
    print(f"'{i}',", end = ' ')
'''