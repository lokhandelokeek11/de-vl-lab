import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # This will print the data type of the array

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)  # This will print the data type of the string array


x = arr.copy()
arr[0] = 42
print(arr)
print(x)

x = arr.view()
arr[0] = 42
print(arr)
print(x)
