# ==, !=

# Integer vs Integer
result_ii = 5 == 5.0

# Integer vs Float
result_if = 5 == 3.14

# Integer vs Complex 
result_ic = 5 == 3 + 4j

# Integer vs String
result_is = 5 == "10"

# Float vs Float
result_ff = 3.14 == 2.71

# Float vs Complex
result_fc = 3.14 == 2 + 3j

# Float vs String
result_fs = 3.14 == "2.71"

# Complex vs Complex
result_cc = 2 + 3j == 4 + 5j

# Complex vs String
result_cs = 2 + 3j == "4+5j"

# String vs String (Lexicographic comparison)
result_ss = "apple" == "banana"

# Boolean vs Boolean
result_bb = True == False

# Boolean vs Integer
result_bi = True == 0

# Boolean vs Float
result_bf = False == 1.0

# Boolean vs Complex
result_bc = True == 2 + 3j

# Boolean vs String
result_bs = False == "True"

# None vs None
result_nn = None == None  # True

# Integer vs None
result_in = 10 == None

# Float vs None
result_fn = 3.14 == None

# Complex vs None
result_cn = 2 + 3j == None

# String vs None
result_sn = "Hello" == None

# List vs List (Lexicographic comparison)
result_ll = [1, 2, 3] == [1, 2, 4]

# Tuple vs Tuple (Lexicographic comparison)
result_tt = (1, 2, 3) < (1, 2, 4)

# Dictionary vs Dictionary 
result_dd = {"a": 1, "b": 2} ==  {"a": 1, "b": 2}

# Range vs Range
result_rr = range(5) == range(1, 6)

# Bytes vs Bytes (Lexicographic comparison)
result_bb = b"apple" == b"banana"

# Bytearray vs Bytearray (Lexicographic comparison)
result_bab = bytearray(b"apple") == bytearray(b"banana")

# Memoryview vs Memoryview
result_mm = memoryview(b"apple") == memoryview(b"banana")

# Ellipsis vs Ellipsis
result_ee = Ellipsis == Ellipsis

# NotImplemented vs NotImplemented
result_nin = NotImplemented == NotImplemented

# Function vs Function
def func_a(): pass
def func_b(): pass
result_func = func_a == func_b

# Lambda vs Lambda 
lambda_a = lambda x: x
lambda_b = lambda x: x
result_lambda = lambda_a == lambda_b

# Generator vs Generator
gen_a = (i for i in range(5))
gen_b = (i for i in range(5))
result_gen = gen_a == gen_b

print(result_ii)       # True
print(result_if)       # False
print(result_ic)       # False
print(result_is)       # False
print(result_ff)       # False
print(result_fc)       # False
print(result_fs)       # False
print(result_cc)       # False
print(result_cs)       # False
print(result_ss)       # False
print(result_bb)       # False
print(result_bi)       # False
print(result_bf)       # False
print(result_bc)       # False
print(result_bs)       # False
print(result_nn)       # True
print(result_in)       # False
print(result_fn)       # False
print(result_cn)       # False
print(result_sn)       # False
print(result_ll)       # False
print(result_tt)       # True
print(result_dd)       # True
print(result_rr)       # False
print(result_bb)       # False
print(result_bab)      # False
print(result_mm)       # False
print(result_ee)       # True
print(result_nin)      # True
print(result_func)     # False
print(result_lambda)   # False
print(result_gen)      # False
