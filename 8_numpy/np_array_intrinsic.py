import numpy as np

# intrinsic methods of creating numpy arrays

zeroarray = np.zeros([2,3]) # creates 2 X 3 array containing floating-pt zeroes
print(zeroarray)

rng1 = np.arange(8)
print(rng1) # [0 1 2 3 4 5 6 7]

rng2  = np.arange(4,10)
print(rng2) # [4 5 6 7 8 9]

rngreverse = np.arange(15,3,-3)
print(rngreverse) # [15 12  9  6]

# linear space method
spacedarray = np.linspace(3,10,9)
print(spacedarray)

emp = np.empty((3,2),dtype=int) # creates a 3 X 2 unitialised array 
print(emp) 

emp[0,0] = 6
print(emp)

myarray = np.array([4,3,9]) # 1-Dimensional array
print(myarray.dtype) # int64
print(myarray.ndim)  # 1
print(myarray.size)  # 3
print(myarray.shape) # (3,)
alikearray = np.empty_like(myarray)
print(alikearray)

print("\ncreating an identity matrix")
ideamatrix = np.identity(4) # 4 x 4 identity matrix
print(ideamatrix)
print(ideamatrix.shape) # (4, 4)