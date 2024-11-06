# This Problem is a part of the lecture session.
# It is based on Problem 2.7.8 from the textbook.

# This is a tetration problem.

import numpy as np
import math
import sys

sys.set_int_max_str_digits(50000000)

#Begin with converting the tetration notation to exponent
def tetra_to_exp(x, n):
    val = x
    for i in range(n-1):
        #val = x ** val
        val = x ** val
    return val

x = 2
n = 5
val = tetra_to_exp(x, n)
print(val)
val_len = str(val)

print("Amount of digit is : " + str(len(val_len)))