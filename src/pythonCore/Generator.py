#Genrator function:
#  allow you to declare a function that behaves like an iterator,providing a faster and easier way to create iterators

#-> It basically remember last value and logic to generate number. so it will not hold a lot of memory while generating values.

import Main   #'as it is in same package no need to import'
def gencube(n):
    for i in range(n):
        yield i **3

print("RUNNING Generator function")
for i in gencube(5):
    print(i)

print("RUNNING Read file Generator function")
def read_file(path):
     with open(path) as f:
         for line in f:
            yield line

path="/Users/samirb/Documents/GitHub/PythonRepo/src/pythonCore/file.log"
for i in read_file(path):
    print(i)
