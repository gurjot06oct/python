import array

# Define an array with typecode 'i' (signed integers) and an initializer list
my_array = array.array('i', [1, 2, 3, 4, 5])
print(array.array('i', [1, 2, 3, 4, 5]))
# Typecode
print(my_array.typecode) # Output: i

# Accessing elements
print(my_array[0])  # Output: 1

# Slicing
print(my_array[1:3])  # Output: array('i', [2, 3])

# Concatenation
new_array = my_array + array.array('i', [6, 7, 8])
print(new_array)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# Repetition
repeated_array = my_array * 2
print(repeated_array)  # Output: array('i', [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

# Append
my_array.append(6)
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Count
print(my_array.count(6))  # Output: 1

# Extend
my_array.extend([7, 8, 9])
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Index
print(my_array.index(5))  # Output: 4

# Insert
my_array.insert(2, 10)
print(my_array)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6, 7, 8, 9])

# Pop(index=-1)
popped_item = my_array.pop()
print(popped_item)  # Output: 9
print(my_array)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6, 7, 8])

# Remove
my_array.remove(3)
print(my_array)  # Output: array('i', [1, 2, 10, 4, 5, 6, 7, 8])

# Reverse
my_array.reverse()
print(my_array)  # Output: array('i', [8, 7, 6, 5, 4, 10, 2, 1])

# Convert to bytes
bytes_array = my_array.tobytes()
print(bytes_array)  # Output: b'\x08\x00\x00\x00\x07\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x00\x04\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00'


# Use frombytes method to initialize the array from a bytes-like object
bytes_to_my_array = array.array('i')
bytes_to_my_array.frombytes(bytes_array)
print(bytes_to_my_array) # array('i', [8, 7, 6, 5, 4, 10, 2, 1])

# Convert to list
list_array = my_array.tolist()
print(list_array)  # Output: [8, 7, 6, 5, 4, 10, 2, 1]

# Use fromlist method to append items from the list to the array
list_to_my_array = array.array('i')
list_to_my_array.fromlist([1,2,3,4,5,6,7,8])
print(list_to_my_array) # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# Convert to Unicode string
unicode_string_array = array.array('u', 'hello \u2641')
unicode_string = unicode_string_array.tounicode()
print(unicode_string)  # Output: hello ♁

# Buffer info
buffer_info = my_array.buffer_info()
print(buffer_info)  # Output: (140507679273152, 8)

# Byteswap (assuming machine values are 4 bytes)
# Note: This will raise a RuntimeError if tried on current example as all items are 4 bytes
# my_array.byteswap()

# Typecodes
print(array.typecodes)  # Output: 'bBuhHiIlLqQfd'

# Itemsize - ByteSize of one array item
print(my_array.itemsize)  # Output: 4


# inf and nan can also be included
my_array = array.array('d', [1, 2.0, 3.14, float("-inf"), float("nan")])
print(my_array)