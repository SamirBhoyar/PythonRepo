#reverse String and check palindrome
from collections import Counter


def palindrome(str):
    return str==str[::-1]

str="matdam"
print("it is a palindrome" if palindrome(str) else "it is not a palindrome")

#count character frequency

str1="mississippi"
dict ={}

for char in str1:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1

print(dict)
# or

print(Counter(str1))