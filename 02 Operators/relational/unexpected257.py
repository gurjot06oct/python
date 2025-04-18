# Interactive Shell Example
# In an interactive shell, each line is compiled and executed separately.

# Separate lines in the interactive shell
a = 257
b = 257
print(a is b)  # False because each line is a separate statement

# Script Example
# In a script, the compiler can optimize by reusing literals.

# This would be the contents of a script file (e.g., script.py):
a = 257
b = 257
print(a is b)  # True because the compiler reuses the same object

# Function Example in Interactive Shell
# When defining a function, the entire function body is compiled as a single code block.
def test():
    a = 257
    b = 257
    print(a is b)  # True because the compiler reuses the same object

test()

# Float Example
# Python does not cache float literals, but similar optimizations can happen within the same statement.

# Separate lines
a = 5.0
b = 5.0
print(a is b)  # False, float literals are not cached

# Same statement
a = 5.0; b = 5.0
print(a is b)  # True, because the literals are assigned in the same statement

# Tuple Example
# Tuples themselves are not cached, but their elements might be reused if they are the same and within an optimizable context.

# Separate lines
a = (257, 258)
b = (257, 258)
print(a[0] is b[0])  # False, different tuple objects
print(a[1] is b[1])  # False, different tuple objects

# Same statement
a = (257, 258); b = (257, 258)
print(a[0] is b[0])  # True, elements are reused in the same statement
print(a[1] is b[1])  # True, elements are reused in the same statement

# Summary:
# - In the interactive shell, separate statements result in different objects for 257.
# - In a script, the compiler optimizes and reuses the same object for 257.
# - Within a function, the compiler reuses the same object for 257.
# - Floats and tuple elements can also be optimized within the same statement, even though they are not cached like small integers.
