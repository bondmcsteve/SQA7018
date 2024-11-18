""""This problem is based on Problem 6.4.3 in the textbook"""

import numpy as np
import matplotlib.pyplot as plt

# Constants for ammonia
a = 4.225  # L^2 bar mol^-2
b = 0.03707  # L mol^-1
R = 0.08314  # L bar K^-1 mol^-1

# Part (a) - Calculate critical temperature and pressure
T_c = (8 * a) / (27 * R * b)
p_c = a / (27 * b ** 2)

print(f"Critical Temperature (T_c): {T_c:.2f} K")
print(f"Critical Pressure (p_c): {p_c:.2f} bar")


# Function to solve van der Waals cubic equation for volume using numpy's roots
def van_der_waals_volume(T, p):
    # Coefficients of the cubic equation pV^3 - (pb + RT)V^2 + aV - ab = 0
    coeffs = [p, -(p * b + R * T), a, -a * b]

    # Find roots of the polynomial
    roots = np.roots(coeffs)

    # Filter for real roots (ignore complex roots)
    real_roots = roots[np.isreal(roots)].real

    # Choose the largest positive real root (molar volume in gas phase)
    V_molar = max(real_roots)  # assuming largest root represents the gas phase volume
    return V_molar


# Molar volume at (298 K, 1 atm) and (500 K, 120 bar)
V_298K_1atm = van_der_waals_volume(298, 1.01325)  # Convert 1 atm to bar
V_500K_120bar = van_der_waals_volume(500, 120)

print(f"Molar Volume at 298 K, 1 atm: {V_298K_1atm:.4f} L/mol")
print(f"Molar Volume at 500 K, 120 bar: {V_500K_120bar:.4f} L/mol")

# Part (b) - Plot the isotherm at T = 350 K for van der Waals and ideal gas
T_isotherm = 350  # K
epsilon = 1e-5  # Small value to avoid V = b
V_values = np.linspace(b + epsilon, 1.5, 100)  # Start slightly above b

# Calculate pressures for van der Waals gas
p_vdw = [(R * T_isotherm / (V - b)) - (a / V ** 2) for V in V_values]

# Calculate pressures for ideal gas
p_ideal = [R * T_isotherm / V for V in V_values]

# Plotting the isotherms
plt.figure(figsize=(10, 6))
plt.plot(V_values, p_vdw, label="Van der Waals Isotherm (T=350 K)", color="blue")
plt.plot(V_values, p_ideal, label="Ideal Gas Isotherm (T=350 K)", color="red", linestyle="--")
plt.xlabel("Molar Volume (V) [L/mol]")
plt.ylabel("Pressure (p) [bar]")
plt.legend()
plt.title("Isotherms for Ammonia at 350 K")
plt.ylim(0, 150)  # Limit y-axis for better visualization
plt.grid(True)
plt.show()