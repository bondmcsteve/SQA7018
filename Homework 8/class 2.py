# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:29:15 2024

@author: User
"""

import math
import numpy as np

class Spring:
    def __init__(self, m, k, c, x0, v0):
        self.m = m  # Mass
        self.k = k  # Spring constant
        self.c = c  # Damping coefficient
        self.x0 = x0  # Initial displacement
        self.v0 = v0  # Initial velocity

        # Calculate damping ratio and natural frequency
        self.omega0 = math.sqrt(k / m)
        self.zeta = c / (2 * math.sqrt(k * m))

    def position(self, t):
        omega0 = self.omega0
        zeta = self.zeta

        if zeta < 1:  # Underdamped
            omega_d = omega0 * math.sqrt(1 - zeta ** 2)
            A = self.x0
            B = (self.v0 + zeta * omega0 * self.x0) / omega_d
            x_t = math.exp(-zeta * omega0 * t) * (A * math.cos(omega_d * t) + B * math.sin(omega_d * t))
        elif zeta == 1:  # Critically damped
            A = self.x0
            B = self.v0 + omega0 * self.x0
            x_t = (A + B * t) * math.exp(-omega0 * t)
        else:  # Overdamped
            r1 = -omega0 * (zeta - math.sqrt(zeta ** 2 - 1))
            r2 = -omega0 * (zeta + math.sqrt(zeta ** 2 - 1))
            A = (self.v0 - r2 * self.x0) / (r1 - r2)
            B = (r1 * self.x0 - self.v0) / (r1 - r2)
            x_t = A * math.exp(r1 * t) + B * math.exp(r2 * t)

        return x_t

# Instantiate a Spring object
spring = Spring(m=1.0,    # Mass in kg
                k=20.0,   # Spring constant in N/m
                c=2.0,    # Damping coefficient in Ns/m
                x0=0.1,   # Initial displacement in meters
                v0=0.0)   # Initial velocity in m/s

# Compute and print positions at intervals from t=0 to t=10
time_intervals = np.arange(0, 10.1, 0.1)
positions = [spring.position(t) for t in time_intervals]

print("Time (s)\tPosition (m)")
for t, x in zip(time_intervals, positions):
    print(f"{t:.1f}\t\t{x:.5f}")
