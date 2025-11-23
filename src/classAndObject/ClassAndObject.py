
print('==========Class and Object==========')
class FirstClass:
    x=5
#Create an object named p1, and print the value of x:
obj= FirstClass
print(obj.x)

print('-==========__init__()==========')
#Note: classes and objects in their simplest form, and are not really useful in real life applications.
#Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
    # Note: The self parameter is a reference to the current instance of the class,
    # and is used to access variables that belong to the class.(self is like java "this")
    def __init__(self, name, age):      #like java "class constructor"
        self.name = name
        self.age = age

    # It does not have to be named self, you can call it whatever you like,
    # but it has to be the first parameter of any function in the class:
    def myfunc(abc):     #self is abc here
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1.myfunc())

print('==========__str__()==========')
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):                  # like java "toString()"
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

print('==========Delect object and object properties==========')
# class Person:
#     age = 35
#
# p1 = Person
# del p1.age
# print(p1.age)     #AttributeError: 'Person' object has no attribute 'age'
#
# del p1
# print(p1)   #NameError: name 'p1' is not defined

print('==========Pass Statement==========')
# class definitions cannot be empty, but if you for some reason have a class definition
# with no content,put in the pass statement to avoid getting an error.
class Person:
    pass