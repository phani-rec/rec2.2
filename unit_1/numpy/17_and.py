# importing numpy module 
import numpy as np 


l1 = [True, False, True, False] 


l2 = [True, True, False, True] 


l3 = [1, 2, 3, 4, 5, 0] 
  
# list 2 represents an array  
# with integer values 
l4 = [0, 1, 2, 3, 4, 0] 
  

# logical operations between boolean values 
print('Operation between two lists = ', 
	np.logical_and(l1, l2))
# logical operations between integer values 
print('Operation between two lists:',  
      np.logical_and(l3, l4)) 
