# The `not` operator in Python is a unary operator, meaning it operates on a single operand.
# It returns the boolean inverse of the operand.

# Example 1
result1 = not True
# True is the operand
# The `not` operator inverts it
# Result is False
print(result1)  # output: False

# Example 2
result2 = not False
# False is the operand
# The `not` operator inverts it
# Result is True
print(result2)  # output: True

# Example 3
result3 = not 0
# 0 is considered False in a boolean context
# The `not` operator inverts it
# Result is True
print(result3)  # output: True

# Example 4
result4 = not "Hello"
# "Hello" is a non-empty string and considered True in a boolean context
# The `not` operator inverts it
# Result is False
print(result4)  # output: False

# Key Points to Remember:
# - The `not` operator returns the boolean inverse of its operand.
# - If the operand is True, it returns False.
# - If the operand is False, it returns True.
# - Several values are considered False in a boolean context in Python:
#   None, False, 0, "" (empty string), [] (empty list), {} (empty dictionary),
#   () (empty tuple), and objects of classes that implement a `__bool__()` or `__len__()` method returning False or 0.

# Testing with different values
print(not None)        # output: True (None is considered False)
print(not 1)           # output: False (1 is considered True)
print(not [])          # output: True (empty list is considered False)
print(not [1, 2, 3])   # output: False (non-empty list is considered True)
print(not {})          # output: True (empty dictionary is considered False)
print(not {"a": 1})    # output: False (non-empty dictionary is considered True)
print(not ())          # output: True (empty tuple is considered False)
print(not (1, 2))      # output: False (non-empty tuple is considered True)
