from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, StructType, TimestampType, StructField, ArrayType,FloatType, DoubleType)

import pyspark.sql.functions as F

#local[4] portas

spark = SparkSession.builder.appName('main2') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '2gb') \
    .getOrCreate()

# .config('spark.shuffle.sql.partitons', 1) \

#abrindo arquivo .json
df = spark.read.json("D:/scripts/tokyo_olympics_2021/tokyo-olympics-all-by-type-2021-08-11.json")
df.printSchema()
df.show(5)