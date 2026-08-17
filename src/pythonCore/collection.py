
#1. LIST  :- Definition: An ordered, mutable collection that allows duplicates.
l = [1, 2, 3]
l.append(4)        # [1,2,3,4]
l.extend([5, 6])   # [1,2,3,4,5,6]
l.insert(1, 10)    # [1,10,2,3,4,5,6]
l.remove(2)        # removes value 2
l.pop()            # removes last element
l.sort()           # sorts list
l.reverse()        # reverse list
l.clear()          # []
print('---------------')

#2. Tuple :- Definition: An ordered, immutable collection.
t = (1, 2, 3)
# t.append(4) ❌ ERROR
'''Workaround:
Convert → modify → convert back'''

temp = list(t)
temp.append(4)
t = tuple(temp)
print('---------------')

#3. Set:- Definition: An unordered collection of unique elements.

s = {1, 2, 3}

s.add(4)             # {1,2,3,4}
s.remove(2)          # removes 2 (error if not present)
s.discard(5)         # no error if not present
s.pop()              # removes random element
s.update([5, 6])     # add multiple elements
s.clear()            # empty set
print('---------------')

#4. Dictionary :- Definition: A collection of key-value pairs.
# Mutable, Keys must be unique but value can duplicate.

d = {"a": 1, "b": 2}

d["c"] = 3           # add/update
d.update({"d": 4})   # add multiple
d.pop("a")           # remove key
d.popitem()          # remove last inserted
d.clear()            # empty dict