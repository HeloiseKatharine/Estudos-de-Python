#Atividade para a criação de 4 consultas
#4 consultas sem atualizar da simples a mais complexa (nivel de dificuldade)
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

#dbname = get_database()
#collection_name = dbname["Atividades"]

#1 - Crie uma consulta que retorne 2 autores do livro "SNA and TCP/IP Enterprise Networking"
#R: "Daniel C. Lynch" "James P. Gray" "and Edward Rabinovitch" "editors"

'''
detalhes_itens = collection_name.find({"title" : "SNA and TCP/IP Enterprise Networking"})
for item in detalhes_itens:
    print(f"\n{item['authors'][0]}\n")
    print(f"\n{item['authors'][1]}\n")
'''

#2 - Crie uma consulta que retorne todos os livros da categoria "Java"

'''
detalhes_itens = collection_name.find({"categories" : "Java"})
for item in detalhes_itens:
    print(item['title'])
'''

'''
Resposta = 

Android in Action, Second Edition
Griffon in Action
OSGi in Depth
3D User Interfaces with Java 3D      
Hibernate in Action
Hibernate in Action (Chinese Edition)
Java Persistence with Hibernate      
Hibernate Search in Action
jQuery in Action, Second Edition
Spring Dynamic Modules in Action
POJOs in Action
Seam in Action
Open Source SOA
Struts 2 in Action
Spring Roo in Action
Mule in Action
Java Foundation Classes
Managing Components with Modeler
Command-line Processing with CLI
Understanding and Using Chain
Working with the Logging and Discovery Components
Uploading files with FileUpload
Handling Protocols with the Net Component
XML Parsing with Digester
JXPath and Betwixt: Working with XML
Validating Data with Validator
Enhancing Java Core Libraries with Collections
Enhancing Java Core Libraries with BeanUtils and Lang
Pool and DBCP: Creating and Using Object Pools
Grails in Action
Up to Speed with Swing, Second Edition
GWT in Action
Java Development with Ant
Lucene in Action
Lucene in Action, Second Edition
The Awesome Power of PowerJ
Portlets and Apache Portals
Java Network Programming, Second Edition
Struts in Action
Camel in Action
JBoss in Action
Groovy in Action
Groovy in Action, Second Edition
Effective Unit Testing
Making Java Groovy
AspectJ in Action
AspectJ in Action, Second Edition
Hadoop in Action
Tuscany SCA in Action
Tapestry in Action
Ant in Action
iText in Action, Second Edition
Subversion in Action
Distributed Programming with Java
JavaServer Faces in Action
JUnit in Action
Tika in Action
JavaFX in Action
Server-Based Java Programming
Mahout in Action
EJB 3 in Action
EJB 3 in Action, Second Edition
Domino Development with Java
Hibernate Quickly
Lift in Action
JUnit Recipes
Clojure in Action
Scala in Action
Secrets of the JavaScript Ninja
Swing
Swing Second Edition
The Awesome Power of Java Beans
SCBCD Exam Study Kit
Portlets in Action
SWT/JFace in Action
Java 3D Programming
JSP Tag Libraries
Instant Messaging in Java
Java Applets and Channels Without Programming
Making Sense of Java
ActiveMQ in Action
Scala in Depth
JMX in Action
EJB Cookbook
GWT in Action, Second Edition
JUnit in Action, Second Edition
Bitter Java
Bitter EJB
JDK 1.4 Tutorial
XDoclet in Action
Spring in Action
Spring in Action, Second Edition
Spring in Action, Third Edition
Spring in Practice
Java 2 Micro Edition
Java Servlets by Example
'''

#3 - Crie uma consulta que retorne a data de publicação do livro que possui o id = 214
'''
dbname = get_database()
collection_name = dbname["Atividades"]
detalhes_item = collection_name.find({})
detalhes_itens = collection_name.find({"_id" : 214 })
for item in detalhes_itens:
    print(item['publishedDate'])
'''

#4 - Crie uma consulta que retorne todos os livros do autor "Bruno Lowagie"
#R= "iText in Action" e "iText in Action, Second Edition"
'''
detalhes_itens = collection_name.find({"authors" : "Bruno Lowagie"})
for item in detalhes_itens:
    print(item['title'])
'''

# 2) Qual é o número de paginas de cada livro cujo titulo começa com a letra U ?
#detalhes_itens = collection_name.find({"nome_item":{"$regex":"^mera"}})
'''
dbname = get_database()
collection_name = dbname["Atividades"]

detalhes_itens = collection_name.find({'title':{"$regex":"^U"}})
for item in detalhes_itens:
    print(item['pageCount'])
'''





'''
#Quantos livros tem menos de 300 páginas?
dbname = get_database()
collection_name = dbname["Atividades"]
detalhes_item = collection_name.find({})
cont = 0
for item in detalhes_item:
    if(item['pageCount'] < 300):
        cont +=1
print(cont)'''























