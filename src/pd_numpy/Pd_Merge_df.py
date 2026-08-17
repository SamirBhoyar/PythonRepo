import pandas as pd

def1 =pd.DataFrame({
    "emp_id":[1,2,3,4],
    "emp_name":["Samir","Ram","Sham","rohit"],
    "dept_id":[1,2,3,1]
})

def2 =pd.DataFrame({
    "dept_id":[1,2,3,4],
    "dept_name":["Dev","QE","DevOps","SME"]

})

# result = pd.merge(def1,def2,on="dept_id")
result = pd.merge(def1[["dept_id","emp_name"]],def2,on="dept_id",validate="m:1")
print(result)

'''
Prevents unexpected duplicates:
Value   | Meaning
"1:1"   | Both sides have unique values
"1:m"   | Left  key is unique 
"m:1"   | Right  key is unique 
"m:m"   | No uniqueness enforced
'''