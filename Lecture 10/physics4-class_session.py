import random
import numpy as np
from scipy.

"""Step 1: Discretization of N-size array"""
N = 1000 #Input certain value here
gridsize = N * N
x = np.linspace(0,1,N)
y = np.linspace(0,1,N)
#array_2D_discrete = np.linsc

dx = 1/N
dy = 1/N

"""Step 2: 2nd order differential using finite difference method"""
diag = np.full(N, -2.0) # This syntax is to create 1-D matrix with the size N with all elements having fill value of -2.0
off_diag = np.ones(N - 1) # Establish a one dimensional matrix having 999 entries with all elements being 1.0
laplacian = (np.diag(diag) + np.diag(off_diag, -1) + np.diag(off_diag, 1)) / dx**2