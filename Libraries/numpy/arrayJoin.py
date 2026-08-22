import numpy as np

# 1D Array
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

# 2D Array
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[11,12,13,14],[15,16,17,18]])
arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)
