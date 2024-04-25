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

# Tuple (Tuples do not support division)
tuple_value_1 = (1, 2)
tuple_value_2 = (3, 4)

# String (Strings do not support division)
string_value_1 = "Hello"
string_value_2 = "World"

# Dictionary (Dictionaries do not support division)
dict_value_1 = {'a': 10, 'b': 20}
dict_value_2 = {'c': 30, 'd': 40}

# Set (Sets do not support division)
set_value_1 = {1, 2}
set_value_2 = {2, 3}

# List (Lists do not support division)
list_value_1 = [1, 2]
list_value_2 = [3, 4]


# All combinations of division operators
combinations = [
    (int_value_1 / int_value_2),
    (int_value_1 / bool_value_1),
    (int_value_1 / complex_value_1),
    (int_value_1 / float_value_1),
    # (int_value_1 / tuple_value_1), # Division operation is not defined for integer and tuple
    # (int_value_1 / string_value_1), # Division operation is not defined for integer and string
    # (int_value_1 / dict_value_1), # Division operation is not defined for integer and dictionary
    # (int_value_1 / set_value_1), # Division operation is not defined for integer and set
    # (int_value_1 / list_value_1), # Division operation is not defined for integer and list
    
    (bool_value_2/bool_value_1), 
    (bool_value_1 / complex_value_1), 
    (bool_value_1 / float_value_1),
    # (bool_value_1 / tuple_value_1), # Division operation is not defined for boolean and tuple
    # (bool_value_1 / string_value_1), # Division operation is not defined for boolean and string
    # (bool_value_1 / dict_value_1), # Division operation is not defined for boolean and dictionary
    # (bool_value_1 / set_value_1), # Division operation is not defined for boolean and set
    # (bool_value_1 / list_value_1), # Division operation is not defined for boolean and list
    
    (complex_value_1 / complex_value_2),
    (complex_value_1 / float_value_1),
    # (complex_value_1 / tuple_value_1), # Division operation is not defined for complex and tuple
    # (complex_value_1 / string_value_1), # Division operation is not defined for complex and string
    # (complex_value_1 / dict_value_1), # Division operation is not defined for complex and dictionary
    # (complex_value_1 / set_value_1), # Division operation is not defined for complex and set
    # (complex_value_1 / list_value_1), # Division operation is not defined for complex and list
    
    (float_value_1 / float_value_2),
    # (float_value_1 / tuple_value_1), # Division operation is not defined for float and tuple
    # (float_value_1 / string_value_1), # Division operation is not defined for float and string
    # (float_value_1 / dict_value_1), # Division operation is not defined for float and dictionary
    # (float_value_1 / set_value_1), # Division operation is not defined for float and set
    # (float_value_1 / list_value_1), # Division operation is not defined for float and list
    
    # (tuple_value_1 / tuple_value_2), # Division operation is not defined for tuple
    
    # (string_value_1 / string_value_2), # Division operation is not defined for string
    
    # (dict_value_1 / dict_value_2), # Division operation is not defined for dictionary
    
    # (set_value_1 / set_value_2), # Division operation is not defined for set
    
    # (list_value_1 / list_value_2) # Division operation is not defined for list
]

# Printing the combinations
for index, result in enumerate(combinations):
    print(f"Combination division {index + 1}: {result}")


# All combinations of floor division operators
combinations = [
    # Float // Int -> Float
    (float_value_1 // int_value_2),
    
    # Int // Float -> Float
    (int_value_1 // float_value_2),
    
    # Int // Int -> Int
    (int_value_1 // int_value_2),
    
    # Float // Float -> Float
    (float_value_1 // float_value_2)
]

# Printing the combinations
for index, result in enumerate(combinations):
    print(f"Combination floor division {index + 1}: {result}")



# All combinations of modulus operators
combinations = [
    # Float % Int
    (float_value_1 % int_value_2),
    
    # Int % Float
    (int_value_1 % float_value_2),
    
    # Int % Int
    (int_value_1 % int_value_2),
    
    # Float % Float
    (float_value_1 % float_value_2)
]

# Printing the combinations
for index, result in enumerate(combinations):
    print(f"Combination modulus {index + 1}: {result}")
