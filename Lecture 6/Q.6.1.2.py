"""This problem is based on Q6.1.2 from the textbook"""
import numpy as np
import math

"""Need to use square bracket to enclose the array rows"""
arr = np.array([(1,0,0), (0,1,0), (0,0,1)], dtype=float)

#ignore
arr2 = np.array([(1,0,0), (0,1,0)])
#arr3 = np.array([1,0,0], [0,1,0], [0,0,1], dtype=float)
print(arr)
print(np.ndim(arr))

print(arr2)
print(np.ndim(arr2))