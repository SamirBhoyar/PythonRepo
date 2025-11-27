# Write a program to generate list of 10 numbers
from pydoc import text

result = []
for i in range(1,11):
    result.append(i)

print(result)

# How to do it with the help of list comprehension?
# result = [ x for x in range(1,11) ]
result = list(range(1,11))
print(result)

# Get a list of all even numbers between 1 to 50
result = [  x for x in range(1,51) if x % 2 == 0  ]
print(result)


def even_no(n):
    r=[]
    for x in range(1,n):
        if x%2==0:
            r.append(x)
    return r

result=even_no(52)
print(result)

print("------------------")
# Get a list of all odd numbers from given list
list_a = [1,2,4,3,6,7,9]

[print(x) for x in list_a if x %2!=0]
print("------------------")

# convert all string into upper case in given list
list_a = ['hi', 'hello' , 'bye' , 'nice']
result = [ x.upper() for x in list_a  ]
print(result)

def upper_case(str_list):
    r=[]
    for x in str_list :
       xup= x.upper()
       r.append(xup)
    return r

list_a = ['hi', 'hello' , 'bye' , 'nice']
print(upper_case(list_a))

def lower_case(str_list):
   return list(map(str.lower,str_list))

list_a = ['HI', 'HELLO', 'BYE', 'NICE']
print(lower_case(list_a))
print("------------------")
# Put all negative numbers after positive numbers from given list
list_a = [9,-1,2,-5,1,10,-6]

# result = [9,2,1,10,-1,-5,-6]
# result1= [x for x in list_a if x>0 ]
# result2= [x for x in list_a if x<0 ]
# print (result1 + result2)

result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)

def reshape(list_a):
    r=[]
    s=[]
    for x in list_a:
        if x>=0:
            r.append(x)
        else:
            s.append(x)

    r.extend(s)
    return r

list_a = [9,-1,2,-5,1,10,-6]
print(reshape(list_a))

print("------------------")
#question convert string  input = "HeLLo saMIr"   out = "hellO samiR" with python

text= "HeLLo saMIr"
def tranform(w):
    return w[:-1].lower() + w[-1].upper()

result = " ".join(tranform(x) for x in text.split())
print(result)
print("------------------")

#conver string to list and vice versa

strg="I|am|good"

tmp= strg.split('|')
print(tmp)
st=' '.join(tmp)
print(st)

rt=' '.join(map(str,tmp))
print(rt)

rt=' '.join(str(s) for s in tmp)
print(rt)