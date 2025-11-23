#Genrator function:
#  allow you to declare a function that behaves like an iterator,providing a faster and easier way to create iterators

#-> It basically remember last value and logi to generate number. so it will not hold a lot of memory while generating values.

import Main   #'as it is in same package no need to import'
def gencube(n):
    for i in range(n):
        yield i **3

for i in gencube(5):
    print(i)

print('-------_Generator function-----')
