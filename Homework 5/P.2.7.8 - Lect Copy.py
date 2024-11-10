# This problem is based on Problem 2.7.8 from the textbook.

# The question asks us to evaluate the tetration of a function

# Our program will produce long string of numbers which usually
# not supported by standard settings. We will need to import necessary package for this

import sys
sys.set_int_max_str_digits(0)

# Begin with defining the tetration function
def tetration(x,n):
    if n == 0:
        return 1

    # Using the recursion technique similar to P2.7.7
    return x ** tetration(x, n-1)

def count_digit(number):
    return len(str(number)) #String length = amount of digits

# Test cases
tetration_2_5 = tetration(2,5)
digits_2_5 = count_digit(tetration_2_5)

print(f"Tetration of ^5 2: : {tetration_2_5}")
print(f"Number of digits in ^5 2: {digits_2_5}")