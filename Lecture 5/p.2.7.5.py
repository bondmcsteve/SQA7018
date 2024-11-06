# This Problem is a part of the lecture session.
# It is based on Problem 2.7.5 from the textbook.

# We are given the formula for range and max height of projectile launched
# Determine both values using function

#Declare necessary packages
import numpy as np
import math

H = []
R = []
g = 9.81 #in m/s^2

#Defining the function for the equations
#Define function for height
def max_range(v, a_rad):
    R = ((v**2) * (np.sin(2*a))) / g
    return H

def max_height(v, a_rad):
    H = ((v**2) * (sin(a))**2) / (2 * g)
    return H

def angle_rad: