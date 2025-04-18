# getattr(): Returns the value of the named attribute of an object
class MyClass:
    x = 10
value = getattr(MyClass(), 'x', 'default_value')
print(value)



# hasattr(): Returns True if an object has the given attribute
class MyClass:
    x = 10
has_attribute = hasattr(MyClass(), 'x')


# setattr(): Sets the value of the attribute of an object
setattr(MyClass(5), 'x', 10)