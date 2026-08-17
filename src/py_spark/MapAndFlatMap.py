import pyspark
from pyspark.sql import SparkSession

spark= SparkSession.builder.appName("demo").getOrCreate()

data= ["hello world", "how are you", "pyspark is awesome"]
rdd= spark.sparkContext.parallelize(data)

print("-----------Map and FlatMap-------------------")

# map (One-to-one Transformation):
# map applies a function to each element in the RDD or DataFrame, returning a new RDD or
# DataFrame with the same number of elements. Each input element is transformed into exactly
# one output element.
mapRdd= rdd.map(lambda x: x.split(" ")).collect()
print(mapRdd)

# flatMap (One-to-many Transformation):
# flatMap also applies a function to each element but can return zero, one, or multiple elements
# for each input. The resulting output is flattened into a single RDD or DataFrame.
Flatrdd= rdd.flatMap(lambda x: x.split(" ")).collect()
print(Flatrdd)

