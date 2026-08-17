class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v4 = Vector("samir", "bhoyar")
v3 = v1 + v2
print(v3) # Output: (4, 6)
v4 = Vector("samir", "bhoyar")
print(v4)

# ======================
'''Code Breakdown
1️⃣ Define a Class
class Vector:


You are defining a custom data type called Vector — think of it as a 2D point (x, y).

2️⃣ The Constructor (__init__)
def __init__(self, x, y):
    self.x = x
    self.y = y


When you create a new Vector object (e.g. v1 = Vector(1, 2)),
this method initializes its attributes:

v1.x = 1

v1.y = 2

3️⃣ Operator Overloading with __add__
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)


Normally, Python doesn’t know how to add two user-defined objects.
But if you define the special method __add__, Python will call it whenever you use the + operator on your class.

So when you write:

v3 = v1 + v2


Python internally does:

v3 = v1.__add__(v2)


This returns a new Vector whose:

x = v1.x + v2.x = 1 + 3 = 4

y = v1.y + v2.y = 2 + 4 = 6

Hence v3 becomes (4, 6).

4️⃣ String Representation with __str__
def __str__(self):
    return f"({self.x}, {self.y})"


When you call print(v3), Python calls v3.__str__() to get a readable string version of the object.

So instead of printing something like:

<__main__.Vector object at 0x00000123>


It prints:

(4, 6)

✅ Final Output
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)


Output:

(4, 6)
'''