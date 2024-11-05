# This homework is based on Problem P2.5.2 from the textbook
# Tutorial on https://www.youtube.com/watch?v=TRpf0TiICjE

# From the problem, we understand that:
# 1. We need to calculate AGM by using the formula, and then determine Gauss const.
# 2. There will be 2 formulae in said order
# 3. 3 inputs: x, y, and n (or any suitable exit condition for convergence)
# 4. Initial conditions a0 = x and y0 = y

# Import necessary package
import numpy as np

#a_n = []
#b_n = []
#a_nplus = []
#b_nplus = []

# We begin by defining the function for AGM
def agm(x, y, tol=1e-10):
    a_n, b_n = x, y # Tutorial uses a and b for a_n and b_n
    # Loop statement
    while abs(a_n - b_n) > tol:
        # General formula for a and b terms
        a_nplus = (1/2) * (a_n + b_n)
        b_nplus = np.sqrt(a_n * b_n)
        a_n, b_n = a_nplus, b_nplus # Tutorial uses a_next and b_next for a_nplus and b_nplus
    # Return converged value
    return a_n # We can exclude b_n since a_n = b_n

x = float(input("Enter x value : "))
y = float(input ("Enter y value : "))
#x = 1 # Original code
#y = np.sqrt(2) # Original code
agm_value = agm(x,y)

# Calculation for Gauss constant
G = 1 / agm_value
print(agm_value, G) # Return both AGM and Gauss values
