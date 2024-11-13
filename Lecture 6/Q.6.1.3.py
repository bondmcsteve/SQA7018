"""This problem is from Q6.1.3 from the textbook"""
import numpy as np

a = np.array([0,0,0]) #1-D array, also known as vector
a2 = np.array([[0,0,0]]) #2-D array, also known as matrix

print("Dimension of a is: " + str(np.ndim(a)))
print("Dimension of a2 is: " + str(np.ndim(a2)))

"""Dimensionality of an array depends on how many square enclosures used to enclose the elements of array"""