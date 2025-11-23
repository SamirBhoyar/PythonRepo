import pandas as pd

df=pd.read_csv("/Users/samirb/Documents/WorkSpace/PythonWS/PythonWorkspace/src/resource/sink/student_exam_scores.csv")
# print(df.to_string()) #without truncate  #print(df) #->with truncate
print(df.head(10))
