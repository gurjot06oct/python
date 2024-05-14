### Iterables
# An iterable is any Python object capable of returning its members one at a time, allowing it to be looped over.

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
# Output: 1 2 3

### Iterators
# An iterator is an object representing a stream of data; it returns data one element at a time using the `__next__()` method.

my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration