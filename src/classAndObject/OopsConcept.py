class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Good Morning ",self.firstname, self.lastname)

class Student(Person):
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname,year=2020):
        super().__init__(fname, lname)
        self.graduationyear = year
#super() function that will make the child class inherit all the methods and properties from its
#parent class:you do not have to use the name of the parent element, it will automatically inherit

    def welcome(self):
        print("Hello", self.firstname, self.lastname, "you passed in year: ", self.graduationyear)

x = Student("Samir", "Bhoyar",2019)
x.welcome()
y= Student("Chiku","Bhoyar")
y.printname()

print('==========Iterator==========')
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which
# you can get an iterator from.All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# The __iter__() method acts similar to __init__(), you can do operations (initializing etc.),
# but must always return the iterator object itself.
#
#The __next__() method also allows you to do operations,and must return the next item in the sequence.

print('------------------------')
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
# To prevent the iteration from going on forever, we can use the StopIteration statement.

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print('==========Polymorphism==========')

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
    print("----------------")


