import numpy as np


#Check 
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
<<<<<<< HEAD
print('number of dimensions :', arr.ndim)
=======
print('number of dimensions :', arr.ndim)
>>>>>>> 6800c740d67e961c35c45b89fb33e9c1746a71aa
