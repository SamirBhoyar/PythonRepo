#Problem: create a class for Dictionary parsing
# 1.write a function to get all the key
# 2.write a function to get all the value
# 3.write a function to through a exception in case input is not a dictionary
# 4.write a function to take a input and parse key and value for that input out of dictionary
# 5.write a function to insert a key and value pair in dictionary

import ClassAndModule as cm
import json
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
        # key = input(f"Enter key for entry {i+1} key: ")  # class
        # value = input(f"Enter value for key '{key}': ")  # A
        # my_dict[key] = value

# print("Input key-value: ", my_dict)

        #with json
        user_input = input("Enter the dictionary as a JSON string (or type 'exit' to quit): ")  # {"class":"A"} or exit
        if user_input.lower() == "exit":
            print("You exit dictionary add option")
            break
        else:
            json_dict = json.loads(user_input)
            print("Your dictionary:", json_dict)



dict2.set_input(my_dict,dict1.get_dict())
print(dict1)

# # with Json: Ask user until valid input
#
#
#
# while True:
#     user_input = input("Enter the dictionary as a JSON string (or type 'exit' to quit): ")  #{"class":"A"} or exit
# #
#
#     if user_input.lower() == "exit":
#         print("Exiting program.")
#         break
#
#     try:
#         my_dict = json.loads(user_input)
#         print("Your dictionary:", my_dict)
#         break   # exit loop once valid JSON is entered
#     except json.JSONDecodeError as e:
#         print("Invalid JSON. Please try again.")
#         print("Error:", e)
#
# dict2.set_input(my_dict,dict1.get_dict())
# print(dict1)