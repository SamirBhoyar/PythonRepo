#Genrator function:
#  allow you to declare a function that behaves like an iterator,providing a faster and easier way to create iterators
'''
A generator function is a function that:

returns values one at a time
instead of returning everything at once

=>It uses yield instead of return
'''
#-> It basically remember last value and logic to generate number. so it will not hold a lot of memory while generating values.


# yield: pauses the function ->returns a value ->remembers state ->resumes from same place next time

def gencube(n):                # -- calling from Main file and class
    for i in range(n):
        yield i **3

# print("RUNNING Generator function")
# for i in gencube(5):
#     print(i)


def read_file(path):
     with open(path) as f:
         for line in f:
            yield line

path="/Users/samirb/Documents/GitHub/PythonRepo/src/pythonCore/file.log"
print("RUNNING Read file===Generator function:")
# for i in read_file(path):
#     print(i)

'''Generator vs List
Use case: Memory optimization in pipelines
=>'''
gen = (x*x for x in range(10))  # lazy
lst = [x*x for x in range(10)]  # eager
print(gen)
for i in gen:
    print(i)
print( lst)
for i in lst:
    print(i)