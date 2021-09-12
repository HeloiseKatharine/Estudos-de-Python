#sql
from pyspark.sql.session import SparkSession
import pyspark.sql.functions as F

spark = SparkSession \
    .builder \
    .appName('Aula5') \
    .getOrCreate()

data_file = 'D:\scripts\data.csv'

#cache para dataset pequeno(setando para dataset)
df = spark.read.csv(data_file, header=True, sep=",").cache()

#------------------------------------------

data_file2 = "D:\scripts\supermarket_sales.csv"
df = spark.read.csv(data_file2, header= True, sep=",").cache()
#print(df.columns)

gender = df.groupBy('Gender').count()
#gender.show()

#------------------------------------------

df.registerTempTable("sales")
output = spark.sql('SELECT * FROM sales')

output = spark.sql("SELECT * FROM sales WHERE `Unit Price` < 15 AND Quantity < 10")
#output.show()

#------------------------------------------
#UPDATE

output = output.withColumn("Customer type", F.when(F.col("Customer type") == "Member", "Membro").otherwise(F.col("Customer type")))
output.show()

#DELETE
output = output.filter(output['Gender'] != 'Male')
output.show()