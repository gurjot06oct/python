# Global variable
global_var = 10

def outer_function():
    # Enclosing scope variable
    enclosing_var = 20

    def inner_function():
        # Local variable
        local_var = 30

        # Modifying global variable using global keyword
        global global_var
        global_var = global_var + 1

        # Accessing global variable
        print("Inside inner_function, global_var:", global_var)


        # Modifying enclosing scope variable using nonlocal keyword
        nonlocal enclosing_var
        enclosing_var = enclosing_var + 1

        # Accessing enclosing scope variable
        print("Inside inner_function, enclosing_var:", enclosing_var)

        # Accessing local variable
        print("Inside inner_function, local_var:", local_var)

    inner_function()
    print("After inner_function, global_var:", global_var)
    print("After inner_function, enclosing_var:", enclosing_var)

outer_function()
print("After outer_function, global_var:", global_var)
