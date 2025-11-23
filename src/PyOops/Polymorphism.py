# Method overloading:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.speak() # Output: Woof!
cat.speak() # Output: Meow!
print("=============================")

# Duck Typing:
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

def transport(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
plane = Plane()

transport(car)   # Output: Drive!
transport(boat)  # Output: Sail!
transport(plane) # Output: Fly!