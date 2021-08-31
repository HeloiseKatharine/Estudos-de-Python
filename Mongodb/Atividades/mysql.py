import MySQLdb

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

'''
dbname = get_database()
for linha in linhas:
    Collection_name = dbname["itens_mysql_export2"]
    item = {
        "_id":linha[0],
        "nome":linha[1],
        "ISBN":linha[4],
        "PREÇO":linha[5]
    }
    Collection_name.insert_one(item)
print("Documento vindo do MySQL inserido em Mongo!")

'''
