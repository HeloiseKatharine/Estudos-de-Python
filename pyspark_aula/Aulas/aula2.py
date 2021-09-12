from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType)

import pyspark.sql.functions as F

#local[4] portas
spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()


#df = spark.read.load('D:\scripts\covid_cases.csv', format='csv', sep=',', inferSchema='true', header='true')

#print('printSchema')
#df.printSchema()


shema = StructType([StructField("case_id", IntegerType()),
                    StructField("province", StringType()),
                    StructField("city", StringType()),
                    StructField("group", BooleanType()),
                    StructField("infection_case", StringType()),
                    StructField("confirmed", IntegerType()),
                    StructField("latitude", StringType()),
                    StructField("longitude", StringType())
])

path = "D:\scripts\covid_cases_no_header.csv"

print('testeeeeee')

df = spark.read.format("csv") \
    .schema(shema) \
    .load(path) 
#df.printSchema()

#########extract#########

df.show(5)

#alterar nome de coluna
cases = df.withColumnRenamed("infection_case", "casos de infeção")
cases.show(5)


#comentar todas

cases2 = df.toDF(*['ID', 'Província', 'Cidade', 'Grupo', 'Casos de infecção', 'confirmados','Latitude', 'logitude'])


#retorna apenas alguns dados
cases2.select('ID', 'Cidade','Grupo').show(5)

cases2.filter((cases2.confirmados > 10) & (cases2.Província =='Daegu')).show()
#cases2.show(5)

#Iniciar outro DF

regions = spark.read.load('D:\scripts\Region.csv', format='csv', sep=',', inferSchema='true', header='true')

print('regions')
regions.limit(10).show()


cases = cases.join(regions, ['province', 'city'], how ='left')

cases.limit(10).show()

