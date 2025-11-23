# Write a program to generate list of 10 numbers
from pydoc import text

result = []
for i in range(1,11):
    result.append(i)

print(result)

# How to do it with the help of list comprehension?
result = [ x for x in range(1,11) ]
print(result)

# Get a list of all even numbers between 1 to 50
result = [  x for x in range(1,51) if x % 2 == 0  ]
print(result)

print("------------------")
# Get a list of all even numbers from given list
list_a = [1,2,4,3,6,7,9]

[print(x) for x in list_a]
print("------------------")

# convert all string into upper case in given list
list_a = ['hi', 'hello' , 'bye' , 'nice']

result = [ x.upper() for x in list_a  ]
print(result)
print("------------------")
# Put all negative numbers after positive numbers from given list
list_a = [9,-1,2,-5,1,10,-6]

# result = [9,2,1,10,-1,-5,-6]
# result1= [x for x in list_a if x>0 ]
# result2= [x for x in list_a if x<0 ]
# print (result1 + result2)

result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)

print("------------------")
#question convert string  input = "HeLLo saMIr"   out = "hellO samiR" with python

text= "HeLLo saMIr"
def tranform(w):
    return w[:-1].lower() + w[-1].upper()

result = " ".join(tranform(x) for x in text.split())
print(result)