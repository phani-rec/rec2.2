import numpy as np 

arr = np.array([1, 0, 1, 0, 0, 1, 0]) 

print("Original Array: ",arr) 

bool_arr = np.array(arr, dtype='bool') 

print('Boolean Array:', bool_arr) 

arr2 = np.array([5, None, 1, 25, -10, 0, 'A']) 
  
print('Original Array: ',arr2) 
  
bool_arr = np.array(arr2, dtype='bool') 
  
print('Boolean Array: ',bool_arr) 
