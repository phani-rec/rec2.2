import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshape = arr.reshape(2, 3)  # 2x3 array
print(reshape)
print('\n')

arr = np.array([[1, 2], [3, 4]])
flat = np.ravel(arr)
print(flat)
print('\n')

arr = np.array([[1, 2], [3, 4]])
transpose = np.transpose(arr)
print(transpose)
print('\n')

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
result = np.concatenate((arr1, arr2))  # Output: [1, 2, 3, 4]
print(result)
print('\n')

arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 3)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]
print(result)
print('\n')

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
result = np.vstack((arr1, arr2))  # Output: [[1 2] [3 4]]
print(result)
print('\n')

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
result = np.hstack((arr1, arr2))  # Output: [1 2 3 4]
print(result)
print('\n')