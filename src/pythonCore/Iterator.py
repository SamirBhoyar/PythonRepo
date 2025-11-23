# Iterable: the object which can be iterate like list,string
# What is an Iterable?
# An Iterable is basically an object that any user can iterate over.
#We can generate an iterator when we pass the object to the iter() method.

# Iterator: iterate a object of list we need to convert iterable to iterator with
#       ->iter() function.
#       -> for() loop internal working is like
#            -> first it iter() the list and then next () applied and the
#                limit the iteration by condition as next() dont know where to stop as it do not hold lenth of object.
# What is an Iterator?
# An Iterator is also an object that helps a user in iterating over another object (that is iterable).
#We use the __next__() method for iterating. This method helps iterators return the next item available from the object.


my_list = [10, 20, 30, 40]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30
print(next(my_iterator))

print('-----------------------')
#While you can manually use iter() and next(), the most common way to iterate through a list (or any iterable)
# in Python is using a for loop, which implicitly handles the creation of the iterator and the calls to next():

for item in my_list:
    print(item)