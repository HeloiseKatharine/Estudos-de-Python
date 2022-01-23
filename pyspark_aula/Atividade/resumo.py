#gráficos
#função 
#manipulação de string

#https://covid.saude.gov.br/

import pandas as pd
import matplotlib.pyplot as plt  

plt.style.use("ggplot")

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/myFirstDatabase"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['Covid']#Base de dados

dbname = get_database()

collection_name = dbname["2020_parte1"]

detalhes_itens = collection_name.find()

#criando um dataframe 714.482 linhas
df_covid = pd.DataFrame(list(detalhes_itens))
#criando um dataframe menor
micro_df = df_covid[0:10000]

#criando um novo dataframe
def criando_df(df):
    #_id
    #Brasil;;;76;;;;2020-02-25;9;210147125;0;0;0;0;;;

    lista = []
    df_obitosAcumulado = []
    semanaEpi = []
    regiao = []
    estado = []

    for i in df['regiao;estado;municipio;coduf;codmun;codRegiaoSaude;nomeRegiaoSaude;data;semanaEpi;populacaoTCU2019;casosAcumulado;casosNovos;obitosAcumulado;obitosNovos;Recuperadosnovos;emAcompanhamentoNovos;interior/metropolitana']:
        lista.append(i.split(';'))#quebra onde tem ; e gera uma lista 
    
    #Brasil;;;76;;;;2020-02-25;9;210147125;0;0;0;0;;;
    #[região, estado,...]
    for i in lista:
        #add os dados nas listas
        df_obitosAcumulado.append(i[12])
        semanaEpi.append(i[8])
        regiao.append(i[0])
        estado.append(i[1])

    #novo dataframe
    df_new = pd.DataFrame(list(zip(df_obitosAcumulado, semanaEpi, regiao, estado)), columns = ['df_obitosAcumulado','semanaEpi', 'regiao', 'estado'])

    return df_new

#função que retorna um gráfico pizza com os óbitos acumulados por região
def obitosAcumulado_regiao(df_new):

    graf = (df_new.filter(items=['df_obitosAcumulado', 'regiao']).groupby('regiao').count())

    #Brasil = Indefinido
    labels = ['Indefinido', 'Centro-Oeste', 'Nordeste', 'Norte', 'Sudeste', 'Sul']

    #gráfico de pizza
    graf.plot.pie(autopct='%1.1f%%', shadow=True, subplots=True, ylabel='', startangle = 90, labels = labels)

    plt.title("óbitos acumulados por região\n")
    plt.legend(title="Regiões",bbox_to_anchor=(1.9, 1.9))
    plt.show()

resp = criando_df(micro_df)
obitosAcumulado_regiao(resp)
