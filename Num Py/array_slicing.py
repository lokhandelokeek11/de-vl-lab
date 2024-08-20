#Slicing arrays 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])  #[start:end]. [start:end:step]
print(arr[1:5])

# Slice elements from index 4 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])