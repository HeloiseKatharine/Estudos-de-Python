from pymongo import collection
from pymongo.results import InsertManyResult

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "#"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#conexão com o cliente

    return client['Paises']#Base de dados

############################ AMÉRICA 10 ############################

if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["America"]

    print('Base de dados criada!!!!')

    item_1 = {
        '_id' :  1,
        'nome' : 'Brasil',
        'capital' : 'Brasilia',
        'moeda' : 'real', 
        'idioma' : 'Português brasileiro', 
        'PIB':  1.84,
        'populacao': 44.94
    }

    item_2 = {
        '_id' :  2,
        'nome' : 'Argentina',
        'capital' : 'Buenos Aires', 
        'moeda' :'Peso argentino', 
        'idioma' : 'Língua castelhana', 
        'populacao': 211.0
    }

    item_3 = {
        '_id' :  3,
        'nome' : 'paraguai',
        'capital' : 'Assunção',
        'moeda' : 'Guarani',
        'idioma' :  ' Língua guarani, Língua castelhana',
        'populacao' : 7.045
    }

    item_4 = {
        '_id' :  4, 
        'nome' : 'Uruguai', 
        'capital' : 'Montevidéu', 
        'moeda' : 'Peso uruguaio', 
        'idioma' : 'Língua castelhana', 
        'populacao': 3.462
    }

    item_5 = {
        '_id' :  5, 
        'nome' : 'México', 
        'capital' : 'Cidade do México', 
        'moeda' : 'Peso mexicano', 
        'populacao': 127.6
    }

    item_6 = {
        '_id' :  6,
        'nome' : 'Colômbia', 
        'capital' : 'Bogotá', 
        'moeda' : 'Peso colombiano', 
        'idioma' : 'Língua castelhana', 
        'populacao': 50.34
    }

    item_7 = {
        '_id' :  7, 
        'nome' : 'Nicarágua', 
        'capital' : 'Manágua', 
        'moeda' : 'Córdoba', 
        'idioma' : 'Língua castelhana', 
        'populacao': 6.546
    }

    item_8 = {
        '_id' :  8, 
        'nome' : 'Honduras', 
        'capital' : 'Tegucigalpa', 
        'moeda' : 'Lempira', 
        'idioma' : 'Língua castelhana',
        'populacao': 9.746
    }

    item_9 = {
        '_id' :  9, 
        'nome' : 'Guatemala', 
        'capital' : 'Cidade da Guatemala', 
        'moeda' : 'Quetzal', 
        'idioma' : 'Língua castelhana',
        'populacao': 16.6
    }

    item_10 = {
        '_id' :  10, 
        'nome' : 'Panamá', 
        'capital' : 'Cidade do Panamá', 
        'moeda' : 'Dólar dos Estados Unidos e Balboa', 
        'idioma' : 'Língua castelhana' , 
    }
    '''
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9,item_10])'''

############################ Ásia 15 ############################

    dbname = get_database()

    collection_name = dbname["Ásia"]

    print('Base de dados criada!!!!')

    item_1 = {
        'nome' : 'Japão',
        'capital' : 'Tóquio',
        'moeda' : 'Iene', 
        'idioma' : 'Japonês', 
        'populacao': 126.3
    }

    item_2 = {
        'nome' : 'Filipinas',
        'capital' : 'Manila', 
        'moeda' :'Peso filipino | Philippine peso sign', 
        'idioma' : 'Filipino e Inglês', 
        'populacao': 108.1
    }

    item_3 = {
        'nome' : 'Vietnã',
        'capital' : 'Hanói',
        'moeda' : 'Dong',
        'idioma' :  'Vietnamita',
        'populacao' : 96.46
    }

    item_4 = {
        'nome' : 'Myanmar', 
        'capital' : 'Naipidau', 
        'moeda' : 'Quiate', 
        'idioma' : 'Língua birmanesa', 
        'populacao': 54.05
    }

    item_5 = {
        'nome' : 'Coreia do Sul', 
        'capital' : 'Seul', 
        'moeda' : 'Won sul-coreano', 
        'populacao': 51.71
    }

    item_6 = {
        '_id' :  11,
        'nome' : 'Tailândia', 
        'capital' : 'Bangkok', 
        'moeda' : 'Baht', 
        'idioma' : 'Tailandês', 
        'populacao': 69.63
    }

    item_7 = {
        '_id' :  12, 
        'nome' : 'Taiwan', 
        'capital' : 'Taipé', 
        'moeda' : 'Novo dólar taiwanês', 
        'idioma' : 'Língua mandarim', 
        'populacao': 23.57
    }

    item_8 = {
        '_id' :  13, 
        'nome' : 'Singapura', 
        'capital' : 'Cidade de Cingapura', 
        'moeda' : 'Dólar de Singapura', 
        'idioma' : 'inglês | malaio | mandarim | tâmil.',
        'populacao': 5.704
    }

    item_9 = {
        '_id' :  14, 
        'nome' : 'Laos', 
        'capital' : 'Vienciana', 
        'moeda' : 'Kip', 
        'idioma' : 'Língua laociana',
        'populacao': 7.169
    }

    item_10 = {
        '_id' :  15, 
        'nome' : 'Cambodja', 
        'capital' : 'Phnom Penh', 
        'moeda' : 'Riel', 
        'idioma' : 'Khmer',
        'populacao': 7.169
    }
    item_11 = {
        '_id' :  16, 
        'nome' : 'China', 
        'capital' : 'Pequim', 
        'moeda' : ' Renminbi', 
        'idioma' : 'Mandarim'
    }

    item_12 = {
        '_id' :  17, 
        'nome' : 'Indonésia', 
        'capital' : 'Jacarta', 
        'moeda' : 'Rupia indonésia', 
        'idioma' : 'Indonésio',
        'populacao': 270.6
    }

    item_13 = {
        '_id' :  18, 
        'nome' : 'Malásia ', 
        'capital' : 'Kuala Lumpur', 
        'moeda' : 'Ringgit malaio', 
        'idioma' : ' Malaio',
        'populacao': 31.95
    }

    item_14 = {
        '_id' :  19, 
        'nome' : 'Timor-Leste', 
        'capital' : 'Díli', 
        'moeda' : 'Dólar dos Estados Unidos', 
        'idioma' : ' Português |Língua tétum',
        'populacao': 1.293
    }

    item_15 = {
        '_id' :  20, 
        'nome' : 'Brunei', 
        'capital' : 'Bandar Seri Begawan', 
        'moeda' : 'Dólar de Brunei', 
        'idioma' : 'Malaio',
        'populacao': 433.285
    }
    '''
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9,item_10, item_11, item_12, item_13, item_14, item_15])
    '''

############################ África 20  ############################
    dbname = get_database()

    collection_name = dbname["Africa"]

    print('Base de dados criada!!!!')

    item_1 = {
            'nome' : 'Angola', 
            'capital' : 'Luanda', 
            'moeda' : 'Kwanza', 
            'idioma' : 'Português',
            'populacao': 31.83
    }

    item_2 = {
            'nome' : 'Zâmbia', 
            'capital' : 'Lusaka', 
            'moeda' : 'Kwacha zambiano', 
            'idioma' : 'Inglês',
            'populacao': 17.86
    }

    item_3 = {
            'nome' : 'África do Sul', 
            'capital' : 'Cidade do Cabo | Pretória | Bloemfontein', 
            'moeda' : 'Rand', 
            'idioma' : ' Africâner | Inglês, Língua zulu | Língua xossa | Sesoto | Língua venda | Língua tswana | Sepedi | Língua Tsonga | Língua suázi | Língua ndebele do sul',
            'populacao': 58.56
    }

    item_4 = {
            'nome' : 'Namíbia', 
            'capital' : ' Windhoek', 
            'idioma' : 'Inglês',
            'populacao': 2.495
    }

    item_5 = {
            'nome' : 'Botsuana', 
            'capital' : 'Lusaka', 
            'moeda' : 'Pula', 
            'idioma' : 'Inglês',
            'populacao': 2.304
    }

    item_6 = {
            'nome' : 'Madagascar', 
            'capital' : 'Antananarivo', 
            'idioma' : 'Língua malgaxe  | Francês',
            'populacao': 26.97
    }

    item_7 = {
            'nome' : 'Nigéria', 
            'capital' : 'Abuja',
            'moeda' : 'Naira',
            'idioma' : 'Inglês',
            'populacao': 488.1
    }

    item_8 = {
            'nome' : 'Chade', 
            'capital' : 'Djamena',
            'moeda' : 'Franco CFA Central',
            'idioma' : ' Francês | Árabe',
            'populacao': 15.95
    }

    item_9 = {
            'nome' : 'Sudão', 
            'capital' : 'Cartum',
            'moeda' : 'Libra Sudanesa',
            'idioma' : ' Francês | Árabe',
            'populacao': 42.81
    }

    item_10 = {
            'nome' : 'Líbia', 
            'capital' : 'Trípoli',
            'moeda' : 'Dinar líbio',
            'idioma' : 'Árabe',
            'populacao': 6.777
    }

    item_11 = {
            '_id' :  21, 
            'nome' : 'Níger', 
            'capital' : 'Niamei',
            'idioma' : 'Francês',
            'populacao': 23.31
    }

    item_12 = {
            '_id' :  22, 
            'nome' : 'Mali', 
            'capital' : 'Bamako',
            'moeda' : 'Franco CFA ocidental',
            'idioma' : 'Francês',
            'populacao': 19.66
    }

    item_13 = {
            '_id' :  23, 
            'nome' : 'Saara Ocidental', 
            'capital' : 'El Aiune',
            'moeda' : 'Dirrã marroquino |Uguia | Peseta saaraui',
            'idioma' : 'Árabe',
    }

    item_14 = {
            '_id' :  24, 
            'nome' : 'Mauritânia', 
            'capital' : 'Nouakchott',
            'moeda' : 'Uguia',
            'idioma' : 'Árabe',
            'populacao': 4.526
    }

    item_15 = {
            '_id' :  25, 
            'nome' : 'Camarões', 
            'capital' : 'Yaoundé',
            'moeda' : 'Franco CFA Central',
            'idioma' : 'Francês | Inglês',
            'populacao': 25.88
    }

    item_16 = {
            '_id' :  26, 
            'nome' : 'Benin', 
            'capital' : 'Porto Novo',
            'moeda' : 'Franco CFA Central',
            'idioma' : 'Francês',
            'populacao': 11.8
    }

    item_17 = {
            '_id' :  27, 
            'nome' : 'Togo', 
            'capital' : 'Lomé',
            'moeda' : 'Franco CFA ocidental',
            'idioma' : 'Francês',
            'populacao': 8.082
    }

    item_18 = {
            '_id' :  28, 
            'nome' : 'Senegal', 
            'capital' : 'Dacar',
            'moeda' : 'Franco CFA ocidental',
            'idioma' : 'Francês',
            'populacao': 16.3
    }

    item_19 = {
            '_id' :  29, 
            'nome' : 'Serra Leoa', 
            'capital' : 'Freetown',
            'moeda' : 'Leone',
            'idioma' : 'Inglês'
    }

    item_20 = {
            '_id' :  30, 
            'nome' : 'Congo', 
            'capital' : 'Brazzaville',
            'moeda' : 'Franco CFA Central',
            'idioma' : 'Francês',
            'populacao': 5.381
    }
    '''
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19, item_20])'''

############################ Europa 15  ############################
#if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["Europa"]

    print('Base de dados criada!!!!')

    item_1 = {
        '_id' :  1,
        'nome' : 'Alemanha',
        'capital' : 'Berlim', 
        'moeda' :'Euro', 
        'idioma' : 'Alemão', 
        'populacao': 83.02
    }

    item_2 = {
        '_id' :  2,
        'nome' : 'Espanha',
        'capital' : 'Madrid', 
        'moeda' :'Euro', 
        'idioma' : 'Língua castelhana', 
        'populacao': 46.94
    }

    item_3 = {
        '_id' :  3,
        'nome' : 'Portugal',
        'capital' : 'Lisboa', 
        'moeda' :'Euro', 
        'idioma' : 'Português de Portugal', 
        'populacao': 10.28
    }

    item_4 = {
        '_id' :  4,
        'nome' : 'França',
        'capital' : 'Paris', 
        'moeda' :'Euro | Franco CFP', 
        'idioma' : 'Francês', 
        'populacao': 67.06
    }

    item_5 = {
        '_id' :  5,
        'nome' : 'Itália',
        'capital' : 'Roma', 
        'moeda' :'Euro', 
        'idioma' : 'Italiano', 
        'populacao': 60.36
    }

    item_6 = {
        '_id' :  6,
        'nome' : 'Bélgica',
        'capital' : 'Bruxelas', 
        'moeda' :'Euro', 
        'idioma' : ': Neerlandês | Francês | Alemão', 
        'populacao': 11.46
    }

    item_7 = {
        '_id' :  7,
        'nome' : 'Suíça',
        'capital' : 'Berna', 
        'moeda' :'Franco suíço', 
        'idioma' : ' Alemão |Italiano, Língua romanche | Francês', 
        'populacao': 8.545
    }

    item_8 = {
        '_id' :  8,
        'nome' : 'Luxemburgo',
        'capital' : 'Luxemburgo', 
        'moeda' :'Euro', 
        'idioma' : 'Língua luxemburguesa | Francês | Alemão', 
        'populacao': 613.894
    }

    item_9 = {
        '_id' :  9,
        'nome' : 'Irlanda',
        'capital' : 'Dublin', 
        'moeda' :'Euro', 
        'idioma' : 'Língua irlandesa, Inglês', 
        'populacao': 4.904
    }

    item_10 = {
        '_id' :  10,
        'nome' : 'Reino Unido',
        'capital' : 'Londres', 
        'moeda' :'Libra esterlina', 
        'idioma' : 'Inglês', 
        'populacao': 66.65
    }

    item_11 = {
        'nome' : 'Dinamarca',
        'capital' : 'Copenhage', 
        'moeda' :'Coroa dinamarquesa', 
        'idioma' : 'Dinamarquês', 
        'populacao': 5.806
    }

    item_12 = {
        'nome' : 'Noruega',
        'capital' : 'Oslo', 
        'moeda' :'Coroa norueguesa', 
        'idioma' : 'Norueguês', 
        'populacao': 5.328
    }

    item_13 = {
        'nome' : 'Suécia',
        'capital' : 'Estocolmo', 
        'moeda' :'Coroa sueca', 
        'idioma' : 'Sueco', 
        'populacao': 10.23
    }

    item_14 = {
        'nome' : 'República Tcheca',
        'capital' : 'Praga', 
        'moeda' :'Coroa checa', 
        'idioma' : 'Tcheco', 
        'populacao': 10.65
    }

    item_15 = {
        'nome' : 'Hungria',
        'capital' : 'Budapeste', 
        'moeda' :'Florim húngaro', 
        'idioma' : 'Húngaro', 
        'populacao': 9.773
    }
    '''
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15])
    '''