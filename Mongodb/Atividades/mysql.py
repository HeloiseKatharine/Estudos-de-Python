import MySQLdb

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
    CONNECTION_STRING = "#"

    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cria o banco de dados.
    
    return client['soulcodeTeste2']
  

def mostrarDocumentos():
    dbname = get_database()
    collection_name = dbname["itens_mysql_export2"]
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)

db = MySQLdb.connect(host="185.201.11.44", user="u781216269_rootx", passwd="h5S3J#oP1@", db = "u781216269_library")

cursor = db.cursor()
cursor.execute("SELECT * FROM `tblbooks`")
numrows = int(cursor.rowcount)
linhas = cursor.fetchall()

print("Número total de registros encontrados: ", cursor.rowcount)
print("\nMostrando resultados...")

i=0

for linha in linhas:
    print("ID: ", linha[0])
    print("Nome: ", linha[1])
    print("ISBN: ", linha[4])
    print("Preço R$0: ", linha[5])

dbname = get_database()
for linha in linhas:
   collection_name = dbname["itens_mysql_export2"]  
   item = {
      "_id": linha[0], 
      "dado_1": linha[1],
      "ISBN": linha[4],
      "Preço": linha[5]
   }
   collection_name.insert_one(item)
print("Documento vindo do MySQL inserido em Mongo!")   

mostrarDocumentos()


# admin 6
# tblauthors 4
# tblcategory 5
# tblissuedbookdetails 7
# tblstudents 9

