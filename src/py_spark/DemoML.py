import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType
from pyspark.sql.window import Window

spark= SparkSession.builder.appName("demo").getOrCreate()
file_path= "/Users/samirb/Documents/GitHub/PythonRepo/src/resource/sink/emp.csv"
#readDf= spark.read.option('header','True').csv(file_path)
readDf= spark.read.csv(file_path,header=True,inferSchema=True)
print("------------------------------")
# finalDf= readDf.limit(10)
# finalDf.printSchema()
print("------------------------------")
# readDf.show()
# readDf.select('First Name', 'salary'+1000 ).show()   # with out col function
#with col function
# readDf.select(col('First Name'), col('Salary')).withColumn('New sal',col('salary')+1000).show()
# readDf.select(max('Salary')).show()
# readDf.filter('Salary==139852').select('First Name','Salary').show()
# readDf.select('First Name', 'Salary').orderBy(col('Salary').desc()).show()
# readDf.groupby('Salary').agg(sum('Salary').alise('sal'), max('salary')).show()
print("------------------------------")
# newDf= readDf.withColumn('empSalary',when(col('Salary')>100000,"A").when((col('Salary')<100000) & (col('Salary')>70000),"B").otherwise('c'))
# newDf.select('First Name','Salary','empSalary').show()
print("------------------------------")
# empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show()
# readDf.alias('t1').join(readDf.alias('t2'), col('t1.Team')==col('t2.Team')).select('t1.First Name','t2.Salary','t1.Team').show()
print("------------------------------")
# @udf(returnType=StringType())
# def upperCase(in_str):
#     out_str= in_str.upper()
#     return out_str
#
# readDf.select(upperCase(col('First Name'))).show()
print("------------------------------")

# windowSpec = Window.orderBy(col('Salary').desc())
# df=readDf.withColumn("empSal", rank().over(windowSpec))
# df.filter(col('empSal')==2).select('First Name', 'Salary').show()
# Or
df=readDf.withColumn("empSal", rank().over(Window.orderBy(col('Salary').desc())))
df.filter(col('empSal')==2).select('First Name', 'Salary').show()
output='/Users/samirb/Documents/WorkSpace/PySpark/resource'
df.repartition(1).write.parquet('output')
df.rdd.getNumPartitions()

print("------------------------------")
# readDf.write.mode("overwrite").option("header",True).save("/output/result")

# readDf.write.mode("overwrite").option("header",True).format("csv").save("/output/result")
# readDf.write.mode("append").option("header",True).format("csv").save("/output/result")
