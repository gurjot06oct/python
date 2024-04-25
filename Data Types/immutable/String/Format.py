# rawstring - R|r
print(r"abcdefc\bgujoec")

# unicodes - U|u
print(u"\u03A9")


# formated String F|f, formatted + raw string  fr|Fr|FR|fR, .format() , %   

# Integer
integer = 10

# Floating-point
float_number = 3.14159

# Binary
binary_number = 10

# Octal
octal_number = 10

# Lowercase hexadecimal
hex_lower = 255

# Uppercase hexadecimal
hex_upper = 255

# String
string = "hello"

# Minimum width
string_min_width = "hi"

# Left-aligned
string_left_aligned = "hi"

# Centered
string_centered = "hi"

# Right-aligned
string_right_aligned = "hello"

# Character
char = 'a'

# Literal percent sign
percent = 50

# Output of repr() function
obj = [1, 2, 3]

# Pointer or address
pointer = 0x7fff3f268830

# Hexadecimal with prefix "0x"
hex_prefix = 255

# Octal with prefix "0o"
oct_prefix = 10

# Using str.format() method
formatted_string_1 = "Integer: {0}\nFloat: {1:.2f}\nBinary: {2:08b}\nOctal: {3:o}\nLowercase Hex: {4:x}\nUppercase Hex: {5:X}\nString: {6}\nMinimum Width: {7:>5}\nLeft Aligned: {8:<5}\nCentered: {9:^5}\nRight Aligned: {10:>10}\nCharacter: {11}\nPercent: {12:.2f}%\nRepr: {13!r}\nStr: {14!s}\nPointer: {15:#x}\nHex with Prefix: {16:#x}\nOctal with Prefix: {17:#o}".format(
    integer, float_number, binary_number, octal_number, hex_lower, hex_upper, string, string_min_width, string_left_aligned, string_centered, string_right_aligned, char, percent, obj,obj, pointer, hex_prefix, oct_prefix)

# Using f-strings
formatted_string_2 = f"Integer: {integer}\nFloat: {float_number:.2f}\nBinary: {binary_number:08b}\nOctal: {octal_number:o}\nLowercase Hex: {hex_lower:x}\nUppercase Hex: {hex_upper:X}\nString: {string}\nMinimum Width: {string_min_width:>5}\nLeft Aligned: {string_left_aligned:<5}\nCentered: {string_centered:^5}\nRight Aligned: {string_right_aligned:>10}\nCharacter: {char}\nPercent: {percent:.2f}%\nRepr: {obj!r}\Str: {obj!s}\nPointer: {pointer:#x}\nHex with Prefix: {hex_prefix:#x}\nOctal with Prefix: {oct_prefix:#o}"

# Using % method
formatted_string_3 = "Integer: %d\nFloat: %.2f\nOctal: %o\nLowercase Hex: %x\nUppercase Hex: %X\nString: %s\nMinimum Width: %5s\nLeft Aligned: %-5s\nCharacter: %c\nPercent: %.2f%%\nRepr: %r\nPointer: %e\nHex with Prefix: %#x\nOctal with Prefix: %#o" % (integer, float_number, octal_number, hex_lower, hex_upper, string, string_min_width, string_left_aligned, char, percent, obj, pointer, hex_prefix, oct_prefix)

print("Using str.format() method:\n", formatted_string_1)
print("\nUsing f-strings:\n", formatted_string_2)
print("\nUsing % method:\n", formatted_string_3)





# {width}.{precision} for Floats
# Positive width and precision
print("%10.2f" % 3.14159)  # Output: "      3.14"
# Negative width and positive precision
print("%-10.2f" % 3.14159)  # Output: "3.14      "





# What is !r and !s format?
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Create an instance of the Person class
person = Person("Alice", 30)

# Using str.format() method
formatted_string = "Using str.format() method: {!s}, {!r}".format(person, person)
print(formatted_string)

# Using f-strings
formatted_string = f"Using f-strings: {person!s}, {person!r}"
print(formatted_string)

