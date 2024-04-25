s = "Hello, World!"
print(s[2:5])
my_slice = slice(7, 12)
print(len(s))
substring = s[my_slice]
print(substring)


my_slice = slice(5)  # End index: 5
substring = s[my_slice]
print(substring)  # Output: Hello

my_slice = slice(0, 12, 2)  # Start index: 0, End index: 12, Step: 2
substring = s[my_slice]
print(substring)  # Output: HloWrd