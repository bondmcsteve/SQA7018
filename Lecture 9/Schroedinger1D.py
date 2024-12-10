import matplotlib.pyplot as plt
import numpy as np
import random as random

n_points = 10000
L_limit = 5
h_bar = 1
mass = 1

class Schroedinger:
    def __init__(self, n_points, l_limit):
        self.n_points = n_points
        self.l_limit = l_limit
        self.potential = 0
        self.mass = 1
        self.x_discrete = []

    def Ke_prefactor:
        prefactor = -(h_bar**2) / 2m

    """Declaring discrete instance"""
    def discretize(self):
        self.x_discrete = np.linspace(0, self.l_limit, self.n_points)
        return self.x_discrete

    """Declaring the hamiltonian matrix instance"""
    def finite_difference_approximation(self, discrete):
        approx = wavefunc[]