import numpy as np

# Convert various inputs into NumPy arrays
arr1 = np.asarray([1, 2, 3])                  # Convert list to array
arr2 = np.asarray((4, 5, 6))                  # Convert tuple to array
arr3 = np.asarray([[1, 2, 3], [4, 5, 6]])     # Convert list of lists to array
arr4 = np.asarray([1, 2, 3],dtype=np.float64)  # Specify dtype
existing_array = np.array([7, 8, 9])
arr5 = np.asarray(existing_array)            # Aliased array of existing_array
arr6 = np.array(existing_array) 
existing_array[0]=10

# Print the results
print("Array from list:", arr1)
print("Array from tuple:", arr2)
print("Array from list of lists:", arr3)
print("Array with specified dtype:", arr4)
print("Array with existing_array:", existing_array)
print("Array from arr5:", arr5)
print("Array from arr6:", arr6)
