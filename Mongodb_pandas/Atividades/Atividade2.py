#collection.count_documents({}) #para contar todos ({específico})
def get_database():
    from pymongo import MongoClient
    import pymongo

    #URL de conexao
    CONNECTION_STRING = "mongodb+srv://user:jkgugA78@cluster1.bgw0k.mongodb.net/myFirstDatabase"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#Conexão com o cliente

    return client['Banco_teste2']#Base de dados

def mostrarDocumentos():
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)

#mostrarDocumentos()  

#a) Quantos livros possuem número de páginas 0
def imprime_livros_pag(pag):
    dbname = get_database()
    collection_name = dbname["Atividades"]

    tam = collection_name.count_documents({"pageCount" : pag})
    print(f'\nQuantidade de livros que possuem número de páginas 0 = {tam} \n')

    '''
    tam1 = 0
    detalhes_itens = collection_name.find({"pageCount" : pag})
    for item in detalhes_itens:
        tam1 +=1
        print('\n')
        print(item)
    print(f'\n {tam1} \n')
    '''
#b) Quantos livros foram publicados?
def publicados():
    dbname = get_database()
    collection_name = dbname["Atividades"]
    tam = collection_name.count_documents({"status" : "PUBLISH"})
    #tam = collection_name.count_documents({"pageCount" : pag})
    print(f'\nQuantos livros foram publicados? {tam} \n')

#c) Qual o título do livro, cujo ISBN é 1933988924
def titulo_ISBN(isbn):
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find({"isbn" : isbn})
    #doc = collection_name.find_one({'isbn': '1933988924'})
    for item in detalhes_itens:
        print(f"\n{item['title']}\n")

#d) Qual a descrição do livro Machine Learning in Action
#f) Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade?

def descricao(title):
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find({"title" : title})
    for item in detalhes_itens:
        print(f"\n{item['longDescription']}\n")

#e) O Livro ArcGIS Web Development foi publicado?
def publicado(title):
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find({"title" : title})

    for item in detalhes_itens:
        if item['status'] == "PUBLISH":
            print('\nfoi publicado')
        else:
            print('\nNão foi publicado')
        print(f"{item['status']}\n")

#g) Quantas páginas possui o livro Jess in Action?
def quant_pag(title):
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find({"title" : title})
    for item in detalhes_itens:
        print(f"\n{item['pageCount']}\n")

#h) Quais são os primeiros três livros da coleção?
def imprime_tres():
    dbname = get_database()
    collection_name = dbname["Atividades"]

    detalhes_itens = collection_name.find({}).limit(3)
    for item in detalhes_itens:
        print(f"\n{item['title']}\n")


#a) Quantos livros possuem número de páginas 0? 
#imprime_livros_pag(0)

#b) Quantos livros foram publicados?
#publicados()

#c) Qual o título do livro, cujo ISBN é 1933988924? 
#titulo_ISBN("1933988924")

#d) Qual a descrição do livro Machine Learning in Action?
#descricao("Machine Learning in Action")

#e) O Livro ArcGIS Web Development foi publicado?
#publicado("ArcGIS Web Development")

#f) Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade? 
#descricao("Secrets of the JavaScript Ninja pBook upgrade") #longDescription
'''
dbname = get_database()
collection_name = dbname["Atividades"]

detalhes_itens = collection_name.find({"title" : "Secrets of the JavaScript Ninja pBook upgrade"})
for item in detalhes_itens:
    print(f"\n{item['shortDescription']}\n")
'''

#g) Quantas páginas possui o livro Jess in Action?
#quant_pag("Jess in Action")

#h) Quais são os primeiros três livros da coleção?
#imprime_tres()

#i) Qual o ID do livro, cujo ISBN é 1930110987? Ele é declarado ou setado pelo MongoDB?

'''
dbname = get_database()
collection_name = dbname["Atividades"]
detalhes_itens = collection_name.find({"isbn" : "1930110987"})
for item in detalhes_itens:
    print(f"\n{item['_id']}")
    if type(item['_id']) is int:
        print('É declarado')
    else:
        print('É setado pelo MongoDB\n')
'''