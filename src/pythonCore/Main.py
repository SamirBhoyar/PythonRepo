from src.pythonCore.Generator import gencube

def fun(l):             #function calling form main class
    print("Main logic")
    print("RUNNING Generator function")
    for i in gencube(5): #function calling from other model in same package
     print(i)
     l.append(i)
#
# def fun2():
#     print("Main2 logic")
#     result = []
#     for i in gencube(5):
#         result.append(i)
#     return result

#here Python: Loads Generator.py->Executes everything at the top level->Then gives you gencube
# So even though you only wanted gencube, Python still runs:
#print(...)
#ead_file(...)

if __name__ == "__main__":
    l=[]
    fun(l)
    # s=()
    # fun2()