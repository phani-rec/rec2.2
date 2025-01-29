import numpy as np
arr = np.array([1, 2, 3])
print(arr)
print('\n')

ar2 = np.zeros((3, 3))  # 3x3 array of zeros
print(ar2)
print('\n')

ar3 = np.ones((2, 3))  # 2x3 array of ones
print(ar3)
print('\n')

ar4 = np.arange(0, 10, 2)  # Output: [0, 2, 4, 6, 8]
print(ar4)
print('\n')

ar5 = np.linspace(0, 1, 5)  # Output: [0.   0.25 0.5  0.75 1.  ]
print(ar5)
print('\n')

ar6 = np.eye(3)  # 3x3 identity matrix
print(ar6)
print('\n')

ar7 = np.random.rand(2, 3)  # 2x3 array of random numbers
print(ar7)
print('\n')

ar8 = np.random.randint(0, 10, size=(2, 3))  # 2x3 array of random integers
print(ar8)
print('\n')



