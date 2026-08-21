# Shape of an Array

# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) # 2 Dim array with 4 elements that'll give (2, 4) <- Tuple

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

# Reshaping 
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # 4 rows of 3 element each, so the original array must have 4*3 elements.

print(newarr)