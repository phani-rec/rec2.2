import numpy as np

# Creating a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing: Access the element at (1, 2)
element = arr[1, 2]
print("Element at index (1, 2):", element)

# Slicing: Extract a sub-array
sub_array = arr[0:2, 1:3]
print("Sliced Sub-array:")
print(sub_array)
