import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

"""Computation range and discretization value"""
dx = 0.1
dy = 0.1
N = int(10 / dx) + 1
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
Cx = 5
Cy = 5
alpha = 2

"""Size of the 2-D grid"""
N_size = N * N

# Initialize the coefficient matrix and right-hand side vector
A = lil_matrix((N_size, N_size))
b = np.zeros(N_size)

"""Map 2D indices to 1D indices"""
def idx(i, j):
    return i + j * N

"""Initial values"""
u0 = np.exp(-((x - Cx)**2 + (y - Cy)**2) / alpha**2)

# Set up the equations
for j in range(N):
    for i in range(N):
        k = idx(i, j)
        if i == 0:
            # Left boundary
            A[k, k] = 1
            b[k] = 0
        elif i == N - 1:
            # Right boundary
            A[k, k] = 1
            b[k] = np.sin(np.pi * y[j])
        elif j == 0 or j == N - 1:
            # Top and bottom boundaries
            A[k, k] = 1
            b[k] = 0
        else:
            # Interior points
            A[k, idx(i+1, j)] = 1 / dx**2
            A[k, idx(i-1, j)] = 1 / dx**2
            A[k, idx(i, j+1)] = 1 / dy**2
            A[k, idx(i, j-1)] = 1 / dy**2
            A[k, k] = -2 * (1 / dx**2 + 1 / dy**2)
            b[k] = 0


