# < , <= , >= same as <

# Integer vs Integer
result_ii = 5 < 10

# Integer vs Float
result_if = 5 < 3.14

# Integer vs Complex ( not supported )
# result_ic = 5 < 3 + 4j

# Integer vs String  ( not supported )
# result_is = 5 < "10"

# Float vs Float
result_ff = 3.14 < 2.71

# Float vs Complex ( not supported )
# result_fc = 3.14 < 2 + 3j

# Float vs String ( not supported )
# result_fs = 3.14 < "2.71"

# Complex vs Complex ( not supported )
# result_cc = 2 + 3j < 4 + 5j

# Complex vs String ( not supported )
# result_cs = 2 + 3j < "4+5j"

# String vs String (Lexicographic comparison)
result_ss = "apple" < "banana"

# Boolean vs Boolean
result_bb = True < False

# Boolean vs Integer
result_bi = True < 0

# Boolean vs Float
result_bf = False < 1.0

# Boolean vs Complex ( not supported )
# result_bc = True < 2 + 3j

# Boolean vs String ( not supported )
# result_bs = False < "True"

# None vs None  ( not supported )
# result_nn = None < None

# Integer vs None ( not supported )
# result_in = 10 < None

# Float vs None
# result_fn = 3.14 < None

# Complex vs None ( not supported )
# result_cn = 2 + 3j < None

# String vs None  ( not supported )
# result_sn = "Hello" < None

# List vs List (Lexicographic comparison)
result_ll = [1, 2, 3] < [1, 2, 4]

# Tuple vs Tuple (Lexicographic comparison)
result_tt = (1, 2, 3) < (1, 2, 4)

# Dictionary vs Dictionary ( not supported )
# result_dd = {"a": 1, "b": 2} < {"a": 1, "b": 3}

# Range vs Range ( not supported )
# result_rr = range(5) < range(1, 6)

# Bytes vs Bytes (Lexicographic comparison)
result_bb = b"apple" < b"banana"

# Bytearray vs Bytearray (Lexicographic comparison)
result_bab = bytearray(b"apple") < bytearray(b"banana")

# Memoryview vs Memoryview ( not supported )
# result_mm = memoryview(b"apple") < memoryview(b"banana")


# Ellipsis vs Ellipsis ( not supported )
# result_ee = Ellipsis < Ellipsis

# NotImplemented vs NotImplemented ( not supported )
# result_nn = NotImplemented < NotImplemented

# Function vs Function ( not supported )
# def func_a(): pass
# def func_b(): pass
# result_func = func_a < func_b

# Lambda vs Lambda ( not supported )
# lambda_a = lambda x: x
# lambda_b = lambda x: x
# result_lambda = lambda_a < lambda_b

# Generator vs Generator ( not supported )
# gen_a = (i for i in range(5))
# gen_b = (i for i in range(5))
# result_gen = gen_a < gen_b


