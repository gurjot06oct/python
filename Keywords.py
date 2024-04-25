import asyncio
# Python keywords example

# False, True, None
bool_var = True
if bool_var:
    print(True)
else:
    print(False)

# and, or, not
x = True
y = False
if x and not y or False:
    print("and, or, not operators")

# as
import math as m
print(m.sqrt(25))

# assert
assert 2 + 2 == 4, "Math is broken"

# async, await
async def example():
    await asyncio.sleep(1)
    print("Async function")

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# def
def my_function():
    print("Function called")

my_function()

# del
my_list = [1, 2, 3]
del my_list[1]
print(my_list)

# elif, else, if
x = 10
if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5")

# except, try, finally, raise
try:
    a = int(input("Enter an integer in the range [1, 10]: "))
    if a < 1 or a > 10:
        raise ValueError("Please follow the instructions.")
    # num = int("hello")
except ValueError as e:
    print("Error:", e)
else:
    print("Else block is executed.")
finally:
    print("The End")

# for
for i in range(5):
    print(i)

# from, import
from math import sqrt
print(sqrt(16))

# global
x = 5
def my_func():
    global x
    x = 10

my_func()
print(x)

# in
my_list = [1, 2, 3]
if 2 in my_list:
    print("2 is in the list")

# is
a = [1, 2, 3]
b = a
print(a is b)

# lambda
my_lambda = lambda x: x * 2
print(my_lambda(5))

# nonlocal
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()

outer()

# pass
def my_function():
    pass

# return
def add(a, b):
    return a + b

print(add(2, 3))

# while
i = 0
while i < 5:
    print(i)
    i += 1

# In Python, the with statement is used to simplify exception handling and resource management, particularly for objects that support the context management protocol. The with statement ensures that certain operations are properly initialized and finalized, even if exceptions occur during the execution of the block of code.
# with
with open('example.txt', 'w') as f:
    f.write('Hello, world!')

# yield
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
