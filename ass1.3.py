import numpy as np
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# 1. Addition
addition = matrix_a + matrix_b
print("Addition:\n", addition)

print()

# 2. Substraction
substraction = matrix_a - matrix_b
print("Substraction:\n", substraction)

print()

# 3. Multiplication
multiplication = matrix_a * matrix_b
print("Multiplication:\n", multiplication)

# 3.1 Multiplication using Dot
dot_multiplication = np.dot(matrix_a, matrix_b)  
print("Matrix Multiplication (Dot Product):\n", dot_multiplication)

# 3.2 Multiplication using Multiply() function
mul_function = np.multiply(matrix_a,matrix_b)
    
print()

# 4. Division
division = matrix_a / matrix_b  
print("Element-wise Division:\n", division)

print()

# 5. Flattening
flattened = matrix_a.flatten()
print("Flattened Matrix A:\n", flattened)

# 6. Reshaping 
reshaped = matrix_a.reshape(1,9)
print("Reshaped Matrix:\n",)

# 7. Concatenation - along rows
concatenated = np.concatenate((matrix_a, matrix_b), axis = 0)
print("Concatenated Matrix (along rows):\n", concatenated)

# 7.1 Concatenation - along columns 
concatenated = np.concatenate((matrix_a, matrix_b), axis = 1)
print("Concatenated Matrix (along rows):\n", concatenated)

print()

# 8. Transpose
transpose_a = matrix_a.T
print("Transpose of Matrix A:\n", transpose_a)


