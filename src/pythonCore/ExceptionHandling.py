
l =[4,5,6,7,8,8,9,0]

# It will through IndexError :because there is no value at 8 index as value is only till 7 index.
# for i in range(len(l)+1):
#     print(l[i])

# Try - Except Block:
# try:
#     for i in range(len(l)+1):
#         print(l[i])
# except Exception as e:
#     print("Error in code is :",e)

#=================================================
# Try - Except,else, finally  Block:
#else block: This optional block is executed only if no exception occurs within the try block.
# It is useful for code that should only run when the try block executes successfully.
#finally :This optional block is always executed,regardless of whether an exception occurred or not.

# try:
#     #for i in range(len(l)+1):  #for with error
#      for i in range(len(l)):  #for with no error
#         print(l[i])
# except Exception as e:
#     print("Error in code is :",e)
# else:
#     print("try block run successfully, so i can run now")
# finally:     #Note: finally block can give error if you made runTime error mistake.
#     print("Any way i will run, if exception occur or not")
#=================================================

# write a code to ask user again and again if input is wrong

#recurcive approach
# def recInt():
#     try:
#         a= int(input())
#         # return a
#     except Exception as ee:
#         print("Entre correct value in numbers:",ee)
#         return recInt()
#     else:
#         return a
#
# #loop approach
# def lopInt():
#     while True:
#         try:
#             a= int(input())
#             break
#         except ValueError:
#             print("your inserted value is not correct, Enter Again")
#             continue
#
#     return a
#
# result=lopInt()
# print("input value is : ",result)

#=================================================
#Raise and CustomError Exception:

class CustomError(Exception):
    """A custom exception for specific error scenarios."""
    pass

def fun(num):
    try:
        if num < 0:
            raise CustomError("Pass value greate then one")
    except CustomError as e:
        print(f"please :",{e})

    print(num)

fun(-1)