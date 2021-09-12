from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType, DoubleType)

import pyspark.sql.functions as F

#local[4] portas
spark = SparkSession.builder.appName('Aula2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitons', 1) \
    .getOrCreate()

#abrindo arquivo .json
df = spark.read.json("D:\scripts\zipcodes.json")
df.printSchema()
df.show(5)

#
# Define custom schema
schema = StructType([
      StructField("RecordNumber",IntegerType()),
      StructField("Zipcode",IntegerType()),
      StructField("ZipCodeType",StringType()),
      StructField("City",StringType()),
      StructField("State",StringType()),
      StructField("LocationType",StringType()),
      StructField("Lat",DoubleType()),
      StructField("Long",DoubleType()),
      StructField("Xaxis",IntegerType()),
      StructField("Yaxis",DoubleType()),
      StructField("Zaxis",DoubleType()),
      StructField("WorldRegion",StringType()),
      StructField("Country",StringType()),
      StructField("LocationText",StringType()),
      StructField("Location",StringType()),
      StructField("Decommisioned",BooleanType()),
      StructField("TaxReturnsFiled",StringType()),
      StructField("EstimatedPopulation",IntegerType()),
      StructField("TotalWages",IntegerType()),
      StructField("Notes",StringType())
])

#criando outro dataframe com shema
print('criando outro dataframe com shema')
df_with_shema = spark.read.schema(schema) \
    .json('D:\scripts\zipcodes.json')
df_with_shema.printSchema()
df_with_shema.show()

