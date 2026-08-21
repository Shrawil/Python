# Shape of an Array

# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) # 2 Dim array with 4 elements that'll give (2, 4) <- Tuple

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)