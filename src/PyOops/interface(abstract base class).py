from abc import ABC, abstractmethod

# Define an interface (abstract base class)
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Class implementing the interface
class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


# Trying to instantiate Vehicle will raise error
# v = Vehicle()  # ❌ TypeError: Can't instantiate abstract class

c = Car()
c.start()
c.stop()

print('==========Multiple “interface-like” inheritance in Python===============')

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck flying")
    def swim(self):
        print("Duck swimming")

d = Duck()
d.fly()
d.swim()

print('============duck typed 🦆==============')

#Question: Why Python doesn’t need interfaces explicitly
#Ans:
#Because Python is duck typed 🦆 — meaning, if an object behaves like an interface (has required methods), it’s accepted.

class File:
    def read(self):
        return "Reading from a file"

class NetworkStream:
    def read(self):
        return "Reading from a network stream"

def read_data(source):
    print(source.read())  # ✅ only requires the .read() method

read_data(File())
read_data(NetworkStream())

print('==============Error example: AttributeError===================')
#Behind the Scenes:

# Python doesn’t check the type of source — It only checks at runtime whether source has a .read() method.

#In Java, you’d need both Dog and Cat to implement an interface like Soundable, otherwise the compiler would reject it.

#Instead, it checks at runtime:

# “Does this object have a .read() method?”
# “If yes, call it. If not, raise AttributeError.”

#Question : What Happens If It Doesn’t Match
class Car:
    def drive(self):
        print("Vroom!")

def make_sound(animal):
    print(animal.sound())

make_sound(Car())