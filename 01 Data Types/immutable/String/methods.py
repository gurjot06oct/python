# String methods in Python with explanations

# capitalize(): Converts the first character to uppercase
example_string = "hello world"
capitalized_string = example_string.capitalize()
print(example_string,"capitalize():", capitalized_string)  # Output: Hello world




# casefold(): Converts the string into lowercase
example_string = "hello World"
lowercased_string = example_string.casefold()
print("casefold():", lowercased_string)  # Output: hello world





# center(width[, fillchar]): Returns a centered string of specified width
example_string = "hello"
centered_string = example_string.center(10, '-')
print("center():", centered_string)  # Output: --hello---




# count(sub[, start[, end]]): Returns the number of occurrences of a specified substring
example_string = "hello world"
count_occurrences = example_string.count('o')
print("count():", count_occurrences)  # Output: 2
print(example_string.count('o',1,4))  # 0




# encode(encoding='utf-8', errors='strict'): Returns an encoded version of the string
example_string = "hello world"
encoded_string = example_string.encode('utf-8')
print("encode():", encoded_string)  # Output: b'hello world'




# endswith(suffix[, start[, end]]): Returns true if the string ends with the specified value
example_string = "hello world"
ends_with = example_string.endswith("world")
print("endswith():", ends_with)  # Output: True




# expandtabs(tabsize=8): Sets the tab size of the string
example_string = "hello\tworld"
expanded_string = example_string.expandtabs(4)
print("expandtabs():", expanded_string)  # Output: hello   world




# find(sub[, start[, end]]): Searches the string for a specified value and returns the position of where it was found
example_string = "hello world"
position = example_string.find("world")
print("find():", position)  # Output: 6





# format(*args, **kwargs): Formats specified values in a string
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("format():", formatted_string)  # Output: My name is Alice and I am 30 years old.





# format_map(mapping): Formats specified values in a string
person = {'name': 'Alice', 'age': 30}
template = 'My name is {name} and I am {age} years old.'
result = template.format_map(person)
print("format_map():", result)  # Output: My name is Alice and I am 30 years old.





# index(sub[, start[, end]]): Searches the string for a specified value and returns the position of where it was found
example_string = "hello world"
position = example_string.index("world")
print("index():", position)  # Output: 6





# isalnum(): Returns True if all characters in the string are alphanumeric
example_string = "hello123"
is_alphanumeric = example_string.isalnum()
print("isalnum():", is_alphanumeric)  # Output: True





# isalpha(): Returns True if all characters in the string are in the alphabet , empty string returns False
example_string = "hsdf"
is_alpha = example_string.isalpha()
print("isalpha():", is_alpha)  # Output: True





# isascii(): Returns True if all characters in the string are ASCII characters
example_string = "hello"
is_ascii = example_string.isascii()
print("isascii():", is_ascii)  # Output: True





# isdecimal(): Returns True if all characters in the string are decimals
example_string = "123"
is_decimal = example_string.isdecimal()
print("isdecimal():", is_decimal)  # Output: True





# isdigit(): Returns True if all characters in the string are digits
example_string = "123"
is_digit = example_string.isdigit()
print("isdigit():", is_digit)  # Output: True




# isidentifier(): Returns True if the string is an identifier
example_string = "hello"
is_identifier = example_string.isidentifier()
print("isidentifier():", is_identifier)  # Output: True




# islower(): Returns True if all characters in the string are lowercase
example_string = "hello"
is_lower = example_string.islower()
print("islower():", is_lower)  # Output: True




# isnumeric(): Returns True if all characters in the string are numeric
example_string = "123"
is_numeric = example_string.isnumeric()
print("isnumeric():", is_numeric)  # Output: True





# isprintable(): Returns True if all characters in the string are printable
example_string = "hello\nworld"
is_printable = example_string.isprintable()
print("isprintable():", is_printable)  # Output: False





# isspace(): Returns True if all characters in the string are whitespaces
example_string = "   "
is_space = example_string.isspace()
print("isspace():", is_space)  # Output: True





# istitle(): Returns True if the string follows the rules of a title
example_string = "Hello World"
is_title = example_string.istitle()
print("istitle():", is_title)  # Output: True





# isupper(): Returns True if all characters in the string are uppercase
example_string = "HELLO"
is_upper = example_string.isupper()
print("isupper():", is_upper)  # Output: True





# join(iterable): Joins the elements of an iterable to the end of the string
separator = "-"
words = ["hello", "world"]
joined_string = separator.join(words)
print("join():", joined_string)  # Output: hello-world





# ljust(width[, fillchar]): Returns a left-justified version of the string
example_string = "hello"
left_justified_string = example_string.ljust(10, '-')
print("ljust():", left_justified_string)  # Output: hello-----





# lower(): Converts a string into lowercase
example_string = "Hello World"
lowercased_string = example_string.lower()
print("lower():", lowercased_string)  # Output: hello world





# lstrip([chars]): Returns a left trim version of the string
example_string = "   hello   "
trimmed_string = example_string.lstrip()
print("lstrip():", trimmed_string)  # Output: hello   





# maketrans(x[, y[, z]]): Returns a translation table to be used in translations
translation_table = str.maketrans("aeiou", "12345")
example_string = "hello world"
translated_string = example_string.translate(translation_table)
print("translate():", translated_string)  # Output: h2ll4 w4rld






# partition(sep): Returns a tuple where the string is parted into three parts
example_string = "hello world"
partitioned_string = example_string.partition(" ")
print("partition():", partitioned_string)  # Output: ('hello', ' ', 'world')





# replace(old, new[, count]): Returns a string where a specified value is replaced with a specified value
example_string = "hello world"
replaced_string = example_string.replace("world", "universe")
print("replace():", replaced_string)  # Output: hello universe




# rfind(sub[, start[, end]]): Searches the string for a specified value and returns the last position of where it was found
example_string = "hello world"
position = example_string.rfind("l")
print("rfind():", position)  # Output: 9





# rindex(sub[, start[, end]]): Searches the string for a specified value and returns the last position of where it was found
example_string = "hello world"
position = example_string.rindex("l")
print("rindex():", position)  # Output: 9





# rjust(width[, fillchar]): Returns a right justified version of the string
example_string = "hello"
right_justified_string = example_string.rjust(10, '-')
print("rjust():", right_justified_string)  # Output: -----hello





# rpartition(sep): Returns a tuple where the string is parted into three parts
example_string = "hello world"
partitioned_string = example_string.rpartition(" ")
print("rpartition():", partitioned_string)  # Output: ('hello', ' ', 'world')





# rsplit(sep=None, maxsplit=-1): Splits the string at the specified separator, and returns a list
example_string = "hello world"
split_string = example_string.rsplit(" ")
print("rsplit():", split_string)  # Output: ['hello', 'world']





# rstrip([chars]): Returns a right trim version of the string
example_string = "   hello   "
trimmed_string = example_string.rstrip()
print("rstrip():", trimmed_string)  # Output:    hello




# split(sep=None, maxsplit=-1): Splits the string at the specified separator, and returns a list
example_string = "hello world"
split_string = example_string.split(" ")
print("split():", split_string)  # Output: ['hello', 'world']




# splitlines([keepends]): Splits the string at line breaks and returns a list
example_string = "hello\nworld"
split_lines = example_string.splitlines()
print("splitlines():", split_lines)  # Output: ['hello', 'world']




# startswith(prefix[, start[, end]]): Returns true if the string starts with the specified value
example_string = "hello world"
starts_with = example_string.startswith("hello")
print("startswith():", starts_with)  # Output: True




# strip([chars]): Returns a trimmed version of the string
example_string = "   hello   "
trimmed_string = example_string.strip()
print("strip():", trimmed_string)  # Output: hello




# swapcase(): Swaps cases, lower case becomes upper case and vice versa
example_string = "Hello World"
swapped_case_string = example_string.swapcase()
print("swapcase():", swapped_case_string)  # Output: hELLO wORLD




# title(): Converts the first character of each word to uppercase
example_string = "hello world"
title_case_string = example_string.title()
print("title():", title_case_string)  # Output: Hello World




# translate(table): Returns a translated string
translation_table = str.maketrans("aeiou", "12345")
example_string = "hello world"
translated_string = example_string.translate(translation_table)
print("translate():", translated_string)  # Output: h2ll4 w4rld





# upper(): Converts a string into uppercase
example_string = "hello world"
uppercased_string = example_string.upper()
print("upper():", uppercased_string)  # Output: HELLO WORLD




# zfill(width): Fills the string with a specified number of 0 values at the beginning
example_string = "42"
zero_padded_string = example_string.zfill(5)
print("zfill():", zero_padded_string)  # Output: 00042
