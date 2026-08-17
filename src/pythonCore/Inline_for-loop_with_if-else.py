# 1. Basic Inline for with if-else
'''Syntax
[expression_if_true if condition else expression_if_false for item in iterable]'''

# Example 1: Even / Odd Label
nums = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in nums]
print(result)

# The flow is:
# FOR loop runs first → THEN if-else is evaluated per item

# Output
# ['odd', 'even', 'odd', 'even', 'odd']
print("-----------------------------------")
# 2. Inline for with only if (filtering)
'''Syntax
[expression for item in iterable if condition]'''

# Example
nums = [1, 2, 3, 4, 5]
result = [x for x in nums if x % 2 == 0]
print(result)

#The flow is:
# result = []
# for x in nums:
#     if x % 2 == 0:
#         result.append("even")
#     else:
#         result.append("odd")
# FOR runs → IF filters → THEN value added

'''[x      for x in nums]
 ↑           ↑
what to add   loop
Left side → expression (what to return)
Right side → loop (iteration)
'''
# Output
# [2, 4]
print("-----------------------------------")
'''Important Difference
Type	Syntax	Use
if-else inline	before for	transformation
only if	after for	filtering
'''
# 3. Your Use Case (Palindrome Check)
words = ["madam", "hello", "level"]
result = ["palindrome" if w == w[::-1] else "not palindrome" for w in words]
print(result)
print("-----------------------------------")

# 4. Nested Inline (Advanced)
nums = [1, 2, 3, 4]
result = ["even" if x % 2 == 0 else "odd" for x in nums if x > 1]
print(result)

'''Final Takeaway
Transformation → if-else before for
Filtering → if after for
Clean, concise, Pythonic
'''