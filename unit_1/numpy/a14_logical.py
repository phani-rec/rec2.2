import numpy as np
arr = np.array([True, True, False])
result = np.all(arr)  # Output: False
print(result)
print('\n')

arr = np.array([False, False, True])
result = np.any(arr)  # Output: True
print(result)
print('\n')

arr = np.array([1, 2, 3, 4])
result = np.where(arr > 2, arr, 0)  # Output: [0 0 3 4]
print(result)
print('\n')

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 3, 3])
result = np.equal(arr1, arr2)  # Output: [ True False  True]
print(result)
print('\n')

arr = np.array([1, 2, np.nan, 4])
result = np.isnan(arr)  # Output: [False False  True False]
print(result)
print('\n')