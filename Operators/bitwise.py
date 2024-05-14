import sys
int_value = sys.maxsize

# Bitwise AND
result_and = 5 & 3
print("Bitwise AND:", result_and)

# Bitwise OR
result_or = 5 | 3
print("Bitwise OR:", result_or)

# Bitwise XOR
result_xor = 5 ^ 3
print("Bitwise XOR:", result_xor)

# Bitwise NOT 
# ~x= -(x+1)
result_not = ~5
print("Bitwise NOT:", result_not)

# Bitwise Left Shift 
# x<<n = x*(2^n)
result_left_shift = int_value << 2
print("Bitwise Left Shift:", result_left_shift)
result_left_shift_negative = (-int_value) << 2
print("Bitwise Left Shift Negative:", result_left_shift_negative) 
# result_left_shift_negative == -result_left_shift



# Bitwise Right Shift
# x>>n = x*(2^-n) or remove last n bits
result_right_shift = int_value >> 2
print("Bitwise Right Shift:", result_right_shift)
result_right_shift_negative = (-int_value) >> 2
print("Bitwise Left Shift Negative:", result_right_shift_negative) 
# result_right_shift_negative == -result_right_shift


# Important
# binary of -x is 2's compliment of x

# Example for &
# -2 & -1 = ?
    #  2:  0010
    #  1:  0001
    # -2:  1110
    # -1:  1111
# find -2 & -1 and then 2's compliment the result and add - before it
    # 1110 & 1111 = 1110
    # 2's compliment of 1110 = 0010 = 2
    # therefore answer is -2