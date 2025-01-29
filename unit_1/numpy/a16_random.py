import numpy as np
arr = np.array([1, 2, 3, 4])
result = np.random.choice(arr, size=2, replace=False)  # Output: [4 2]
print(result)

arr = np.array([1, 2, 3, 4])
result=np.random.shuffle(arr)
print(result)
