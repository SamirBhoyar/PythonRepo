text = "  Hello Samir, Welcome to Data Engineering World!  "

# 1. lower() and upper()
print(text.lower())   # convert to lowercase
print(text.upper())   # convert to uppercase

# 2. strip(), lstrip(), rstrip()
print(text.strip())   # remove spaces from both sides
print(text.lstrip())  # remove left spaces
print(text.rstrip())  # remove right spaces

# 3. replace()
print(text.replace("Samir", "Data Engineer"))

# 4. find() and index()
print(text.find("Welcome"))   # returns index, -1 if not found
# print(text.index("Python")) # would throw error if not found

# 5. startswith() and endswith()
print(text.strip().startswith("Hello"))
print(text.strip().endswith("!"))

# 6. split()  ⭐ IMPORTANT
words = text.strip().split(" ")
print(words)
# ['Hello', 'Samir,', 'Welcome', 'to', 'Data', 'Engineering', 'World!']

# 7. join()
joined_text = "-".join(words)
print(joined_text)

# 8. count()
print(text.count("o"))  # count occurrences

# 9. isalpha(), isdigit(), isalnum()
print("Samir".isalpha())   # True
print("123".isdigit())     # True
print("Samir123".isalnum())# True

# 10. title() and capitalize()
print(text.title())
print(text.capitalize())

# 11. split with delimiter
data = "apple,banana,grape"
print(data.split(","))
# ['apple', 'banana', 'grape']

# 12. split with maxsplit
sentence = "one two three four"
print(sentence.split(" ", 2))
# ['one', 'two', 'three four']
print('=============================')
# 13. Check if Two Strings are Anagrams
# Use case: Data matching / dedup
# => An anagram is when two strings have the same characters with the same frequency, but possibly in a different order.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagram("apple", "banana"))
print('=============================')
# 14. Count Word Frequency
# Use case: Text analytics / logs
# =>
from collections import Counter

def word_count(s):
    return Counter(s.split())
s="kkk kere ttt kkk  ttt tfqv ttt"
print(word_count(s))