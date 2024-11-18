""""This problem is based on Problem 6.1.3 in the Textbook"""

import numpy as np
import matplotlib.pyplot as plt


# Define the Gaussian function
def gaussian(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))


# Parameters
mu = 0
sigmas = [0.5, 1.0, 1.5]
x = np.linspace(-10, 10, 1000)  # 1000 points in the interval [-10, 10]
h = 0.01  # Small step for derivative calculation

# Plot the Gaussian functions
plt.figure(figsize=(10, 6))
for sigma in sigmas:
    g_x = gaussian(x, mu, sigma)
    plt.plot(x, g_x, label=f'σ = {sigma}')

    # Check normalization by integrating (summing) using the trapezoidal rule
    area = np.trapz(g_x, x)
    print(f'Normalization check for σ={sigma}: Area = {area:.4f}')

plt.title("Gaussian Functions for Different σ Values")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.show()

# Calculate and plot the first derivative using central difference approximation
plt.figure(figsize=(10, 6))
for sigma in sigmas:
    g_x = gaussian(x, mu, sigma)
    g_prime_x = (gaussian(x + h, mu, sigma) - gaussian(x - h, mu, sigma)) / (2 * h)
    plt.plot(x, g_prime_x, label=f'σ = {sigma}')

plt.title("First Derivative of Gaussian Functions for Different σ Values")
plt.xlabel("x")
plt.ylabel("g'(x)")
plt.legend()
plt.show()