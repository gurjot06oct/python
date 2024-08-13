import numpy as np

typecodes = {
    'b': 'boolean',
    'i': 'signed integer',
    'u': 'unsigned integer',
    'f': 'floating point',
    'c': 'complex floating point',
    'm': 'timedelta',
    'M': 'datetime',
    'O': 'object',
    'S': 'string',
    'a': 'string',
    'U': 'unicode string',
    'V': 'raw data (void)'
}

print("Typecodes and Corresponding Data Types in NumPy:")
for code, dtype_name in typecodes.items():
    print(f"{code}: {dtype_name}")
