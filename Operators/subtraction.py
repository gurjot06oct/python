# Integers
int_value_1 = 10
int_value_2 = 5

# Boolean
bool_value_1 = True
bool_value_2 = False

# Complex
complex_value_1 = 3 + 4j
complex_value_2 = 1 + 2j

# Float
float_value_1 = 3.14
float_value_2 = 1.5

# Tuple
tuple_value_1 = (1, 2)
tuple_value_2 = (3, 4)

# String
string_value_1 = "Hello"
string_value_2 = " World"

# Dictionary
dict_value_1 = {'a': 1, 'b': 2}
dict_value_2 = {'c': 3, 'd': 4}

# Set
set_value_1 = {1, 2}
set_value_2 = {2, 3}

# List
list_value_1 = [1, 2]
list_value_2 = [3, 4]

# All combinations of subtraction operators
combinations = [
    (int_value_1 - int_value_2),
    (int_value_1 - bool_value_1),
    (int_value_1 - complex_value_1),
    (int_value_1 - float_value_1),
    # (int_value_1 - tuple_value), # Subtraction operation is not defined for integer and tuple
    # (int_value_1 - string_value), # Subtraction operation is not defined for integer and string
    # (int_value_1 - dict_value), # Subtraction operation is not defined for integer and dictionary
    # (int_value_1 - set_value), # Subtraction operation is not defined for integer and set
    # (int_value_1 - list_value), # Subtraction operation is not defined for integer and list
    

    (bool_value_1 - int_value_1),
    (bool_value_1 - bool_value_2),
    (bool_value_1 - complex_value_1),
    (bool_value_1 - float_value_1),
    # (bool_value_1 - tuple_value), # Subtraction operation is not defined for boolean and tuple
    # (bool_value_1 - string_value), # Subtraction operation is not defined for boolean and string
    # (bool_value_1 - dict_value), # Subtraction operation is not defined for boolean and dictionary
    # (bool_value_1 - set_value), # Subtraction operation is not defined for boolean and set
    # (bool_value_1 - list_value), # Subtraction operation is not defined for boolean and list
    


    (complex_value_1 - int_value_1),
    (complex_value_1 - bool_value_2),
    (complex_value_1 - complex_value_2),
    (complex_value_1 - float_value_1),
    # (complex_value_1 - tuple_value), # Subtraction operation is not defined for complex and tuple
    # (complex_value_1 - string_value), # Subtraction operation is not defined for complex and string
    # (complex_value_1 - dict_value), # Subtraction operation is not defined for complex and dictionary
    # (complex_value_1 - set_value), # Subtraction operation is not defined for complex and set
    # (complex_value_1 - list_value), # Subtraction operation is not defined for complex and list
    

    (float_value_1 - int_value_1),
    (float_value_1 - bool_value_2),
    (float_value_1 - complex_value_2),
    (float_value_1 - float_value_2),
    # (float_value_1 - tuple_value), # Subtraction operation is not defined for float and tuple
    # (float_value_1 - string_value), # Subtraction operation is not defined for float and string
    # (float_value_1 - dict_value), # Subtraction operation is not defined for float and dictionary
    # (float_value_1 - set_value), # Subtraction operation is not defined for float and set
    # (float_value_1 - list_value), # Subtraction operation is not defined for float and list
    
    # (tuple_value_1 - tuple_value_2), # Subtraction operation is not defined for tuples
    # (tuple_value_1 - string_value), # Subtraction operation is not defined for tuple and string
    # (tuple_value_1 - dict_value), # Subtraction operation is not defined for tuple and dictionary
    # (tuple_value_1 - set_value), # Subtraction operation is not defined for tuple and set
    # (tuple_value_1 - list_value), # Subtraction operation is not defined for tuple and list
    
    # (string_value_1 - string_value_2), # Subtraction operation is not defined for string
    # (string_value_1 - dict_value), # Subtraction operation is not defined for string and dictionary
    # (string_value_1 - set_value), # Subtraction operation is not defined for string and set
    # (string_value_1 - list_value), # Subtraction operation is not defined for string and list
    
    # (dict_value_1 - dict_value_2), # Subtraction operation is not defined for dictionary
    
    (set_value_1 - set_value_2), # Subtraction operation for set is difference
    
    # (list_value_1 - list_value_2) # Subtraction operation is not defined for list
]

# Printing the combinations
for index, result in enumerate(combinations):
    print(f"Combination {index + 1}: {result}")
