import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType
from pyspark.sql.window import Window

spark= SparkSession.builder.appName("demo").getOrCreate()
file_path= "/Users/samirb/Documents/GitHub/PythonRepo/src/resource/sink/emp.csv"
readDf= spark.read.csv(file_path,header=True,inferSchema=True)

nullCount=readDf.select([count(when(col(c).isNull(),'c')).alias(c) for c in readDf.columns])
nullCount.show()



#note:"I iterate over columns, convert null checks to 1/0, and aggregate to get null counts per column."
'''
Loop through each column
col(c).isNull() → checks NULL
when(..., 1) → mark NULL as 1
count() → counts those 1s
alias(c) → keeps column name
'''