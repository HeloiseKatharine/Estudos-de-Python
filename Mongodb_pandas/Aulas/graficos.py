import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from IPython.display import display 

plt.style.use("ggplot")

df_csv = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")

nome = ['carlos', 'jose', 'andre']
valores = [5,8,6]

#ipykernel instalar
#plt.plot(nome, valores)
#plt.show()

#gráfico de barras
#df_csv['preco'].plot.hist()
#df_csv['preco'].plot.hist(bins=30, edgecolor = 'black')

#df_csv['bairro'].value_counts().plot.bar()

#df_csv['bairro'].value_counts().plot.barh() 

#df_csv.plot.scatter(x='preco', y = 'area')

#df_csv['bairro'].value_counts().plot.barh(title= "oalos") 

#df_csv['quartos'].value_counts().plot.pie()

#plt.show()