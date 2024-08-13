# Chaining comparison operators allows you to compare multiple values in a single, readable expression.
# This checks if 1 is less than 5 and 5 is less than 10.
result = 1 < 5 < 10  # True

# You can chain more than two comparisons together.
# This checks if 3 is less than 7, 7 is less than 10, and 10 is less than 15.
another_result = 3 < 7 < 10 < 15  # True

# Chaining also works with equality and inequality operators.
# This checks if 4 is less than 6, and 6 is equal to 6.
yet_another_result = 4 < 6 == 6  # True

# If any comparison in the chain is False, the entire expression is False.
# This checks if 2 is less than 8 and 8 is equal to 10, which is False.
false_result = 2 < 8 == 10  # False

print(result)              # Output: True
print(another_result)      # Output: True
print(yet_another_result)  # Output: True
print(false_result)        # Output: False

### Explanation:
    # 1. `1 < 5 < 10` evaluates to `True` because both `1 < 5` and `5 < 10` are `True`.
    # 2. `3 < 7 < 10 < 15` evaluates to `True` because `3 < 7`, `7 < 10`, and `10 < 15` are all `True`.
    # 3. `4 < 6 == 6` evaluates to `True` because `4 < 6` is `True` and `6 == 6` is `True`.
    # 4. `2 < 8 == 10` evaluates to `False` because `8 == 10` is `False`, even though `2 < 8` is `True`.