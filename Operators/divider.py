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
    # (int_value_1 / tuple_value_1), 
    # (int_value_1 / string_value_1),
    # (int_value_1 / dict_value_1),
    # (int_value_1 / set_value_1),
    # (int_value_1 / list_value_1),
    
    (bool_value_1 / int_value_1), 
    (bool_value_2 / bool_value_1), 
    (bool_value_1 / complex_value_1), 
    (bool_value_1 / float_value_1),
    # (bool_value_1 / tuple_value_1), 
    # (bool_value_1 / string_value_1), 
    # (bool_value_1 / dict_value_1), 
    # (bool_value_1 / set_value_1),
    # (bool_value_1 / list_value_1),
    
    (complex_value_1 / int_value_1), 
    (complex_value_1 / bool_value_1), 
    (complex_value_1 / complex_value_2),
    (complex_value_1 / float_value_1),
    # (complex_value_1 / tuple_value_1), 
    # (complex_value_1 / string_value_1), 
    # (complex_value_1 / dict_value_1), 
    # (complex_value_1 / set_value_1), 
    # (complex_value_1 / list_value_1),
    
    (float_value_1 / int_value_1), 
    (float_value_1 / bool_value_1), 
    (float_value_1 / complex_value_1),
    (float_value_1 / float_value_2),
    # (float_value_1 / tuple_value_1), 
    # (float_value_1 / string_value_1),
    # (float_value_1 / dict_value_1),
    # (float_value_1 / set_value_1),
    # (float_value_1 / list_value_1),
    
    # (tuple_value_1 / int_value_1), 
    # (tuple_value_1 / bool_value_1), 
    # (tuple_value_1 / complex_value_1),
    # (tuple_value_1 / float_value_2),
    # (tuple_value_1 / tuple_value_2), 
    # (tuple_value_1 / string_value_1),
    # (tuple_value_1 / dict_value_1),
    # (tuple_value_1 / set_value_1),
    # (tuple_value_1 / list_value_1),
    
    # (string_value_1 / int_value_1), 
    # (string_value_1 / bool_value_1), 
    # (string_value_1 / complex_value_1),
    # (string_value_1 / float_value_1),
    # (string_value_1 / tuple_value_1), 
    # (string_value_1 / string_value_2),
    # (string_value_1 / dict_value_1),
    # (string_value_1 / set_value_1),
    # (string_value_1 / list_value_1),
    
    # (dict_value_1 / int_value_1), 
    # (dict_value_1 / bool_value_1), 
    # (dict_value_1 / complex_value_1),
    # (dict_value_1 / float_value_1),
    # (dict_value_1 / tuple_value_1), 
    # (dict_value_1 / string_value_1),
    # (dict_value_1 / dict_value_2),
    # (dict_value_1 / set_value_1),
    # (dict_value_1 / list_value_1),

    # (set_value_1 / int_value_1), 
    # (set_value_1 / bool_value_1), 
    # (set_value_1 / complex_value_1),
    # (set_value_1 / float_value_1),
    # (set_value_1 / tuple_value_1), 
    # (set_value_1 / string_value_1),
    # (set_value_1 / dict_value_1),
    # (set_value_1 / set_value_2),
    # (set_value_1 / list_value_1),
    
    # (list_value_1 / int_value_1), 
    # (list_value_1 / bool_value_1), 
    # (list_value_1 / complex_value_1),
    # (list_value_1 / float_value_1),
    # (list_value_1 / tuple_value_1), 
    # (list_value_1 / string_value_1),
    # (list_value_1 / dict_value_1),
    # (list_value_1 / set_value_1),
    # (list_value_1 / list_value_2),
]


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

