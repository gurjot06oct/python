# Integer
print(42 == 42)       # True
print(42 != 42)       # False

# Boolean
print(True == False)  # False
print(True != False)  # True

# Complex
print(1 + 2j == 1 + 2j)   # True
print(1 + 2j != 1 + 2j)   # False

# Float
print(3.14 == 3.14)   # True
print(3.14 != 3.14)   # False

# Integer vs Float
print(42 == 42.0)       # True
print(42 != 42.0)       # False

# Integer vs Complex
print(42 == 42 + 0j)    # True
print(42 != 42 + 0j)    # False

# Integer vs Boolean
print(42 == True)       # False
print(42 != True)       # True

# Float vs Complex
print(3.14 == 3.14 + 0j)    # True
print(3.14 != 3.14 + 0j)    # False

# Float vs Boolean
print(3.14 == True)         # False
print(3.14 != True)         # True

# Complex vs Boolean
print(1 + 2j == True)       # False
print(1 + 2j != True)       # True


# Tuple
print((1, 2) == (1, 2))   # True
print((1, 2) != (1, 2))   # False

# Dictionary
print({'a': 1} == {'a': 1})   # True
print({'a': 1} != {'a': 1})   # False

# List
print([1, 2] == [1, 2])   # True
print([1, 2] != [1, 2])   # False

# Set
print({1, 2} == {1, 2})   # True
print({1, 2} != {1, 2})   # False

# String
print("hello" == "hello")   # True
print("hello" != "hello")   # False

# NoneType
print(None == None)   # True
print(None != None)   # False
