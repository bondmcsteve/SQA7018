#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:02:46 2024

@author: andy
"""

# Generate and print Pascal's Triangle for the first 8 rows without using functions, map, or join

# Initialize the triangle with the first row
triangle = [[1]]

# Generate rows from the second row up to the 8th row
for i in range(1, 8):
    prev_row = triangle[-1]  # Get the previous row
    # New row starts and ends with 1, with intermediate values being the sum of adjacent numbers from the previous row
    new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
    triangle.append(new_row)

# Print the triangle in a nicely formatted way
n = len(triangle)
for i, row in enumerate(triangle):
    # Center the rows by adding spaces
    print(" " * (n - i), end=" ")  # Print leading spaces
    for num in row:
        print(num, end="   ")  # Print each number with spaces
    print()  # Newline after each row
