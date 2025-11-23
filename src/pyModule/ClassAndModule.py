from this import d


class DictionaryGet:

    def __init__(self,d):
        self.d =d

    def get_keys(self):
        return self.d.keys()

    def get_values(self):
        return self.d.values()
    def get_dict(self):
        return self.d

def __str__(self):
    return f"Dictionary : {self.d}"

class DictionarySet(DictionaryGet):
    def __init__(self):
        super().__init__(d)


    def set_input(self, input, d2):

          try:
              if isinstance(input,dict):
               d2.update(input)
               print(d2)

              else:
                raise TypeError(input)

          except TypeError as e:
                    print("Input is not a dictionary type: ",e ," ,Enter again !")



# d = Dictionary({"name":"samir"})
# print(d.get_keys())
# print(d.get_values())
# d.set_input({5})
