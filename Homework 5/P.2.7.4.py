# This problem is based on Problem 2.7.4 from the textbook. Question available in "photo" folder

# This questions asks us to write a program that we define a function "pyramid_AV"
# with output V and S when inputting n, s and h
# (The question not included in the snapshot but is in the book)

import math

def pyramid_AV(n, s, h):
    """Calculate the volume and surface area of a right regular pyramid."""
    # Calculate the apothem a
    a = 0.5 * s * (1 / math.tan(math.pi / n))

    # Calculate the base area A
    A = 0.5 * n * s * a

    # Calculate the slant height l
    l = math.sqrt(h ** 2 + a ** 2)

    # Calculate the volume V
    V = (1 / 3) * A * h

    # Calculate the surface area S
    S = A + 0.5 * n * s * l

    return V, S


n = 5  # Number of sides
s = 4  # Side length of the base polygon
h = 10  # Height of the pyramid

volume, surface_area = pyramid_AV(n, s, h)
print("Volume (V):", volume)
print("Surface Area (S):", surface_area)