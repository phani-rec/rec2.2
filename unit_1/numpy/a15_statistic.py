import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
correlation = np.corrcoef(arr1, arr2)  # Output: [[1. 1.] [1. 1.]]
print(correlation)

arr = np.array([1, 2, 3, 4, 5])
percentile_50 = np.percentile(arr, 50)  # Output: 3.0
print(percentile_50)