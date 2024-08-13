# In Python, `==` and `is` are both used to compare objects, but they serve different purposes and behave differently.
# Optimization range: [-5,256]
### `==` Operator
	# - **Purpose:** The `==` operator is used to check if the values of two objects are equal.
	# - **Behavior:** It compares the values of the objects to see if they are equivalent. This means that even if two objects are distinct in memory, if their contents are the same, `==` will return `True`.



### `is` Operator

	# - **Purpose:** The `is` operator is used to check if two references point to the same object in memory.
	# - **Behavior:** It compares the identities of the objects, meaning it returns `True` if both variables point to the same object (same memory location).


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True, because the contents of a and b are the same.
c = a

print(a is b)  # Output: False, because a and b are distinct objects in memory.
print(a is c)  # Output: True, because c is a reference to the same object as a.


### Key Differences
	# 1. **Value vs Identity Comparison:**
	# - `==` checks if the values are the same.
	# - `is` checks if the objects are the same instance.

	# 2. **Usage Context:**
	# - Use `==` when you need to compare the data/values stored in the objects.
	# - Use `is` when you need to check if two variables point to the exact same object.

### Examples to Illustrate Differences

#### Immutable Objects
	# For small integers and interned strings, Python may reuse objects, making `is` sometimes return `True` for seemingly different objects.

x = 256
y = 256
print(x is y)  # Output: True, because Python reuses small integer objects.

x = 257
y = 257
print(x is y)  # Expected Output: False, because these are distinct objects in memory.
# Real Output : True

a = 'hello'
b = 'hello'
print(a is b)  # Output: True, because of string interning.

a = 'hello world'
b = 'hello world'
print(a is b)  # Expected Output: False, as these are distinct string objects.
# Real Output: True


# Refer to the reason for these unexpected Outputs


#### Mutable Objects

	# With mutable objects like lists or dictionaries, `is` will almost always return `False` unless explicitly assigned to the same object.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True
print(a is b)  # Output: False

c = a
print(a is c)  # Output: True

# In summary, use `==` for comparing values and `is` for comparing object identities.