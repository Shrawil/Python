# Splitting NumPy Arrays

# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr = np.array_split(arr, 3)

print(newarr)
# Split Into Arrays
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Splitting 2-D Arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)