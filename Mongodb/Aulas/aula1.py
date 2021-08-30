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
    collection_name.insert_one(item_4)
    
