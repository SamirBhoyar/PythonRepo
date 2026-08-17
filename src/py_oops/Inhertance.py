
class xyz:
    def __init__(self,a):
        self.a =a

    def test(self):
        print("This is xyz class:", self.a)

class abc(xyz):
    pass

x = abc(23)  # even if i pass but as child will call it parent we need to pass arg through child to parent.
x.test()
print('=====================')


#case of inheritance :

print('==========Example 1 — Constructor from the first parent is used==========')

class Xyz:
    def __init__(self,a,b):
        self.a= a
        self.b= b
        print("Xyz constructor called ",self.a," : ",self.b)

class Abc:
    def __init__(self,p,q):
        print("Abc constructor called ",p," : ",q)

class Child1(Xyz, Abc):   #Xyz constructor called
    pass

class Child2(Abc, Xyz):
    pass

obj = Child1(2,3)
obj2 = Child2(2,3)


print('==========#Example 2 — explicitly Calling both parent constructors==========')

class Xyz1:
    def __init__(self):
        print("Xyz constructor called")

class Abc1:
    def __init__(self):
        print("Abc constructor called")

class Ch(Xyz1, Abc1):
    def __init__(self):
        # call both parents
        Xyz1.__init__(self)
        Abc1.__init__(self)
        print("Child constructor called")

ob = Ch()

print('==========Ex 3- Using super() with multiple inheritance=====')

#Note: When you use super(), Python uses the MRO (Method Resolution Order) chain,
# to determine the order of constructor calls.


class xyz:
    def __init__(self):
        print("Xyz constructor called")
        super().__init__()

class abc:
    def __init__(self):
        print("Abc constructor called")

class child(xyz, abc):
    def __init__(self):
        print("Child constructor called")
        super().__init__()

Obj = child()

print('''Note: super() automatically handles the MRO(Method Resolution Order):
Child → Xyz → Abc, but if i remove super from xyz class. it will only give child->xyz as per 
first parent''' )