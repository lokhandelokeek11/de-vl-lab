#Accessing 1-D array elements
# 1. Basics
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2])

#2. Get third and fourth elements from the following array and add them.

arr = np.array([4,56,65,12,5])
print(arr[2] + arr[4])

#Accessing 2-D array elements
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('4th element on 1st row: ', arr[0,3])
print('5th element on 2st row: ', arr[1,4])

#Accessing 3-D array elements

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('Access the third element of the second array of the first array:', arr[0, 1, 2])

# Example explained 
'''arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6'''


# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])