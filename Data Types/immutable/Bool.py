#empty
print(bool()) # False

#numbers
print(bool(0))# False
print(bool(1))# True
print(bool(-1))# True
print(bool(5))# True

#boolValues
print(bool(True))# True
print(bool(False))# False

#float
print(bool(2.6))# True
print(bool(0.0))# False
print(bool(0.01))# True

#complex
print(bool(5 + 0j)) # True
print(bool(0 + 5j)) # True
print(bool(0 + 0j)) # False

#dict
print(bool({})) # False
print(bool({"key":42})) # True

#set
print(bool({})) # False
print(bool({1})) # True

#tuple
print(bool(())) # False
print(bool((1,))) # True

#list
print(bool([])) # False
print(bool([1])) # True

#string
print(bool("")) # False
print(bool(" ")) # True
print(bool("1")) # True