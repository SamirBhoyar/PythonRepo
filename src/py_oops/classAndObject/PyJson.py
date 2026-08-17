
import json
from pprint import pprint

#Note: If you have a JSON string, you can parse it by using the "json.loads()" method.
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print('-----------------')


x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(x)
print('-----------------')
pprint(x) # it will just let you print the way 'x' is(in Python format),
          # but you can't write this format in file like json.dump(Strict JSON format)
print('-----------------')
# sort the result alphabetically by keys:
# Use the indent parameter to define the numbers of indents:
# (Indentation in Python refers to the whitespace (spaces or tabs) at the beginning of a line of code)
print(json.dumps(x, indent=4, sort_keys=True))
#Note: If you have a Python object,you can convert it into a JSON string by using json.dumps() method.