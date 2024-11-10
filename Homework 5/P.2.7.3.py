# This problem is based on Problem 2.7.3 in the textbook

# The problem asks us to write a program that calculates dot, cross product, and triple product
# of both types.

def dot_product(a, b):
    """Calculate the dot product of two 3D vectors a and b."""
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def cross_product(a, b):
    """Calculate the cross product of two 3D vectors a and b."""
    cross = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]
    return cross

def scalar_triple_product(a, b, c):
    """Calculate the scalar triple product of vectors a, b, and c."""
    return dot_product(a, cross_product(b, c))

def vector_triple_product(a, b, c):
    """Calculate the vector triple product of vectors a, b, and c."""
    b_cross_c = cross_product(b, c)
    return cross_product(a, b_cross_c)

# Test cases
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print("Dot product (a · b):", dot_product(a, b))         # Expected output: scalar value
print("Cross product (a × b):", cross_product(a, b))      # Expected output: vector
print("Scalar triple product (a · (b × c)):", scalar_triple_product(a, b, c))  # Expected output: scalar value
print("Vector triple product (a × (b × c)):", vector_triple_product(a, b, c))  # Expected output: vector
