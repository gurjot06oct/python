#creating dict
# Using curly braces
my_dict = {"name": "John", "age": 30}

# Using dict() constructor
my_dict = dict(name="John", age=30)



# Using fromkeys
keys = ['name', 'age', 'city']
default_value = 'unknown'
# Create a dictionary with specified keys and default value
my_dict = dict.fromkeys(keys, default_value)
print(my_dict) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
# fromkeys can only be used with dict class but not the object
my_dict.fromkeys(["a","b","c"],default_value)
print(my_dict) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}



# access elements
print(my_dict["name"])  # Output: John

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f) # True

del a["one"]
print(a)

# key in dictionary
print("one" in a) # False

# dict comprehension
square_dict = {x: x*x for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(square_dict)


# copying Dict
square2 = square_dict.copy()
print(square2,id(square2))
print(square_dict,id(square_dict))


# get(key[, default])
print("Value:",square2.get(2))
# Output: 4

# items()
for key,val in square2.items():
    print(key,val)

# Output: 
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25

# keys()
for key in square2.keys():
    print(key)

# Output:
# 1
# 2
# 3
# 4
# 5

# values()
for val in square2.values():
    print(val)

# Output:
# 1
# 4
# 9
# 16
# 25

# pop(key) -> value (key is required)
# pop removes the key and its value
print(square2.pop(4))
# Output - 16


# pop item
print(square2.popitem())
# Output: (5,25)

# reversed()
for x in reversed(square2.keys()):
    print(x)
# Output: 
# 3
# 2
# 1

print(square2)
# {1: 1, 2: 4, 3: 9}

# setdefault(key[,default=None]) -> value
# It sets the key if not present to default Value.
print(square2.setdefault(2))
# Output: 4

# update (like creating)
square2.update({2:8})
print(square2)
# Output: {1: 1, 2: 8, 3: 9}

# clearning dict
square_dict.clear()
print(square_dict)
# Output: {}


# deleting whole dict
del a
# print(a) gives error as a is not defined