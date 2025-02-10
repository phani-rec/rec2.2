# importing numpy module 
import numpy as np 

# logical operations between boolean values 
print('Operation between true and true ( 1 and 1) = ', 
	np.logical_xor(True, True)) 
print('Operation between true and false ( 1 and 0) = ', 
	np.logical_xor(True, False)) 
print('Operation between false and true ( 0 and 1) = ', 
	np.logical_xor(False, True)) 
print('Operation between false and false (0 and 0)= ', 
	np.logical_xor(False, False)) 


# list 1 represents an array with boolean values 
list1 = [True, False, True, False] 

# list 2 represents an array with boolean values 
list2 = [True, True, False, True] 

# logical operations between boolean values 
print('Operation between two lists = ', 
	np.logical_xor(list1, list2)) 


# list 1 represents an array 
# with integer values 
list1 = [1, 2, 3, 4, 5, 0] 

# list 2 represents an array 
# with integer values 
list2 = [0, 1, 2, 3, 4, 0] 

# logical operations between integer values 
print('Operation between two lists = ', 
	np.logical_xor(list1, list2)) 
