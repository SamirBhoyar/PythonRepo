import pandas as pd

df=pd.read_csv("/Users/samirb/Documents/GitHub/PythonRepo/src/resource/sink/student_exam_scores.csv")
# print(df.to_string()) #without truncate  #print(df) #->with truncate
# print(df.head(10))

df = pd.DataFrame({
    'col1': [1,2,3,4,5],
    'col2': [3,4,8,9,5],
    'col3': 'samir bhoyar data engineer'
})
print(df)
'----------------------'
