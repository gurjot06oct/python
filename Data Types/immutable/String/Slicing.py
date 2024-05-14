s = "Hello, World!"


my_slice = slice(7, 12) # Start index: 7, End index: 11, Step: 1
substring = s[my_slice]
print(substring,s[7:12]) # Output: World

my_slice = slice(5)  # Start index: 0, End index: 4, Step: 2
substring = s[my_slice]
print(substring,s[:5])  # Output: Hello

my_slice = slice(0, 12, 2)  # Start index: 0, End index: 11, Step: 2
substring = s[my_slice]
print(substring,s[0:12:2])  # Output: Hlo ol


my_slice = slice(-1, len(s),2)  # Start index: -1, End index: 11, Step: 2
substring = s[my_slice]
print(f"{substring}-{s[-1::2]}")  # Output: !-!