import numpy as np

# creating numpy array using various methods
myarray = np.array([[1,2,3,4],[5,6,7,8]]) # 2D array [[]]
print(myarray)
print(type(myarray)) # <class 'numpy.ndarray'>
print(myarray.shape) # (2, 4)
print(myarray.dtype) # int64
print(myarray.size)  # 8
print(myarray[1,2]) # acessing element in  2nd row third column
myarray[1,2] = 5    # numpy arrays are mutable
print(myarray[0,2]) # 3
print(myarray.ndim) # checks dimensions of an array, in this case 2

decimals = np.array([[1.3, 3.2, 7.3],[2.2,4.5,6.0]])
print(decimals.dtype) # float64

letters = np.array(["RVCE",True,1,3.14])
print(letters)
print(type(letters))
print(letters.dtype) # <U32 for unicode 32

mynums = np.array(range(2,14,3)) # [ 2  5  8 11]
print(mynums)
print(mynums.dtype) # int64

rngnums = np.array(range(20,4,-4)) # [20 16 12  8]
print(rngnums)

setsarray = np.array({2,"hi",4,6})
print(setsarray)
print(type(setsarray)) 
print(setsarray.dtype) # object

my1darr = np.array([[[0,7,-1]]]) # creates a 3D array 
print(my1darr.shape) # (1, 1, 3)
print(my1darr.ndim)  # checking dimensions of an array