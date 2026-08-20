import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# arr[start:stop:step]
# Default start = 0
# Default stop = len(arr) - 1    
# Default step = +1

print(arr[1:5]) # Start from index 1 to index 5
print(arr[5:]) # Every element from and after 5th index
print(arr[:5]) # Every element before 5th index