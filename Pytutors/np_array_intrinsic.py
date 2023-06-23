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