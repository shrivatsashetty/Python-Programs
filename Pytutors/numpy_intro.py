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
print(myarray[1,2]) # 5

decimals = np.array([[1.3, 3.2, 7.3],[2.2,4.5,6.0]])
print(decimals.dtype) # float64

letters = np.array("R,V,C,E")
print(letters)
print(type(letters))
print(letters.dtype) # <U7

mynums = np.array(range(2,14,3)) # [ 2  5  8 11]
print(mynums)
print(mynums.dtype) # int64

rngnums = np.array(range(20,4,-4)) # [20 16 12  8]
print(rngnums)

setsarray = np.array({2,"hi",4,6})
print(setsarray)
print(type(setsarray))
print(setsarray.dtype)