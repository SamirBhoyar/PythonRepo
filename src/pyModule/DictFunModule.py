#Problem: create a class for Dictionary parsing
# 1.write a function to get all the key
# 2.write a function to get all the value
# 3.write a function to through a exception in case input is not a dictionary
# 4.write a function to take a input and parse key and value for that input out of dictionary
# 5.write a function to insert a key and value pair in dictionary

import ClassAndModule as cm
from src.pyModule.ClassAndModule import DictionarySet

dict1 = cm.DictionaryGet({"name":"samir","age":29})
print(dict1)        #use __Str__(self) -> output: string

print(dict1.get_keys())
print(dict1.get_values())

dict2 =cm.DictionarySet()
my_dict = {}
num_entries = int(input("Enter the number of key-value pairs you want to add: "))

if num_entries < 3:
    for i in range(num_entries):
        key = input(f"Enter key for entry {i+1} key: ")
        value = input(f"Enter value for key '{key}': ")
        my_dict[key] = value

print("Input key-value: ", my_dict)

dict2.set_input(my_dict,dict1.get_dict())
print(dict1)