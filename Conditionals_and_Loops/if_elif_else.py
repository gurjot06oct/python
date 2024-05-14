### Introduction to the if Statement
x = 10
if x > 5:
    print("x is greater than 5")



### Grouping Statements: Indentation and Blocks
x = 10
if x > 5:
    print("x is greater than 5")
    print("This is part of the same block")
print("This is outside the if block")



### Python: It’s All About the Indentation
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
    print("This is still within the first if block")
print("This is outside all if blocks")



### The else and elif Clauses
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")




### One-Line if Statements
x = 10
if x > 5: print("x is greater than 5")


### Conditional Expressions (Python’s Ternary Operator)
x = 10
result = "x is greater than 5" if x > 5 else "x is 5 or less"
print(result)



### The Python pass Statement
x = 10
if x > 5:
    pass  # Placeholder for future code
else:
    print("x is 5 or less")
print("pass statement executed, but nothing happened")