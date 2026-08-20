import numpy as np

#               0
arr = np.array([1, 2, 3, 4])
print(arr[0])

#                0          1
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1][0])

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

# Negative Indexing
print(arr[1, -1]) # Last element of 2nd row.