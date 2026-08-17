
class ListMethod:

    def __init__(self,l):
        self.l= l


    def list_parsel(self):
        if isinstance(self.l,list):
            for i in range(len(self.l)):
                print(self.l[i])

    def list_reversal(self):
        if type(self.l)==list:
            return  self.l[::-1]


list1 = ListMethod([2,3,5,78,90,34,2])

print(list1.list_parsel())
print('-----------------')
print(list1.list_reversal())