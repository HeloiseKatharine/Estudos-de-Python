from pymongo import collection
from pymongo.results import InsertManyResult

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/myFirstDatabase"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['Banco_teste2']#Base de dados

#CRUD
if __name__ == "__main__":
    dbname = get_database()
    collection_name = dbname["Atividades"]

    #Crie uma função cadastrar documento, onde seja possível inserir quantos campos forem necessários. Todos os campos devem ser do tipo string. Informe mensagem ao usuário que o documento foi cadastrado.
    def cadastrar():
        while True: 
            op = int(input('\n1 - Cadastrar um documento\n2 - Sair\n'))
            if op == 1:
                dbname = get_database()
                collection_name = dbname["Atividades"]
                dic={}
                while True:
                    print('\n**Para sair insira 0 em campo**')
                    campo = input('Digite o nome do campo: ')
                    if campo == '0':
                        break
                    else:
                        valor = input('Digite o valor do campo: ')
                        dic[campo] = valor
                collection_name.insert_one(dic)
            elif op == 2:
                break
            else:
                print('\nOpção inválida!!\nTente novamente.')


    #Crie uma função que exiba todos os documentos da coleção.
    def exibir():
        dbname = get_database()
        collection_name = dbname["Atividades"]
        detalhes_itens = collection_name.find()
        print('\n')
        for item in detalhes_itens:
            print(item)#todos os itens


    #Crie uma função que atualialize apenas um item por id e que atualize todos os campos sendo esse campo dado pelo usuário.

    #fazer a segunda parte

    def update():
        id = input('Digite o id do item que deseja atualizar: ')
        dbname = get_database()
        collection_name = dbname["Atividades"]
        detalhes_itens = collection_name.find()
        aux = 0
        for item in detalhes_itens:
            if(item['_id'] == id):
                aux = 1
                lista = list(item.keys())
                campo = input(f'\n{lista}\nDigite o nome do campo que deseja atualizar: ')
                valor = input('Digite o valor atualizado: ')
                if (campo in lista) == True:
                    collection_name.update_one({campo:item[campo]}, {"$set":{campo:valor}})
                    print('O campo foi atualizado com sucesso.')
                else: 
                    print('O campo não foi encontrado.')
        if(aux == 0):
            print('O ID não foi localizado. ')
    

    #Crie uma função que delete o documento por ID.
    def delete():
        id = input('Digite o id do item que deseja excluir: ')
        dbname = get_database()
        collection_name = dbname["Atividades"]
        detalhes_itens = collection_name.find()
        aux = 0
        for item in detalhes_itens:
            if(item['_id'] == id):
                aux = 1
                collection_name.delete_one({"_id":id})
                print('O campo foi excluído com sucesso.')
        if(aux == 0):
            print('O ID não foi localizado. ')


    #Crie uma função que delete todos os documento
    def delete_tudo():
        resp = input('Deseja EXCLUIR TODOS os itens do seu banco de dados? y/n')

        if(resp.lower() == 'y'):
            collection_name.drop()#deleta a coleção 
            print('Todos os itens foram excluídos.')

        elif(resp.lower == 'n'):
            print('Os itens não foram excluídos.')

        else:
            print('Erro!')
        

    #cadastrar()
    #exibir()
    #update() #fazer a segunda parte
    #delete() #revisar
    #delete_tudo()