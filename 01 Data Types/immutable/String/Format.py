# rawstring - R|r
print(r"abcdefc\bgujoec")

# unicodes - U|u
print("\u03A9")


# formated String F|f, formatted + raw string  fr|Fr|FR|fR, .format() , %

# Integer
integer = 10

# Floating-point
float_number = 3.144

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

# Character
char = "a"

# Literal percent sign
percent = 50

# Output of repr() function
obj = [1, 2, 3]

# Pointer or address
pointer = 0x7FFF3F268830

# Hexadecimal with prefix "0x"
hex_prefix = 255

# Octal with prefix "0o"
oct_prefix = 10


# Using str.format() method
formatted_string_1 = "Integer: {0: d}\nFloat: {1:.2f}\nBinary: {2:08b}\nOctal: {3:o}\nLowercase Hex: {4:x}\nUppercase Hex: {5:X}\nString: {6}\nMinimum Width: {7:5} is Left Aligned by Default\nLeft Aligned: {8:<5}\nCentered: {9:^5}\nRight Aligned: {10:>10}\nCharacter: {11}\nPercent: {12:.2f}%\nRepr: {13!r}\nStr: {14!s}\nPointer: {15:#x}\nHex with Prefix: {16:#x}\nOctal with Prefix: {17:#o}".format(
    integer,
    float_number,
    binary_number,
    octal_number,
    hex_lower,
    hex_upper,
    string,
    string,
    string,
    string,
    string,
    char,
    percent,
    obj,
    obj,
    pointer,
    hex_prefix,
    oct_prefix,
)

# Using f-strings
formatted_string_2 = f"Integer: {integer}\nFloat: {float_number:.2f}\nBinary: {binary_number:08b}\nOctal: {octal_number:o}\nLowercase Hex: {hex_lower:x}\nUppercase Hex: {hex_upper:X}\nString: {string}\nMinimum Width: {string:>5}\nLeft Aligned: {string:<5}\nCentered: {string:^5}\nRight Aligned: {string:>10}\nCharacter: {char}\nPercent: {percent:.2f}%\nRepr: {obj!r}\Str: {obj!s}\nPointer: {pointer:#x}\nHex with Prefix: {hex_prefix:#x}\nOctal with Prefix: {oct_prefix:#o}"

# Using % method
formatted_string_3 = (
    "Integer: %d\nFloat: %.2f\nOctal: %o\nLowercase Hex: %x\nUppercase Hex: %X\nString: %s\nMinimum Width: %5s\nLeft Aligned: %-5s\nCharacter: %c\nPercent: %.2f%%\nRepr: %r\nPointer: %e\nHex with Prefix: %#x\nOctal with Prefix: %#o"
    % (
        integer,
        float_number,
        octal_number,
        hex_lower,
        hex_upper,
        string,
        string,
        string,
        char,
        percent,
        obj,
        pointer,
        hex_prefix,
        oct_prefix,
    )
)

print("Using str.format() method:", formatted_string_1,sep="\n")
print("\nUsing f-strings:", formatted_string_2,sep="\n")
print("\nUsing % method:", formatted_string_3,sep="\n")


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


person = Person("Alice", 30)
formatted_string = "Using str.format() method: {!s}, {!r}".format(person, person)
print(formatted_string)

formatted_string = f"Using f-strings: {person!s}, {person!r}"
print(formatted_string)