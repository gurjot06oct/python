my_float = 3.14
scientific_float = 6.022e23  # Avogadro's number (6.022 x 10^23)
num_str = "3.14"
my_float = float(num_str)  # Convert string to float

# Due to floating-point precision, result may not be exactly 0.3
print(0.1 + 0.2)
x = 0.1 + 0.2
y = 0.3
print(x == y) # False

pos_inf = float('inf')
neg_inf = float('-inf')
nan = float('nan')
print(pos_inf,neg_inf,nan)

rounded_num = round(3.14159, 2)  # Rounds to 2 decimal places: 3.14
print(rounded_num) # 3.14
print(round(2343.14159, -2)) # 2300.0