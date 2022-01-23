import pandas as pd

arquivo = pd.read_csv("D:\scripts\wine_dataset.csv")

#arquivo.head()

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis=1) #axis = 1 linha | axis = 0 coluna

from sklern.model_selection import train_teste_split

x_treino, x_teste, y_treino, y_teste = train_teste_split(x, y, teste_size = 0.3)




