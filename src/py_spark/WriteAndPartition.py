

# readDf.write.mode("overwrite").partitionBy("DEPARTMENT_NAME").option("header",True).format("csv").save("/output/result")
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Accounting
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Administration
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Executive
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Finance
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Human Resources
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=IT
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Marketing
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Public Relations
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Purchasing
# drwxr-xr-x   - abc supergroup          0 2023-01-14 11:33 /output/result/DEPARTMENT_NAME=Shipping
# -rw-r--r--   1 abc supergroup          0 2023-01-14 11:33 /output/result/_SUCCESS

# >>> resultDf.rdd.getNumPartitions()
# 1
# >>> resultDf.repartition(10)
# DataFrame[EMPLOYEE_ID: int, DEPARTMENT_ID: int, DEPARTMENT_NAME: string]
# >>> resultDf.rdd.getNumPartitions()
# 1
# >>> newDf = resultDf.repartition(10)
# >>> newDf.rdd.getNumPartitions()
# 10
# >>> df1 = newDf.repartition(2)
# >>> df1.rdd.getNumPartitions()
# 2
# >>> newDf.rdd.getNumPartitions()
# 10
# >>> df2 = newDf.coalesce(20)
# >>> df2.rdd.getNumPartitions()
# 10
# >>> df3 = newDf.coalesce(5)
# >>> df3.rdd.getNumPartitions()
# 5
