#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:46:10 2024

@author: andy
"""

# Import relevant packages for maths and plottings
import numpy as np
import matplotlib.pyplot as plt

# Dumping the constants for Argon atoms
A = 1.024e-23 #J nm^6
B = 1.582e-26 #J nm^12
k_b = 1.381e-23 # J K^-1

# Division of A and B to Boltzmann constant as per question recommendation
A /= k_b
B /= k_b 

# We define the potential function U(r) and force function F(r) 

# New! Function definition
def U(r):
    return (B / r**12) - (A / r**6)

def F(r):
    return ((12*B) / r**13) - ((6*A) / r**7)

# Initiate np.linspace() for discrete computation.
# Choose start and end points in a way that they enclose the equilibrium point, which supposedly falls 
# on 0.38164103. For this case, we can just choose 0.3 up to 0.7

# Begin by assigning r to with the np.linspace()
r = np.linspace(0.3, 0.7, 1000)

# Now, the calculation shall their inputs on the r. Defined functions are summoned as following
U_vals = U(r)
F_vals = F(r)

min_index = np.argmin(U_vals)
epsilon = U_vals[min_index]
r0 = r[min_index]

# Calculation for k-term is expressed as follows
k = ((156*B) / (r0**14)) - ((42*A) / (r0**8))
V_val = ((1/2)*k*((r-r0)**2)) + epsilon  

# Setting up plots
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plotting U(r)
color = 'tab:red' # Designating the color scheme for this plot
ax1.set_xlabel('r (nm)') # Labelling the x-axis
ax1.set_ylabel('U(r) (K)', color = color) # Labelling the y-axis
ax1.plot(r, U_vals, color = color, label = 'U(r) - Leonard-Jones Potential') # Labelling the plot name
ax1.tick_params(axis = 'y', labelcolor = color)
ax1.grid(True) # Enable grid appearance

# Overlaying the next graph, F(r), onto the same plot
ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('F(r) (K/nm)', color = color2)
ax2.plot(r, F_vals, color = color2, label = 'F(r) - Force', linestyle = '--')
ax2.tick_params(axis = 'y', labelcolor = color2)

# Adjustment on y-axis for better visibility
ax1.set_ylim(epsilon * 1.5, max(U_vals) * 0.5)
ax2.set_ylim(min(F_vals) * 1.5, max(F_vals) * 0.5)

# Plotting for the harmonic approximation graph
color3 = 'tab:green'
ax1.plot(r, V_val, color = color3, linestyle = '-.', label = 'V(r) - Harmonic Approximation')

# Adding text to highlight epsilon and r0
ax1.text(r0, epsilon, f'ϵ = {epsilon:.3f} K\nr0 = {r0:.3f} nm',
        ha = 'right', va = 'bottom', fontsize = 10, color = 'black')

# Title and layout adjustments 
plt.title('Leonard-Jones Potential and Force for Argon', fontsize = 14)
fig.tight_layout()

# Add legends
ax1.legend(loc = 'upper left', fontsize = 10)
ax2.legend(loc = 'upper right', fontsize = 10)

# Show plot
plt.show()