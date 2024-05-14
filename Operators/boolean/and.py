# The `and` operator in Python evaluates expressions from left to right
# and stops as soon as it encounters a value that is considered `False` in a boolean context.
# This is known as short-circuit evaluation.


# Let's look at the provided examples to understand this better.

# Example 1
print(1 and 2 and 0 and 9)  # output: 0

# Detailed evaluation of Example 1
# 1 and 2 and 0 and 9
# Step-by-Step Evaluation:
# 1 is True, so move to the next operand
# 2 is True, so move to the next operand
# 0 is False, so the evaluation stops here
# Result is 0

# Example 2
print("First" and "" and "last")  # output: ""

# Detailed evaluation of Example 2
# "First" and "" and "last"
# Step-by-Step Evaluation:
# "First" is True, so move to the next operand
# "" is False, so the evaluation stops here
# Result is ""


result1 = 1 and 2 and 0 and 9
# 1 is True, so move to the next operand
# 2 is True, so move to the next operand
# 0 is False, so the evaluation stops here
# Result is 0
print(result1)  # output: 0

result2 = "first" and "" and "last"
# "first" is True, so move to the next operand
# "" is False, so the evaluation stops here
# Result is ""
print(result2)  # output: ""

# Key Points to Remember:
# - The `and` operator stops at the first `False` value it encounters and returns it.
# - If all values are `True`, it returns the last value.
# - In Python, the following are considered `False` in a boolean context: 
#   None, False, 0, "" (empty string), [] (empty list), {} (empty dictionary), 
#   () (empty tuple), and objects of classes that implement a `__bool__()` or `__len__()` method returning False or 0.

# Testing with different false values
print(None and 1)        # output: None
print(False and True)    # output: False
print(0 and 1)           # output: 0
print([] and [1, 2, 3])  # output: []
print({} and {"a": 1})   # output: {}
print(())                # output: ()
