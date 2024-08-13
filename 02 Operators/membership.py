# The `in` operator in Python is used to check if a value exists within a sequence or collection
# It returns `True` if the value is found, otherwise it returns `False`


# Example 1: Using `in` with Strings
result1 = 'a' in 'apple'
# Checks if the character 'a' is present in the string 'apple'
# 'a' is found, so it returns True
print(result1)  # output: True



# Example 2: Using `in` with Lists
result2 = 2 in [1, 2, 3]
# Checks if the number 2 is present in the list [1, 2, 3]
# 2 is found, so it returns True
print(result2)  # output: True



# Example 3: Using `in` with Tuples
result3 = 'x' in ('x', 'y', 'z')
# Checks if the character 'x' is present in the tuple ('x', 'y', 'z')
# 'x' is found, so it returns True
print(result3)  # output: True




# Example 4: Using `in` with Sets
result4 = 3 in {1, 2, 3}
# Checks if the number 3 is present in the set {1, 2, 3}
# 3 is found, so it returns True
print(result4)  # output: True




# Example 5: Using `in` with Dictionaries
result5 = 'key1' in {'key1': 'value1', 'key2': 'value2'}
# Checks if the string 'key1' is a key in the dictionary {'key1': 'value1', 'key2': 'value2'}
# 'key1' is found, so it returns True
print(result5)  # output: True





# Key Points to Remember:
# - The `in` operator checks for membership in sequences or collections
# - It returns True if the value is found, otherwise it returns False
# - It can be used with strings, lists, tuples, sets, and dictionaries

# Testing with different collections and values
print('b' in 'banana')          # output: True (substring check in string)
print(5 in [1, 2, 3, 4, 5])     # output: True (element check in list)
print('c' in ('a', 'b', 'c'))   # output: True (element check in tuple)
print(10 in {10, 20, 30})       # output: True (element check in set)
print('key2' in {'key1': 1, 'key2': 2})  # output: True (key check in dictionary)

# Checking for non-existing elements
print('x' in 'apple')           # output: False (substring not in string)
print(7 in [1, 2, 3, 4, 5])     # output: False (element not in list)
print('d' in ('a', 'b', 'c'))   # output: False (element not in tuple)
print(40 in {10, 20, 30})       # output: False (element not in set)
print('key3' in {'key1': 1, 'key2': 2})  # output: False (key not in dictionary)
