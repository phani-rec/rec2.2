import numpy as np

# Define two 3x3 matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Perform matrix addition
result = np.add(matrix1, matrix2)

# Alternatively, you can use the + operator for addition
# result = matrix1 + matrix2

print("Matrix Addition Result:")
print(result)
