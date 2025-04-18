# Modules:
    # A module is a file containing Python code. This code can include functions, classes, and variables.
    # Modules allow you to logically organize your Python code.
    # You can import modules into other Python scripts to use the functions, classes, and variables defined within them.


# In Python, modules can contain various entities besides functions that can be imported and used. Here are the main entities that can be imported from a module:
# Functions: These are blocks of reusable code that perform a specific task when called.
# Variables: Modules can contain variables that store data. These variables can be simple variables, lists, dictionaries, or any other data structure.
# Classes: Modules can define classes, which are blueprints for creating objects. Classes encapsulate data for the object and methods to manipulate that data.
# Constants: Although Python doesn't have built-in support for constants, you can use variables with uppercase names to represent constants. Modules can define such constants.
# Nested Modules and Packages: A module can import and use other modules or packages, making their contents accessible.
# Special Objects and Constants: Modules might define special objects or constants specific to the domain they represent. For example, a module for mathematical operations might define mathematical constants like pi.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
