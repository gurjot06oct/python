import numpy as np


# Create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]])


# Shape of the array
print("Shape of the array:")
print(arr.shape)  # Output: (2, 3)


# Dimension of the array
print("\nDimension of the array:")
print(arr.ndim)   # Output: 2


# Data type of the array
print("\nData type of the array:")
print(arr.dtype)  # Output: int64


# Total number of elements in the array
print("\nTotal number of elements in the array:")
print(arr.size)   # Output: 6


# Reshape the array
print("\nReshaped array:")
print(arr.reshape(3, 2))  # Output: [[1 2], [3 4], [5 6]]


# Transpose of the array
print("\nTransposed array:")
print(arr.T)  # Output: [[1 4], [2 5], [3 6]]


# Sum of all elements in the array
print("\nSum of all elements in the array:")
print(arr.sum())  # Output: 21


# Mean of all elements in the array
print("\nMean of all elements in the array:")
print(arr.mean())  # Output: 3.5


# Maximum element in the array
print("\nMaximum element in the array:")
print(arr.max())  # Output: 6


# Minimum element in the array
print("\nMinimum element in the array:")
print(arr.min())  # Output: 1
