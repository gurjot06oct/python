### A Survey of Definite Iteration in Programming
# Definite iteration refers to looping a specific number of times or over a fixed collection of items. The `for` loop is a common structure used to achieve this in many programming languages.

### Numeric Range Loop
# A numeric range loop iterates over a sequence of numbers. This is often used to execute a block of code a specified number of times.


for i in range(5):  # Loops from 0 to 4
    print(i)
# Output: 0 1 2 3 4


### Collection-Based or Iterator-Based Loop
# These loops iterate over elements in a collection or an iterator, such as lists, tuples, sets, or dictionaries in Python.
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
# Output: 1 2 3 4 5



### The Python for Loop
# Python’s `for` loop is designed to iterate over iterable objects (e.g., lists, tuples, dictionaries).
for item in [1, 2, 3]:
    print(item)
# Output: 1 2 3




### The Guts of the Python for Loop
# Under the hood, a `for` loop in Python creates an iterator from the iterable and repeatedly calls `next()` on it.
my_list = [1, 2, 3]
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
# Output: 1 2 3




### Altering for Loop Behavior
# You can alter the behavior of a `for` loop using `break`, `continue`, and the `else` clause.

### The break and continue Statements
    # - `break` exits the loop immediately.
    # - `continue` skips the current iteration and moves to the next.
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4 

### The else Clause
# The `else` clause in a `for` loop executes if the loop completes without encountering a `break`.

for i in range(5):
    print(i)
else:
    print("Loop completed without break")
# Output: 0 1 2 3 4
# Output: Loop completed without break

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break")
# Output: 0 1 2


### Conclusion
# The `for` loop is a powerful and flexible construct in Python, allowing for iteration over various data structures and altering loop behavior with control statements like `break`, `continue`, and `else`. Understanding these concepts enhances your ability to write efficient and readable code.