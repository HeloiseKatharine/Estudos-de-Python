import findspark
from pyspark import rdd

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType, DoubleType)

findspark.init() #D:\spark-3.1.2-bin-haddoop2.7

from pyspark.sql import SparkSession
import pandas as pd


spark = SparkSession.builder \
    .master("local") \
    .appName("main") \
    .config("spark.executor.memory", "2gb") \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

#criando seção

#abrindo arquivo .json
#df = spark.read.json("D:/scripts/tokyo_olympics_2021/tokyo-olympics-all-by-type-2021-08-11.json")

schema = StructType([
      StructField("Aggregate",IntegerType())])

path = "D:/scripts/tokyo_olympics_2021/tokyo-olympics-all-by-type-2021-08-11.json"

df = spark.read.format("json") \
    .schema(schema) \
    .load(path) 
   
teste = df.show(5)
print(teste)

# D:/scripts/tokyo_olympics_2021/tokyo-olympics-all-by-type-2021-08-11.json
# D:\scripts\zipcodes.json
