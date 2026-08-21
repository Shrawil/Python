# Iterating Arrays

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

arr = np.array([[1,2,3],[4,5,6]])

for x in arr:
    for y in x:
        print(y, end=" ")
    print()

# Iterating Arrays Using nditer()

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, 
# that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#              Every row, Every element at 2nd step. (1, 3, 5, 7)
for x in np.nditer(arr[:, ::2]):
    print(x)

# Enumerator
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)