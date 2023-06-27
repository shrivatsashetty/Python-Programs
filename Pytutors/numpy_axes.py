import numpy as np

arr = np.array([[[9, 9, 9],[1,2,3],[4,5,7]]])
print("The array looks like this\n",arr)
print("Shape: ",arr.shape)
print("Dimensions :",arr.ndim)
print("total elements: ",arr.size)
print("The length of axes are:")
for axis in arr.shape:
    print(axis)
# length_axis_0 = arr.shape[0]
# length_axis_1 = arr.shape[1]

# print(length_axis_0)  # Output: 4
# print(length_axis_1)  # Output: 3