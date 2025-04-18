import numpy as np

# Using numpy.array
zero_d_array = np.array(42)
print(zero_d_array)  # Output: 42
print(zero_d_array.shape)  # Output: ()

# Using numpy.ndarray
zero_d_array = np.ndarray((), dtype=int, buffer=np.array(42))
print(zero_d_array)  # Output: 42
print(zero_d_array.shape)  # Output: ()
