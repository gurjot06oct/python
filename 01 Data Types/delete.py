# Getting to Know Python’s del Statement
# del is used to delete objects like variables, list elements, dictionary keys, and more.



# Learning the del Syntax
x = 10
print(x)  # Output: 10
del x
# print(x)  # Raises NameError: name 'x' is not defined




# Understanding the Effects of del
y = [1, 2, 3]
del y[1]
print(y)  # Output: [1, 3]





# Unraveling del vs Garbage Collection
# del removes references, making objects eligible for garbage collection if no other references exist.




# Using del vs Assigning None
z = 10
z = None  # z still exists but holds None
print(z)  # Output: None

w = 20
del w  # w is completely removed
# print(w)  # Raises NameError: name 'w' is not defined





# Deleting Names From a Scope
a = 5
del a
# print(a)  # Raises NameError: name 'a' is not defined




# Removing Items From Mutable Collections

# Deleting Items From a List
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # Output: [1, 3]



# Deleting a Slice From a List
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]
print(my_list)  # Output: [1, 4, 5]



# Removing Keys From Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict)  # Output: {'a': 1, 'c': 3}



# Removing Items From Mutable Nested Collections
nested_list = [[1, 2], [3, 4], [5, 6]]
del nested_list[1][0]
print(nested_list)  # Output: [[1, 2], [4], [5, 6]]



# Deleting Members From Custom Classes

# Removing Class Members: A Generic Example
class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(obj.value)  # Output: 10
del obj.value
# print(obj.value)  # Raises AttributeError: 'MyClass' object has no attribute 'value'



# Removing an Instance Attribute: A Practical Example
class DynamicClass:
    def __init__(self):
        self.attributes = {}

    def add_attribute(self, name, value):
        self.attributes[name] = value

    def remove_attribute(self, name):
        if name in self.attributes:
            del self.attributes[name]

instance = DynamicClass()
instance.add_attribute('age', 25)
print(instance.attributes)  # Output: {'age': 25}
instance.remove_attribute('age')
print(instance.attributes)  # Output: {}



# Preventing Attribute Deletion in Custom Classes
class SafeClass:
    def __init__(self):
        self.value = 10

    def __delattr__(self, name):
        if name == 'value':
            raise AttributeError("Cannot delete 'value' attribute")
        else:
            super().__delattr__(name)

obj = SafeClass()
# del obj.value  # Raises AttributeError: Cannot delete 'value' attribute

# Conclusion
# The del statement is powerful for managing memory and references in Python.
# Proper use of del ensures efficient and clean code management.
