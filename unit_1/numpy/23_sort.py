import numpy as np 

a = np.array([12, 15, 10, 1]) 
print("Array before sorting",a) 
a.sort() 
print("Array after sorting",a) 


b = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(b, axis = 0)		 
print ("Along first axis : \n", arr1)		 
# sort along the last axis 
c = np.array([[10, 15], [12, 1]]) 
arr2 = np.sort(c, axis = -1)		 
print ("\nAlong first axis : \n", arr2) 
d = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(d, axis = None)		 
print ("\nAlong none axis : \n", arr1)

