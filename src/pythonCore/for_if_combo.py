print('=====1.First understand normal for loop=====')
'''1. First understand normal for loop
Basic syntax:
for variable in collection:
    # code
Example:
'''
numbers = [1, 2, 3, 4]
for x in numbers:
    print(x)

# Here: for x in numbers means: Take each value from numbers, one by one, and put it into x.



print('=====2.for with if — (if AFTER for)=====')
'''
2. for with if — filtering
This is probably the most important combination.[x for x in numbers if x > 5]

Think:
       FOR ->take each x ->if (x>5 ?) ->  Yes(include)
                                      |-> No(skip) 

Equivalent normal code:
result = []
for x in numbers:
    if x > 5:
        result.append(x)
Example:
'''
numbers = [1, 2, 6, 8, 10]
result = [x for x in numbers if x > 5]
print(result)

print('=====3.for with if-else — (if BEFORE for)=====')
'''3. for with if-else — transformation
Now we have something different:[x if x > 5 else 0 for x in numbers]

Previously: Filter values. Meaning:Give me only values where condition is true.
[x for x in numbers if x > 5]

Now: Transform every value. Meaning:Give me something for EVERY value. If condition is true, give me x; otherwise give me 0.
[x if x > 5 else 0 for x in numbers]
The if-else comes BEFORE for. Because: x if x > 5 else 0, is the expression/result that we want to generate.

The structure is: [expression_if_true if condition else expression_if_false for x in collection]
Example:
'''
numbers10 = [1, 6, 3, 8]
result10 = [x if x > 5 else 0 for x in numbers]
print(result10)
'''Equivalent normal loop:
result = []
for x in numbers:
    if x > 5:
        result.append(x)
    else:
        result.append(0)
This distinction is VERY important.
'''
print('=====4.for + multiple if=====')
'''
4. for + multiple if

You can also have:[x for x in numbers if x > 5 if x % 2 == 0]

This means:For each x, it must satisfy both conditions.

Equivalent:
result = []
for x in numbers:
    if x > 5:
        if x % 2 == 0:
            result.append(x)

Or more commonly:
[x for x in numbers if x > 5 and x % 2 == 0]
Example:
'''
numbers = [2, 4, 6, 7, 8, 10]
result = [x for x in numbers if x > 5 if x % 2 == 0]
print(result)
print('=====5.for + if-else + for=====')
'''5. for + if-else + for

You can combine them.
Example:
result = [
    x if x > 5 else 0
    for x in numbers
]

But you can also have nested loops:
[x + y for x in list1 for y in list2]
Example:
'''
list1 = [1, 2]
list2 = [10, 20]
result11 = [x + y for x in list1 for y in list2]
print(result11)
'''
Equivalent:
result = []
for x in list1:
    for y in list2:
        result.append(x + y)
 '''
print('=====6.Nested for + if=====')
'''6. Nested for + if
Example:
result = [
    x + y
    for x in list1
    for y in list2
    if x + y > 20
]
Equivalent:
result = []
for x in list1:
    for y in list2:
        if x + y > 20:
            result.append(x + y)

'''
list11 = [1, 2]
list22 = [10, 20]
result22=[x + y for x in list11 for y in list22 if x + y > 20]
print(result22)

print('=====7.Why your PySpark code has for at the end(find this columnNull)=====')
'''
7. Why your PySpark code has for at the end
Your code:
[count(when(col(c).isNull(), 'c')).alias(c) for c in readDf.columns]

The general pattern is:
[expression for variable in collection]
Here: expression = count(when(col(c).isNull(), 'c')).alias(c)


variable = c
collection = readDf.columns

for c in readDf.columns:
    result.append(
        count(when(col(c).isNull(), 'c')).alias(c)
    )
'''