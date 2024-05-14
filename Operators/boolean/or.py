# The `or` operator in Python evaluates expressions from left to right
# and stops as soon as it encounters a value that is considered `True` in a boolean context.
# This is known as short-circuit evaluation.

# Let's look at the provided examples to understand this better.

# Example 1
print(0 or False or 2 or 9)  # output: 2

# Detailed evaluation of Example 1
# 0 or False or 2 or 9
# Step-by-Step Evaluation:
# 0 is False, so move to the next operand
# False is False, so move to the next operand
# 2 is True, so the evaluation stops here
# Result is 2

# Example 2
print("" or None or "Hello" or "World")  # output: "Hello"

# Detailed evaluation of Example 2
# "" or None or "Hello" or "World"
# Step-by-Step Evaluation:
# "" is False, so move to the next operand
# None is False, so move to the next operand
# "Hello" is True, so the evaluation stops here
# Result is "Hello"

# Let's encapsulate these evaluations in variables with comments
result1 = 0 or False or 2 or 9
# 0 is False, so move to the next operand
# False is False, so move to the next operand
# 2 is True, so the evaluation stops here
# Result is 2
print(result1)  # output: 2

result2 = "" or None or "Hello" or "World"
# "" is False, so move to the next operand
# None is False, so move to the next operand
# "Hello" is True, so the evaluation stops here
# Result is "Hello"
print(result2)  # output: "Hello"

# Key Points to Remember:
# - The `or` operator stops at the first `True` value it encounters and returns it.
# - If all values are `False`, it returns the last value.
# - In Python, the following are considered `False` in a boolean context: 
#   None, False, 0, "" (empty string), [] (empty list), {} (empty dictionary), 
#   () (empty tuple), and objects of classes that implement a `__bool__()` or `__len__()` method returning False or 0.

# Testing with different values
print(None or 1)        # output: 1
print(False or True)    # output: True
print(0 or 1)           # output: 1
print([] or [1, 2, 3])  # output: [1, 2, 3]
print({} or {"a": 1})   # output: {'a': 1}
print(()) or (1, 2)     # output: (1, 2)
