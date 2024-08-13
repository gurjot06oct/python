# Function Definition
def my_function(parameter1, parameter2):
    # Function body
    pass

# Function Call
value1 = 31
value2 = 30
result = my_function(value1, value2)

# Return Statement
def add(a, b):
    return a + b

# parameter
def greet(name):
    print("Hello,", name)

greet("Alice")

# Arguments
greet("Bob")  # "Bob" is an argument

# Default Parameters
def greet(name="world"):
    print("Hello,", name)

greet()  # Output: Hello, world

# Keyword Arguments
def greet(name):
    print("Hello,", name)

greet(name="Alice")


# docstring
def add(a, b):
    """
    This function adds two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of a and b.
    """
    return a + b