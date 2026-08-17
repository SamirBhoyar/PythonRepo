#Find duplicate Elements in list

nums=[1,2,3,4,5,2,6,1]
unique=set()
duplicate=set()
for num in nums:
    if num in unique:
        duplicate.add(num)
    else:
        unique.add(num)

print(list(duplicate))
print("=========================")
# Q: Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []

    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# or
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print("=========================")
from collections import Counter
# 2. Find Top N Frequent Elements
# Use case: Most active users / top products
def top_n(nums, k):
    print(Counter(nums).most_common(k))
    return [x for x, _ in Counter(nums).most_common(k)]
    #  Returns k list of tuples with:(element, frequency) ->[(1, 2), (2, 2), (3, 1)]
print(top_n(nums, 3))

'''for x, _ in ...
 _ means:“I don’t care about this value”

Here:
x → element
_ → frequency (ignored)'''
print("=========================")