# Comparison Operators
# < (less than)
# <= (less than or equal to)
# > (greater than)
# >= (greater than or equal to)

# Numerical Types (int, float, complex)

# int and float comparisons
print(3 < 5)       # True
print(3.5 <= 3)    # False
print(4 >= 4.0)    # True
print(7 > 6.5)     # True

# complex comparisons (will raise TypeError)
try:
    print(3 + 4j < 5 + 6j)  # TypeError
except TypeError as e:
    print(e)  # '<' not supported between instances of 'complex' and 'complex'

# Boolean Type
print(True < False)    # False
print(True <= True)    # True
print(False >= False)  # True
print(False > True)    # False
print(True < 1)        # False (True is equal to 1)
print(False <= 0)      # True (False is equal to 0)

# None
# In Python, None cannot be compared with itself using the relational operators <, <=, >, and >=. Attempting to do so will raise a TypeError. This is because None is not a value that can be logically ordered with these operators.

# strings
print("apple" < "banana")   # True
print("apple" > "banana")   # False
print("apple" <= "banana")  # True
print("apple" >= "banana")  # False

# Collection Types (tuple, set, dict, list)

# Tuples
print((1, 2) < (1, 3))  # True
print((1, 2, 3) <= (1, 2, 3))  # True
print((2, 1) >= (1, 2))  # True
print((2, 1) > (1, 3))   # True

# Lists
print([1, 2] < [1, 3])  # True
print([1, 2, 3] <= [1, 2, 3])  # True
print([2, 1] >= [1, 2])  # True
print([2, 1] > [1, 3])   # True

# Sets (will raise TypeError)
try:
    print({1, 2} < {1, 3})  # TypeError
except TypeError as e:
    print(e)  # '<' not supported between instances of 'set' and 'set'

# Dictionaries (will raise TypeError)
try:
    print({'a': 1} < {'b': 2})  # TypeError
except TypeError as e:
    print(e)  # '<' not supported between instances of 'dict' and 'dict'

# Summary:
# - int and float: Can be compared directly
# - complex: Cannot be compared using <, <=, >=, >
# - bool: Can be compared with bool and int
# - string, tuple and list: Can be compared lexicographically
# - None, set and dict: Cannot be compared using <, <=, >=, >
