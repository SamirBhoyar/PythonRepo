from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display(self):
        return f"This shap is :"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# shape = Shape()  # This would raise a TypeError as Shape is an abstract class
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print(circle.display(),"circle")