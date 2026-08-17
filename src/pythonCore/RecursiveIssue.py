# with recursively issue with except if function is not return with return keyword :
'''1)When an exception occurs:
2)The except block runs.
3)Inside it, you call fun() again (recursively).
But you don’t return the result of this recursive call.'''

# def fun():
#     try:
#         a= int(input())
#         # return a
#     except Exception as ee:
#         print("Entre correct value :",ee)
#         fun()
#     else:
#         return a
#
# result=fun()
# print(result)

#Note:
# Hence, when the user enters a wrong input first and then a correct one, the inner fun() returns
# a value — but that value is never returned to the outer function call.Thus,
# the top-level call returns None, so print(result) prints None.

#correct code:

def fun():
    try:
        a= int(input())
        # return a
    except Exception as ee:
        print("Entre correct value in number :",ee)
        return fun()
    else:
        return a

result=fun()
print("input value is : ",result)
