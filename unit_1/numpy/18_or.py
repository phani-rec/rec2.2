import numpy as np 
print('logical_or operation = ', 
	np.logical_or(True, False)) 

a = 2
b = 6
print('logical or Operation between two variables = ',np.logical_or(a, b)) 
a = 0
b = 0
print('logical or Operation between two variables = ',np.logical_or(a, b)) 


# list 1 represents an array with integer values 
list1 = [1, 2, 3, 4, 5, 0] 

# list 2 represents an array with integer values 
list2 = [0, 1, 2, 3, 4, 0] 

# logical operations between integer values 
print('Operation between two lists = ', 
	np.logical_or(list1, list2)) 
