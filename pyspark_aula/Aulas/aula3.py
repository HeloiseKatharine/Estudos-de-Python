from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType)

import pyspark.sql.functions as F

#local[4] portas
spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

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


df = spark.read.format("csv") \
    .schema(shema) \
    .load(path) 

df.show(5)

#criando uma tabela com o resultado de outra + 100
novoDF1 = df.withColumn("NewCofirmed",100+F.col("confirmed"))
novoDF1.show(5)


#criando uma tabela com o EXPONECIOADO resultado de outra
novoDF2 = df.withColumn("ExpConfirmed", F.exp("confirmed"))
novoDF2.show(5)


