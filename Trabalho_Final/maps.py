from pymongo import collection
from pymongo.results import InsertManyResult

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://admin:d7BCRVM11Exx99TF@cluster0.krmag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['projeto-final']#Base de dados

if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["top_30_cwur_heloise"]

    item_0 = {
    'name' : 'Harvard University',
    'location': { 'type': 'Point', 'coordinates': [-71.116832866, 42.371331848]}}

    item_1 = {
    'name' : 'Stanford University',
    'location': { 'type': 'Point', 'coordinates': [ -122.16925228590436, 37.42777269746988]}}

    item_2 = {
    'name' : 'Massachusetts Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-71.09304810305743 , 42.360356445250865]}}

    item_3 = {
    'name' : 'University of Cambridge',
    'location': { 'type': 'Point', 'coordinates': [ 0.11971794830629269,52.20326209483308]}}

    item_4 = {
    'name' : 'University of Oxford',
    'location': { 'type': 'Point', 'coordinates': [ -1.2529533890490945,51.75520408982706 ]}}

    item_5 = {
    'name' : 'Columbia University',
    'location': { 'type': 'Point', 'coordinates': [ -73.96216202802943,40.807636611813834 ]}}

    item_6 = {
    'name' : 'University of California, Berkeley',
    'location': { 'type': 'Point', 'coordinates': [-122.25881761213634 , 37.87238676213995]}}

    item_7 = {
    'name' : 'University of Chicago',
    'location': { 'type': 'Point', 'coordinates': [-87.59829272648254 , 41.7887409039786]}}

    item_8 = {
    'name' : 'Princeton University',
    'location': { 'type': 'Point', 'coordinates': [ -74.61453479986885,40.344431225888925 ]}}

    item_9 = {
    'name' : 'Cornell University',
    'location': { 'type': 'Point', 'coordinates': [-76.47507074895404 ,42.452771761299765]}}

    item_10 = {
    'name' : 'Yale University',
    'location': { 'type': 'Point', 'coordinates': [ -72.92274269375169,41.31691765905514 ]}}

    item_11 = {
    'name' : 'California Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-118.12356347888598 , 34.137896992681604]}}

    item_12 = {
    'name' : 'University of Tokyo',
    'location': { 'type': 'Point', 'coordinates': [139.76266447457286 ,35.713008121889445 ]}}
   
    item_13 = {
    'name' : 'University of Pennsylvania',
    'location': { 'type': 'Point', 'coordinates': [ -75.19055893543786, 39.950752143479555]}}

    item_14 = {
    'name' : 'University of California, Los Angeles',
    'location': { 'type': 'Point', 'coordinates': [-118.44437403213342 ,34.06907783566165 ]}}

    item_15 = {
    'name' : 'Johns Hopkins University',
    'location': { 'type': 'Point', 'coordinates': [ -76.61799105476166,39.33044437630392 ]}}

    item_16 = {
    'name' : 'Kyoto University',
    'location': { 'type': 'Point', 'coordinates': [135.78181423309914 ,35.02656506505538 ]}}

    item_17 = {
    'name' : 'New York University',
    'location': { 'type': 'Point', 'coordinates': [-73.98354970268933 ,40.6939191263751 ]}}
    
    item_18 = {
    'name' : 'University of Michigan, Ann Arbor',
    'location': { 'type': 'Point', 'coordinates': [-83.7381704529702 , 42.278130877058935, ]}}

    item_19 = {
    'name' : 'Swiss Federal Institute of Technology in Zurich',
    'location': { 'type': 'Point', 'coordinates': [8.548248678977483 ,47.37664771855825 ]}}

    item_20 = {
    'name' : 'University of California, San Diego',
    'location': { 'type': 'Point', 'coordinates': [ -118.44401530140208,34.06935645352186 ]}}

    item_21 = {
    'name' : 'Northwestern University',
    'location': { 'type': 'Point', 'coordinates': [ -87.67712038874329, 42.05341462305202 ]}}

    item_22 = {
    'name' : 'Hebrew University of Jerusalem',
    'location': { 'type': 'Point', 'coordinates': [35.24110123733539 ,31.79488198081194 ]}}

    item_23 = {
    'name' : 'Seoul National University',
    'location': { 'type': 'Point', 'coordinates': [126.95067039939248 ,37.45685536925558 ]}}

    item_24 = {
    'name' : 'University of Wisconsin-Madison',
    'location': { 'type': 'Point', 'coordinates': [-89.41159946612801 ,43.07677186118037 ]}}
  
    item_25 = {
    'name' : 'University of California, San Francisco',
    'location': { 'type': 'Point', 'coordinates': [ -117.23972162469579, 32.7161813947009]}}

    item_26= {
    'name' : 'University College London',
    'location': { 'type': 'Point', 'coordinates': [ -0.1341573342153393, 51.524901174217064]}}

    item_27 = {
    'name' : 'Duke University',
    'location': { 'type': 'Point', 'coordinates': [-78.93743088921221 ,36.00160864647893]}}

    item_28 = {
    'name' : 'Rockefeller University',
    'location': { 'type': 'Point', 'coordinates': [ -73.95576468166372,40.76285259943344 ]}}

    item_29 = {
    'name' : 'University of Texas at Austin',
    'location': { 'type': 'Point', 'coordinates': [ -96.80893753506004,32.81123275745848 ]}}


    collection_name.insert_many([item_0,  item_1,  item_2,  item_3,  item_4,  item_5,  item_6,  item_7,  item_8,  item_9,  item_10,  item_11,  item_12,  item_13,  item_14,  item_15,  item_16,  item_17,  item_18,  item_19,  item_20,  item_21,  item_22,  item_23,  item_24,  item_25,  item_26,  item_27,  item_28,  item_29])
    

if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["top_10_cwur_heloise"]

    item_0 = {
    'name' : 'Harvard University',
    'location': { 'type': 'Point', 'coordinates': [-71.116832866, 42.371331848]}}

    item_1 = {
    'name' : 'Massachusetts Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-71.09304810305743 , 42.360356445250865]}}

    item_2 = {
    'name' : 'Stanford University',
    'location': { 'type': 'Point', 'coordinates': [ -122.16925228590436, 37.42777269746988]}}

    item_3 = {
    'name' : 'University of Cambridge',
    'location': { 'type': 'Point', 'coordinates': [ 0.11971794830629269,52.20326209483308]}}

    item_4 = {
    'name' : 'California Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-118.12356347888598 , 34.137896992681604]}}

    item_5 = {
    'name' : 'Princeton University',
    'location': { 'type': 'Point', 'coordinates': [ -74.61453479986885,40.344431225888925 ]}}

    item_6 = {
    'name' : 'University of Oxford',
    'location': { 'type': 'Point', 'coordinates': [ -1.2529533890490945,51.75520408982706 ]}}

    item_7 = {
    'name' : 'Yale University',
    'location': { 'type': 'Point', 'coordinates': [ -72.92274269375169,41.31691765905514 ]}}

    item_8 = {
    'name' : 'Columbia University',
    'location': { 'type': 'Point', 'coordinates': [ -73.96216202802943,40.807636611813834 ]}}

    item_9 = {
    'name' : 'University of California, Berkeley',
    'location': { 'type': 'Point', 'coordinates': [-122.25881761213634 , 37.87238676213995]}}

    item_10 = {
    'name' : 'University of Chicago',
    'location': { 'type': 'Point', 'coordinates': [-87.59829272648254 , 41.7887409039786]}}

    item_11 = {
    'name' : 'Cornell University',
    'location': { 'type': 'Point', 'coordinates': [-76.47507074895404 ,42.452771761299765]}}

    collection_name.insert_many([item_0,  item_1,  item_2,  item_3,  item_4,  item_5,  item_6,  item_7,  item_8,  item_9,  item_10,  item_11])

        ####################################################################33333

if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["top_10_shanghai_heloise"]

    item_1 = {
    'name' : 'University of California, Berkeley',
    'location': { 'type': 'Point', 'coordinates': [-122.25881761213634 , 37.87238676213995]}}

    item_2 = {
    'name' : 'California Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-118.12356347888598 , 34.137896992681604]}}

    item_3 = {
    'name' : 'Columbia University',
    'location': { 'type': 'Point', 'coordinates': [ -73.96216202802943,40.807636611813834 ]}}

    item_4 = {
    'name' : 'Harvard University',
    'location': { 'type': 'Point', 'coordinates': [-71.116832866, 42.371331848]}}

    item_5 = {
    'name' : 'Massachusetts Institute of Technology',
    'location': { 'type': 'Point', 'coordinates': [-71.09304810305743 , 42.360356445250865]}}

    item_6 = {
    'name' : 'Princeton University',
    'location': { 'type': 'Point', 'coordinates': [ -74.61453479986885,40.344431225888925 ]}}       

    item_7 = {
    'name' : 'Stanford University',
    'location': { 'type': 'Point', 'coordinates': [ -122.16925228590436, 37.42777269746988]}}

    item_8 = {
    'name' : 'University of Cambridge',
    'location': { 'type': 'Point', 'coordinates': [ 0.11971794830629269,52.20326209483308]}}

    item_9 = {
    'name' : 'University of Chicago',
    'location': { 'type': 'Point', 'coordinates': [-87.59829272648254 , 41.7887409039786]}}

    item_10 = {
    'name' : 'University of Oxford',
    'location': { 'type': 'Point', 'coordinates': [ -1.2529533890490945,51.75520408982706 ]}}

    collection_name.insert_many([item_1,  item_2,  item_3,  item_4,  item_5,  item_6,  item_7,  item_8,  item_9,  item_10])

