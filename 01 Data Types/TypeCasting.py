# type(): Returns the type of an object
type_of_object = type('hello')



# Integer
int_value = 10

# Boolean
bool_value = True

# Complex
complex_value = 3 + 4j

# Float
float_value = 3.14

# Tuple
tuple_value = (1, 2, 3)

# String
string_value = "Hello"

# Dictionary
dict_value = {'a': 1, 'b': 2}

# Set
set_value = {1, 2, 3}

# List
list_value = [4, 5, 6]

# All combinations of typecasting
typecastings = [
    # Integer to other types
    float(int_value), # 10.0
    bool(int_value), # True
    complex(int_value),  # (10+0j)
    str(int_value), # "10"
    # tuple(int_value),
    # dict(int_value),
    # set(int_value),
    # list(int_value),
    



    # Boolean to other types
    float(bool_value), # 1.0
    int(bool_value), # 1
    complex(bool_value), # 1+0j
    str(bool_value), # True
    # tuple(bool_value),
    # dict(bool_value),
    # set(bool_value),
    # list(bool_value),
    



    # Complex to other types
    # float(complex_value),
    # int(complex_value),
    bool(complex_value),
    str(complex_value),
    # tuple(complex_value),
    # dict(complex_value),
    # set(complex_value),
    # list(complex_value),
    {complex_value},
    [complex_value],
    


    # Float to other types
    bool(float_value),
    int(float_value),
    complex(float_value),
    str(float_value),
    # tuple(float_value),
    # dict(float_value),
    {float_value},
    [float_value],
    



    # Tuple to other types
    bool(tuple_value),
    # No typecasting from tuple to complex as complex(tuple_value) is not defined
    # No typecasting from tuple to float as float(tuple_value) is not defined
    str(tuple_value),
    # dict(tuple_value),
    set(tuple_value),   
    list(tuple_value),
    



    # String to other types
    bool(string_value),
    # No typecasting from string to complex as complex(string_value) is not defined
    # No typecasting from string to float if string is not a valid representation of a float number
    # No typecasting from string to dict as string is not a structured representation of dictionary
    tuple(string_value),
    set(string_value),
    list(string_value),
    


    
    # Dictionary to other types
    bool(dict_value),
    # No typecasting from dict to complex as complex(dict_value) is not defined
    # No typecasting from dict to float as float(dict_value) is not defined
    str(dict_value),
    tuple(dict_value), # keys as element
    set(dict_value),# keys as element
    list(dict_value), # keys as element
    



    # Set to other types
    bool(set_value),
    # No typecasting from set to complex as complex(set_value) is not defined
    # No typecasting from set to float as float(set_value) is not defined
    tuple(set_value),
    # No typecasting from set to dict as set is not a structured representation of dictionary
    list(set_value),
    

    # List to other types
    bool(list_value),
    # No typecasting from list to complex as complex(list_value) is not defined
    # No typecasting from list to float as float(list_value) is not defined
    str(list_value),
    tuple(list_value),
    set(list_value),
    # No typecasting from list to dict as list is not a structured representation of dictionary
]

# Printing the typecastings
for index, result in enumerate(typecastings):
    print(f"Typecasting {index + 1}: {result}")
