import numpy as np
arr = np.array([1, 2, 3])
total = np.sum(arr)  # Output: 6
print(total)
print('\n')

arr = np.array([1, 2, 3, 4])
mean = np.mean(arr)  # Output: 2.5
print(mean)
print('\n')

arr = np.array([1, 3, 2])
median = np.median(arr)  # Output: 2.0
print(median)
print('\n')

arr = np.array([1, 2, 3, 4])
std_dev = np.std(arr)  # Output: 1.118
print(std_dev)
print('\n')

arr = np.array([1, 2, 3, 4])
min_val = np.min(arr)  # Output: 1
max_val = np.max(arr)  # Output: 4
print(min_val , ' ', max_val)
print('\n')

a = np.array([1, 2])
b = np.array([3, 4])
result = np.dot(a, b)  # Output: 11 (1*3 + 2*4)
print(result)
print('\n')

arr = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(arr)
print(inverse)
print('\n')


arr = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(arr)  # Output: -2.0
print(determinant)
print('\n')