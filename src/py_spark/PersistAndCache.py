from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark= SparkSession.builder.appName("demo").getOrCreate()

from pyspark import StorageLevel
df = spark.range(1000)
df.persist(StorageLevel.MEMORY_AND_DISK)
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
print(df_sum)
# Unpersist the DataFrame when done
df.unpersist()

print('=====================Cache==================')
df = spark.range(1000)
df.cache()
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
print(df_sum)

# unpersist() removes the cached or persisted data from memory and disk.
df.unpersist()