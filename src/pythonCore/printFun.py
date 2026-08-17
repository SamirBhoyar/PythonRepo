# 1. Basic print() (most common)
print("Hello World")
print('--------------------')

# 2. Printing multiple values
name = "Samir"
age = 25
print("Name:", name, "Age:", age)
print('--------------------')

# 3. Using sep and end
print("A", "B", "C", sep="-")  #A-B-C
print('----------and ----------')
print("Hello", end=" ")
print("World")  #Hello World
print('--------------------')

#4. f-strings ( most important / modern way)
name = "Samir"
age = 25
#print(f"My name is {name} and I am {age} years old") #leading 'f' can be removed
print("My name is {name} and I am {age} years old")
print('--------------------')

#5. .format() method
print("My name is {} and I am {}".format(name, age))
print('--------------------')

#6. % formatting (very old style)
print("My name is %s and I am %d" % (name, age))
print('--------------------')

#7. Printing to file
with open("output.txt", "w") as f:
    print("Hello File", file=f)  #print in file

with open("output.txt", "r") as f:
    print(f.read())
    print('--------------------')

#8. Pretty printing (for complex data)
from pprint import pprint

data = {"name": "Samir", "skills": ["Python", "SQL"]}
pprint(data)