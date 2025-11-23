# Python provides a built-in functools.lru_cache decorator to implement an LRU (Least Recently Used) cache.
# Alternatively, you can create one manually using the OrderedDict from collections.
#
# Example using functools:

from functools import lru_cache

@lru_cache(maxsize=3)
def add(a, b):
    return a + b

print(add(1, 2))  # Calculates and caches result
print(add(1, 2))  # Retrieves result from cache