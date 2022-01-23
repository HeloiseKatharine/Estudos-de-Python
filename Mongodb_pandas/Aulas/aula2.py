import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from IPython.display import display 

#################séries#################
notas = pd.Series([10,5,7.5,10])
#print(notas)
#print(notas.values)
#print(notas.index)#começa para pula

#lista, index
#notas2 = pd.Series([10,5,7.5,10], index=['José','Ana', 'Heloise', 'Maria'])
#print(notas2)

#descrição
#print(notas.describe())

#média
#print(notas.mean())

#calcula o quadrado de todos os itens da série
#print(notas**2)

#logaritmo de notas
#print(np.log(notas))



#################Dataframes#################
'''
df = pd.DataFrame(
    {'Alunos':["José","Ana", "Heloise","Maria"],
    'Faltas':[3,4,5,6],
    'prova' :[10,5,57,20],
    'Seminario':[0,2,1,30]
    }
)'''

'''
#professor = 

print(df)#Imprimir    
display(df)#Imprimir com Display
print(df.dtypes)#Imprimir os tipos   
print(df.columns)#Imprimir colunas  
print(df["Aluno"])#Imprimir por nomes de colunas
print(df.describe())#Métodos estatísticos
print(df.sort_values(by="Seminário"))#Ordnar por parâmetro             
print(df.loc[3])#Acessar por index ou rótulo
print(df[df["Seminário"] > 8.0])#Filtrar por valor lógico
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])#Filtrar por combinação Lógica

#Leitura de dados
df_csv = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")
print(df_csv)
print(df_csv.head(3))#Imprime os 3 primeiros registros
print(df_csv.tail(3))#Imprime os 3 últimos registros

#Manipulação
print(df_csv['bairro'].unique())#Exibir únicos
print(df_csv['bairro'].value_counts())#Contar dados
print(df_csv.groupby("bairro").mean())#Agrupar por média de bairros

df2 = df_csv.head()#Cria um dataframe com 5 itens usando o anterior.
df2 = df2.replace({"pm2": {12031.25: np.nan}})#Substitui o 12031 por NaN
print(df2)

df2.dropna()#Remove linhas que possuam erros NaN
print(df2)
df2.fillna(99)#Trocar valores que possuem NaN por outro específico
print(df2)
df2.isna()#Verificar quem é NaN ou não.
print(df2)'''

#print(df)
#display(df)
#print(df.dtypes)
#print(df.columns)
#print()

#ordena
#print(df.sort_values(by= "Seminario"))

#print(df.loc[3])
#print(df[df['Seminario'] > 8.0])

# | e &
#print(df[(df['Seminario']>8.0) | (df['prova'] < 3)])


##################################


df_csv = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")

#print(df_csv)

#primeiros dados
#head tem como padrão 5 primeiros números
#print(df_csv.head(2))

#últimos dados
#print(df_csv.tail(2))

#nomes dos bairros sem repetição
#print(df_csv['bairro'].unique())

#quantidade de vezes que um bairro é citado
#print(df_csv['bairro'].value_counts())

#agrupa o bairro e mostra a média 
#print(df_csv.groupby('bairro').mean())


df2 = df_csv.head()

#subistituindo o pm2 = 12031.25 por NaN | o contrario vale
#print(df2.replace({"pm2":{12031.25:np.nan}}))

#subistitui NaN por 99
#print(df2.fillna(99))

#mostra quem tem erro de NaN e quem não tem
print(df2.isna())

#################graficos#################