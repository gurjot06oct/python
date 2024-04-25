# A
# abs(): Returns the absolute value of a number
absolute_value = abs(-10)

# aiter(): Returns an Asynchronous iterator object
# go to extra folder

# all(): Returns True if all elements of an iterable are true
all_true = all([True, True, True])

# anext(): Advances the iterator to the next element and returns it
iter_obj = iter([1, 2, 3])
next_element = next(iter_obj)

# any(): Returns True if any element of an iterable is true
any_true = any([True, False, False])

# ascii(): Returns a string containing a printable representation of an object
ascii_repr = ascii('hello')

# B
# bin(): Converts an integer to a binary string
binary_string = bin(10)

# bool(): Converts a value to a Boolean
bool_value = bool(1)

# breakpoint(): Invokes the Python debugger
# breakpoint()

# bytearray(): Returns a new array of bytes
byte_array = bytearray([65, 66, 67])

# bytes(): Returns a new immutable bytes object
bytes_obj = bytes('12323432', 'utf-8')

# C
# callable(): Returns True if the object appears callable
is_callable = callable(print)

# chr(): Returns a character (a string) from an integer
char_from_int = chr(65)

# classmethod(): Returns a class method for the given function
class_method = classmethod(lambda cls: print(cls))

# compile(): Compiles the source into a code or AST object
compiled_code = compile('print("Hello, World!")', '', 'exec')

# complex(): Returns a complex number
complex_number = complex(1, 2)

# D
# delattr(): Deletes the attribute of an object
class MyClass:
    x = 10

delattr(MyClass, 'x')

# dict(): Returns a new dictionary
dictionary = dict(a=1, b=2)

# dir(): Returns a list of valid attributes for an object
attributes = dir(dict())

# divmod(): Returns the quotient and the remainder when dividing two numbers
quotient_remainder = divmod(10, 3)

# E
# enumerate (iterable,start): Returns an enumerate object
enumerated = enumerate(['a', 'b', 'c'],start=1)
for i,value in enumerated:
    pass

# eval(): Evaluates a Python expression
evaluated = eval('2 + 2')

# exec(): Executes Python code
executed = exec('print("Hello, World!")')

# F
# filter(): Constructs an iterator from elements of an iterable for which a function returns true
filtered = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])

# float(): Returns a floating-point number
floating_point = float(3)

# format(): Formats a specified value
formatted = format(123.456, '.2f')

# frozenset(): Returns a new frozenset object
frozen_set = frozenset([1, 2, 3])

# G
# getattr(): Returns the value of the named attribute of an object
value = getattr(MyClass(), 'x', 'default_value')
print(value)

# globals(): Returns the current global symbol table as a dictionary
global_symbols = globals()

# H
# hasattr(): Returns True if an object has the given attribute
has_attribute = hasattr(MyClass(), 'x')

# hash(): Returns the hash value of an object
hashed_value = hash('hello')
# hash value remains constant till the current session of program but changes for another program


# help(): Invokes the built-in help system
# help()

# hex(): Converts an integer to a hexadecimal string
hex_string = hex(255)

# I
# id(): Returns the identity of an object
identity = id('hello')

# input(): Reads a line from input
# user_input = input("Enter something: ")

# int(): Returns an integer object
integer_value = int('10')

# isinstance(): Returns True if an object is an instance of a class
is_instance = isinstance(10, int)

# issubclass(): Returns True if a class is a subclass of another class
is_subclass = issubclass(int, object)

# iter(): Returns an iterator object
iterable = iter([1, 2, 3])
for item in iterable:
    pass

# L
# len(): Returns the length of an object
length = len([1, 2, 3])

# list(): Returns a list
list_from_iterable = list(range(5))

# locals(): Returns the current local symbol table as a dictionary
local_symbols = locals()

# M
# map(): Applies a function to all the items in an input iterable
mapped = map(lambda x: x * 2, [1, 2, 3])

# max(): Returns the largest item in an iterable
maximum = max([1, 2, 3],key=lambda x:x)

# memoryview(): Returns a memory view object
memory_view = memoryview(b'abc')

# min(): Returns the smallest item in an iterable
minimum = min([1, 2, 3])

# N
# next(): Returns the next item from an iterator
next_item = next(iterable)

# O
# object(): Returns a new featureless object
new_object = object()

# oct(): Converts an integer to an octal string
octal_string = oct(8)

# open(): Opens a file and returns a file object
# file_object = open('example.txt', 'r')

# ord(): Returns the Unicode code point for a character
unicode_code_point = ord('A')

# P
# pow(): Returns the value of x to the power of y
power = pow(2, 3)

# print(): Prints objects to the text stream
print('Hello, World!')

# property(): Returns a property attribute
class MyClass:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)

# R
# range(): Returns a sequence of numbers
number_sequence = range(5)

# repr(): Returns a printable representation of an object
representation = repr([1, 2, 3])

# reversed(): Returns a reverse iterator
reversed_iter = reversed([1, 2, 3])

# round(): Rounds a number to a specified precision
rounded_number = round(3.14159, 2)

# S
# set(): Returns a new set object
set_object = set([1, 2, 3])

# setattr(): Sets the value of the attribute of an object
setattr(MyClass(5), 'x', 10)

# slice(): Returns a slice object
slice_obj = slice(1, 5, 2)

# sorted(): Returns a sorted list
sorted_list = sorted([3, 1, 2])

# staticmethod(): Returns a static method for the given function
static_method = staticmethod(lambda x: print(x))

# str(): Returns a string
string_value = str(123)

# sum(): Returns the sum of all elements in an iterable
summation = sum([1, 2, 3])

# super(): Returns a proxy object that delegates method calls to a parent or sibling class
class SubClass(MyClass):
    def __init__(self, x):
        super().__init__(x)

# T
# tuple(): Returns a tuple
tuple_from_list = tuple([1, 2, 3])

# type(): Returns the type of an object
type_of_object = type('hello')

# V
# vars(): Returns the __dict__ attribute of an object
class MyClass:
    x = 10

variables = vars(MyClass())

# Z
# zip(): Returns an iterator of tuples
zipped = zip([1, 2, 3], ['a', 'b', 'c'])

# Printing the results
print("A")
print("abs():", absolute_value)
print("aiter():", iter_obj)
print("all():", all_true)
print("anext():", next_element)
print("any():", any_true)
print("ascii():", ascii_repr)
print("B")
print("bin():", binary_string)
print("bool():", bool_value)
# print("breakpoint():")  # Uncomment to invoke the debugger
print("bytearray():", byte_array)
print("bytes():", bytes_obj)
print("C")
print("callable():", is_callable)
print("chr():", char_from_int)
print("classmethod():", class_method)
print("compile():", compiled_code)
print("complex():", complex_number)
print("D")
# print("delattr():")  # Uncomment to delete the attribute
print("dict():", dictionary)
print("dir():", attributes)
print("divmod():", quotient_remainder)
print("E")
print("enumerate():", list(enumerated))
print("eval():", evaluated)
print("exec():", executed)
print("F")
print("filter():", list(filtered))
print("float():", floating_point)
print("format():", formatted)
print("frozenset():", frozen_set)
print("G")
print("getattr():", value)
print("globals():", global_symbols)
print("H")
print("hasattr():", has_attribute)
print("hash():", hashed_value)
# print("help():")  # Uncomment to invoke the help system
print("hex():", hex_string)
print("I")
print("id():", identity)
# print("input():", user_input)
print("int():", integer_value)
print("isinstance():", is_instance)
print("issubclass():", is_subclass)
print("iter():", iterable)
print("L")
print("len():", length)
print("list():", list_from_iterable)
print("locals():", local_symbols)
print("M")
print("map():", list(mapped))
print("max():", maximum)
print("memoryview():", memory_view)
print("min():", minimum)
print("N")
print("next():", next_item)
print("O")
print("object():", new_object)
print("oct():", octal_string)
# print("open():", file_object)
print("ord():", unicode_code_point)
print("P")
print("pow():", power)
print("print():", "Printed")
print("property():", "Property created")
print("R")
print("range():", list(number_sequence))
print("repr():", representation)
print("reversed():", list(reversed_iter))
print("round():", rounded_number)
print("S")
print("set():", set_object)
print("setattr():", "Attribute set")
print("slice():", slice_obj)
print("sorted():", sorted_list)
print("staticmethod():", static_method)
print("str():", string_value)
print("sum():", summation)
print("super():", "Proxy object created")
print("T")
print("tuple():", tuple_from_list)
print("type():", type_of_object)
print("V")
print("vars():", variables)
print("Z")
print("zip():", list(zipped))
