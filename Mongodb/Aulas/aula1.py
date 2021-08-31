from pymongo import collection
from pymongo.results import InsertManyResult

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "#"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['Banco_teste2']#Base de dados


if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["Atividades"]
    print('Base de dados criada!!!!')

    item_1 = {
        "_id" : "0001",
        "nome_item" : "Livro",
        "desconto_max" : "10%",
        'REF' : 340,
        "preco" : 25.30,
        'categoria':'fisico'
    }
    item_2 = {
        "_id" : "0002",
        "nome_item" : "Camera",
        "desconto_max" : "10%",
        'REF' : 500,
        "preco" : 1000.30,
        'categoria':'fisico'
    }
    item_3 = {
        "_id" : "0003",
        "nome_item" : "Telefone",
        "desconto_max" : "10%",
        'REF' : 340,
        #"preco" : 100,
        'categoria':'fisico'
    }

    item_4 = {
        "nome_item" : "Aula remota",
        "desconto_max" : "10%",
        'REF' : 545,
        #"preco" : 100,
        'categoria':'online'
    }
    
    #collection_name.insert_one(item_1)
    #collection_name.insert_many([item_2, item_3])
    #collection_name.insert_one(item_4)

    '''
    #Exibição simples de dados
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        #print(item)#todos os itens
        print(item['nome_item'], item['desconto_max'])

    #Atualização simples de dados (somente o primeiro item)
    collection_name.update_one({"desconto_max": "11%"}, {"$set":{"desconto_max":"10%"}})
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)

    #Atualização simples de dados (todos os itens)
    collection_name.update_many({"desconto_max": "11%"}, {"$set":{"desconto_max":"10%"}})
    for item in detalhes_itens:
        print(item)
    '''

    '''
    #Eclusão simples de dados

    #Excluir tudo
    #collection_name.drop()

    #Exclusão por Id
    collection_name.delete_one({"_id":"0001"})

    
    #Exclusão de muitos registros que tem o mesmo dados em comum
    collection_name.delete_many({"desconto_max":"11%"})    

    chave = "desconto_maximo"
    valor = "11%"
    collection_name.delete_many({chave:valor})
    
    '''


    #Novas Queries
    
    #Exibir ordenado
    #detalhes_itens = collection_name.find().sort("nome_item", -1)#sort("nome_item", 1)
   
    #Exibir com parâmetros
    #detalhes_itens = collection_name.find({"categoria" : "Online"})

    #Exibir por valores lógicos
    #detalhes_itens = collection_name.find({"$or" : [{"categoria":"online"}, {"categoria" : "Fisico"}]})

    #detalhes_itens = collection_name.find({"$and" : [{"categoria" : "Fisico"}, {"nome_item" : "camera"}]})

    #Exibir por partes de string
    #detalhes_itens = collection_name.find({"nome_item":{"$regex":"^mera"}})

    #Mostrar por valores distintos
    #detalhes_itens = collection_name.distinct("nome_item")

    #Exibir por limite
    #detalhes_itens = collection_name.find({"categoria" : "fisico"}).limit(2)

    # Saltar registros
    #detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)

    #for item in detalhes_itens:
    #    print(item)
