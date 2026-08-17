
"""
num = int(input("enter the number"))

if num >= 0:
    print("number is positive")
    if (num % 2)==0:
     print("{0} its even number".format(num))
    else: print("{0} its a odd number".format(num))
        
else:
    print("number is negative")


leap year:  - leap year divid by 4 execpt century year which has 00 like 2000
               - century year can only be leap year if it is divisible by 400 and 100 """

""" 
year =int(input('enter the year : '))

if (year % 400 == 0) and (year % 100 ==0):
   print("{yr} is leap year".format(yr=year))

elif (year % 4 == 0) and (year % 100 != 0):
   print("{yr} is a leap year".format(yr=year))

else:
   print('{yr} is not a leap year')

"""
"""
#Prime number: Number which is  greater than 1 and which can only be divided by 1 or itself. 
num = int(input("enter the number : "))

if num>0:
    if num==1: print(" 1 is not the prime number")
    else:
        for i in range (2, num):
            if (num %i ==0):
                print("{no} is not a prime number".format(no=num))
                break
            else: print(i)
        else: print("{0} it is a prime number".format(num))

else: print("{no} is not a prime number".format(no=num))

"""

"""
 #----------------------------------------------------------------
Factorical number: The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720.
"""
num =7
factorial=1

if num==0:
        print("factoral of '0' is 1")
else:
    for i in range(1 ,num + 1): 
        factorial= factorial*i        
    print("factoral of",num, "is",factorial)
"""
def factorial(x):
    #This is a recursive functionto find the factorial of an integer

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)
   
"""

#----------------------------------------------------------------
#   for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial) 

  #que:
  # Is it possible to construct a Python program that calculates the mean of numbers in a list?

n =int(input("How many number mean you want: "))
list1=[]

for i in range(1,n+1):
    item= int(input("enter the number:"))
    list1.append(item)

mean= sum(list1)/n

print(f"mean of given valuse are : {mean}")


"""
Here is source code of the Python Program to check whether a given number is a palindrome. The program output is also shown below.

 
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")"""

#OR

"""def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
    return str(n) == s[::-1]
    
# Get the number from the user
n = int(input("Enter number: "))

# Check if the number is a palindrome
if is_palindrome(n):
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome.")

  """

