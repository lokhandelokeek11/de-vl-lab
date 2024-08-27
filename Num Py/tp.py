import numpy as np

# Define two 3x3 matrices
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# 1. Addition
addition = matrix_a + matrix_b
print("Addition:\n", addition)

# 2. Subtraction
subtraction = matrix_a - matrix_b
print("Subtraction:\n", subtraction)

# 3. Multiplication
multiplication = matrix_a * matrix_b  # Element-wise multiplication
print("Element-wise Multiplication:\n", multiplication)

# 4. Division
division = matrix_a / matrix_b  # Element-wise division
print("Element-wise Division:\n", division)

# 5. Flattening
flattened = matrix_a.flatten()
print("Flattened Matrix A:\n", flattened)

# 6. Reshaping (reshaping to 1x9)
reshaped = matrix_a.reshape(1, 9)
print("Reshaped Matrix A (1x9):\n", reshaped)

# 7. Transpose
transpose_a = matrix_a.T
print("Transpose of Matrix A:\n", transpose_a)

# 8. Diagonal Matrix
diagonal_matrix = np.diag(np.diag(matrix_a))  # Extracting diagonal
print("Diagonal Matrix from Matrix A:\n", diagonal_matrix)

# 9. Concatenation (along rows)
concatenated = np.concatenate((matrix_a, matrix_b), axis=0)
print("Concatenated Matrix (along rows):\n", concatenated)

# 10. Inverse (only for non-singular matrices)
try:
    inverse_a = np.linalg.inv(matrix_a)
    print("Inverse of Matrix A:\n", inverse_a)
except np.linalg.LinAlgError:
    print("Matrix A is singular and cannot be inverted.")

# 11. Square Root (element-wise)
sqrt_a = np.sqrt(matrix_a)
print("Square Root of Matrix A (element-wise):\n", sqrt_a)

import numpy as np

# Define two 3x3 matrices
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# 1. Addition
addition = matrix_a + matrix_b  # Element-wise addition
print("Element-wise Addition:\n", addition)

# 2. Subtraction
subtraction = matrix_a - matrix_b  # Element-wise subtraction
print("Element-wise Subtraction:\n", subtraction)

# 3. Element-wise Multiplication
elementwise_multiplication = np.multiply(matrix_a, matrix_b)  # Using np.multiply
print("Element-wise Multiplication (np.multiply):\n", elementwise_multiplication)

# 4. Matrix Multiplication (Dot Product)
matrix_multiplication = np.dot(matrix_a, matrix_b)  # Using np.dot for matrix multiplication
print("Matrix Multiplication (Dot Product):\n", matrix_multiplication)

# 5. Element-wise Division
elementwise_division = matrix_a / matrix_b  # Element-wise division
print("Element-wise Division:\n", elementwise_division)

# 6. Flattening
flattened = matrix_a.flatten()
print("Flattened Matrix A:\n", flattened)

# 7. Reshaping (reshaping to 1x9)
reshaped = matrix_a.reshape(1, 9)
print("Reshaped Matrix A (1x9):\n", reshaped)

# 8. Transpose
transpose_a = matrix_a.T
print("Transpose of Matrix A:\n", transpose_a)

# 9. Diagonal Matrix
diagonal_matrix = np.diag(np.diag(matrix_a))  # Extracting diagonal
print("Diagonal Matrix from Matrix A:\n", diagonal_matrix)

# 10. Concatenation (along rows)
concatenated = np.concatenate((matrix_a, matrix_b), axis=0)
print("Concatenated Matrix (along rows):\n", concatenated)

# 11. Inverse (only for non-singular matrices)
try:
    inverse_a = np.linalg.inv(matrix_a)
    print("Inverse of Matrix A:\n", inverse_a)
except np.linalg.LinAlgError:
    print("Matrix A is singular and cannot be inverted.")

# 12. Square Root (element-wise)
sqrt_a = np.sqrt(matrix_a)
print("Square Root of Matrix A (element-wise):\n", sqrt_a)