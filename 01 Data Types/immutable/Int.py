print(int(3.7),
int('5'),
int(True))


# int(3 + 4j)
# Output: Error



#base Literals
binar,octa,deci,hexa = 0b101010,0o52,42,0x2a
print(binar,octa,deci,hexa)



#base conversions
decimal_num = 10
binary_representation = bin(decimal_num)  # '0b1010'
octal_representation = oct(decimal_num)  # '0o12'
hexadecimal_representation = hex(decimal_num)  # '0xa'