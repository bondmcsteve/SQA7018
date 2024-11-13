# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:59:57 2024

@author: Woon
"""

# The problem is based on Problem 2.7.6 from the textbook.

# The problem asks us to write a function "sinm_cosn" which returns
# a definite integral
import math

# Defining the double factorial function.
# No need for even and odd distinction in P2.4.6
def double_factorial(n):
    """Calculate the double factorial of n."""
    if n<0 :
        raise ValueError("Negative Input is not allowed.")
    if n <= 0:
        return 1
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result


def sinm_cosn(m, n):
    """Calculate the definite integral of sin^n(theta) * cos^m(theta) from 0 to pi/2."""
    # Check if both m and n are even
    if m % 2 == 0 and n % 2 == 0:
        # Both m and n are even
        result = (double_factorial(m - 1) * double_factorial(n - 1) * math.pi) / (2 * double_factorial(m + n))
    else:
        # m or n (or both) are odd
        result = (double_factorial(m - 1) * double_factorial(n - 1)) / double_factorial(m + n)

    return result


# m = 4  # example m (even)
# n = 6  # example n (even)
# print("Integral result for m = 4 and n = 6:", sinm_cosn(m, n))
#
# m = 3  # example m (odd)
# n = 5  # example n (odd)
# print("Integral result for m = 3 and n = 5:", sinm_cosn(m, n))

# Quiz 5, Q8, ValueError() is raised
m = 0  # example m (odd)
n = 1  # example n (odd)
print("Integral result for m = 0 and n = 1:", sinm_cosn(m, n))