# This problem is based on Problem 2.7.5 from the textbook

# We are given the formulae for range and height of a projectile flying over flat terrain.
# We are to write a function that calculates and returns the value of maximum range
# and height of a projectile by having velocity, v and launching angle, alpha as inputs.

#Importing necessary package
import math

#Definition of the function
def projectile_motion(v, alpha):
    """Calculate the range and maximum height of a projectile."""
    # Constants
    g = 9.81  # Acceleration due to gravity in m/s^2

    # Convert angle from degrees to radians
    alpha_rad = math.radians(alpha)

    # Calculate range (R)
    R = (v ** 2 * math.sin(2 * alpha_rad)) / g

    # Calculate maximum height (H)
    H = (v ** 2 * (math.sin(alpha_rad) ** 2)) / (2 * g)

    return R, H


# Test the function with v = 10 m/s and α = 30°
v_test = 10  # m/s
alpha_test = 30  # degrees

range_result, height_result = projectile_motion(v_test, alpha_test)
print("Range (R):", range_result)
print("Maximum Height (H):", height_result)
