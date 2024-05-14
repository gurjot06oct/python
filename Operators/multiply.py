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
dict_value_1 = {'a': 2, 'b': 3}
dict_value_2 = {'c': 4, 'd': 5}

# Set
set_value_1 = {1, 2}
set_value_2 = {2, 3}

# List
list_value_1 = [1, 2]
list_value_2 = [3, 4]

# All combinations of multiplication operators
combinations = [
    (int_value_1 * int_value_2),
    (int_value_1 * bool_value_1), 
    (int_value_1 * complex_value_1),
    (int_value_1 * float_value_1),
    (int_value_1 * tuple_value_1), 
    (int_value_1 * string_value_1), 
    # (int_value_1 * dict_value_1),
    # (int_value_1 * set_value_1),
    (int_value_1 * list_value_1),
    
    (bool_value_1 * bool_value_2),
    (bool_value_1 * complex_value_1),
    (bool_value_1 * float_value_1), 
    (bool_value_1 * tuple_value_1),
    (bool_value_1 * string_value_1), 
    # (bool_value_1 * dict_value_1), 
    # (bool_value_1 * set_value_1), 
    (bool_value_1 * list_value_1),  

    (complex_value_1 * complex_value_2),
    (complex_value_1 * float_value_1),
    # (complex_value_1 * tuple_value_1), 
    # (complex_value_1 * string_value_1), 
    # (complex_value_1 * dict_value_1),
    # (complex_value_1 * set_value_1), 
    # (complex_value_1 * list_value_1), 
    
    (float_value_1 * float_value_2),
    # (float_value_1 * tuple_value_1),
    # (float_value_1 * string_value_1),
    # (float_value_1 * dict_value_1), 
    # (float_value_1 * set_value_1),
    # (float_value_1 * list_value_1), 
    
    # (tuple_value_1 * tuple_value_2), 
    # (tuple_value_1 * string_value_1),
    # (tuple_value_1 * dict_value_1), 
    # (tuple_value_1 * set_value_1),
    # (tuple_value_1 * list_value_1), 
    
    # (string_value_1 * string_value_2), 
    # (string_value_1 * dict_value_1), 
    # (string_value_1 * set_value_1),
    # (string_value_1 * list_value_1), 
    
    # (dict_value_1 * dict_value_2),
    # (dict_value_1 * set_value_1),
    # (dict_value_1 * list_value_1), 
    
    # (set_value_1 * set_value_2), 
    # (set_value_1 * list_value_1), 
    
    # (list_value_1 * list_value_2)
]

# All combinations of exponentiation operators
combinations = [
    (int_value_1 ** int_value_2),
    (int_value_1 ** float_value_1),
    (int_value_1 ** complex_value_1),

    (float_value_1 ** int_value_1),
    (float_value_1 ** float_value_2),
    (float_value_1 ** complex_value_2),
    
    (complex_value_1 ** int_value_1),
    (complex_value_1 ** float_value_2),
    (complex_value_1 ** complex_value_2),
]

print(2**3**2) # 512 not 64
# @ Matrix Multiplication in numpy or 2d array