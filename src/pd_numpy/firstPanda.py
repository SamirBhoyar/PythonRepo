import pandas as pd

df=pd.read_csv("/Users/samirb/Documents/GitHub/PythonRepo/src/resource/sink/student_exam_scores.csv")
print(df.to_string()) #without truncate  #print(df) #->with truncate
print(df.head(10))

# Note: Pandas object type in dataframe is equivalent to string in core python
'----------------split() function-------------'
df = pd.DataFrame({
    'col1': [1,2,3,4,5],
    'col2': [33,42,81,92,45],
    # 'col3': 'samir bhoyar data engineer'
    'col3': 'samir bhoyar is data engineer'.split()
})
print(df)
print('----------------------')
def cond(words):
    list=[]
    for word in words:
        if word[0]=='s':
            list.append('s')
        else:
            list.append('z')
    return list
df['col5'] = cond(df['col3'])
print(df)
print('----------------------')
df['col5_a'] = df['col3'].str[0]
def test(a):
    if a=='s':
        return 's'
    else:
        return 'z'
df['col5_b'] =df['col3'].apply(test)
print(df)
print('----------------------')
df['col6']= df['col1'].apply(lambda x: 'even' if  x%2==0 else 'odd' )
print(df)
print('----------------------')
df['col7'] =df['col3'].apply(len)
print(df)
print('----------------------')