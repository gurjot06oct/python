import numpy as np

arr1 = np.array([1, 2, 3])   
arr2 = np.array(arr1)                
arr3 = np.asarray(arr1)  # aliasing of arr1    
arr1[1]=5
print(arr1,arr2,arr3)
# [1 5 3] [1 2 3] [1 5 3]