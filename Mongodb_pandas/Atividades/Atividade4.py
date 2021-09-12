from numpy.lib.shape_base import tile
import pandas as pd
import matplotlib.pyplot as plt 

#Crie uma série com dados meteorológicos de cinco cidades como índices.
#plt.style.use('ggplot')
serie = pd.Series([30, 25, 26, 28, 31], index=['Brasília','Planaltina-GO', 'Planaltina-DF', 'Sobradinho', 'Águas Claras'])

#print(serie)



#----------------------------------------------------------------------------------------------

#Crie um Data Frame contendo os dados abaixo:

df = pd.DataFrame({
    'Nome':['João', 'Pedro', 'Carla', 'Suzane'], 
    'Depósitos':[100, 500, 300, 250],
    'Saques':[10, 11.50, 35.30, 200],
    'Estornos':[0, 0, 250, 300]
})

#Os tipos de itens
#print(df.dtypes)

#A média dos itens
#print(df.mean(numeric_only=True))

#Imprima o último item.
#print(df.tail(1))

#Exiba os estornos maiores que 0
est = df[(df['Estornos'] > 0)] 
#print(est)

#Exiba os saques menores que 15
saques = df[(df['Saques'] > 15 )]
#print(saques)

#print(df)

#----------------------------------------------------------------------------------------------

# Gráficos

#serie.plot.bar(title = 'ssf')

df.plot.bar(x="Nome")
plt.show()
#plt.plot(serie.values, serie.index)
#df['Saques'].plot.hist()


