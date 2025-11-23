# Data Structures are a way of storing and organizing data in a computer.
#
# Python has built-in support for several data structures, such as lists, dictionaries, and sets.
#
# Other data structures can be implemented using Python classes and objects, such as linked lists, stacks, queues, trees, and graphs.

import numpy as np
arr = np.array([1, 2, 3])
print(arr)

print("========Remove duplicate from sorted array==========")

def removeDuplicates(array):
    size = len(array)
    if size == 0:
        return 0
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            array[insertIndex] = array[i]
            insertIndex += 1
    return insertIndex

array_1 = [1, 2, 2, 3, 3, 4]
k1 = removeDuplicates(array_1)
# 4; array_1[:k1] -> [1, 2, 3, 4]
print(f"removed :{k1}, old array: {array_1}, and new array :{array_1[:k1]}")

array_2 = [1, 1, 3, 4, 5, 6, 6]
k2 = removeDuplicates(array_2)
# 5; array_2[:k2] -> [1, 3, 4, 5, 6]
print(f"removed :{k2}, old array: {array_2}, and new array : {array_2[:k2]}")

print("======Find missing Number in array=====")

def find_missing_numbers(input_list):
    n = max(input_list)
    print(n)# expected range is 1 to max value
    full_set = set(range(1, n + 1))
    print(full_set)
    input_set = set(input_list)

    return sorted(full_set - input_set)

list_1 = [1,5,6,3,4,8]
print("Missing number from List : ",find_missing_numbers(list_1))
# 2,7