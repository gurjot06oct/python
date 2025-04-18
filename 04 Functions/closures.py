# A closure in Python refers to a function that retains the scope of its 
# enclosing lexical environment even after the enclosing code has finished 
# execution. This means that the function can access and modify variables defined 
# in its enclosing scope, even if that scope is no longer active.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure by calling outer_function
closure = outer_function(5)

# Use the closure
result = closure(3)  # This will return 5 + 3 = 8
print(result)

# In this example:

# outer_function defines an inner function inner_function that takes a parameter y. Inside inner_function, it uses a variable x from its enclosing scope (the outer_function scope).
# When outer_function is called with an argument 5, it returns inner_function with x set to 5. At this point, outer_function finishes execution, but the returned inner_function still retains access to the variable x.
# We assign the returned function to a variable closure.
# We then call closure with an argument 3. Since closure retains access to the variable x (which is 5), it adds 3 to 5 and returns 8.
# So, in essence, a closure allows a function to remember and access variables from its enclosing scope even after that scope has finished executing. This can be particularly useful for creating functions with custom behavior or for implementing function factories.