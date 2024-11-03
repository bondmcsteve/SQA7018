# This homework is based on Problem P2.5.2 from the textbook
# Tutorial on https://www.youtube.com/watch?v=TRpf0TiICjE

# From the problem, we understand that:
# 1. We need to calculate AGM by using the formula, and then determine Gauss const.
# 2. There will be 2 formulae in said order
# 3. 3 inputs: x, y, and n (or any suitable exit condition for convergence)
# 4. Initial conditions a0 = x and y0 = y

# Import necessary package
import numpy as np

# We begin by defining the function for AGM
def agm(x, y, n):
