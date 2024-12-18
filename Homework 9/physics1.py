import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0  # Reduced Planck constant
m = 1.0     # Mass of the particle
L = 1.0     # Length of the box

"""Step 1: Spatial discretization using linear space function"""
N = 1000   # Number of points
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Construct the Hamiltonian matrix
# Using finite difference: -hbar^2/(2m) * d^2/dx^2

"""Kinetic energy operator"""
diag = np.full(N, -2.0) # This syntax is to create 1-D matrix with the size N with all elements having fill value of -2.0
off_diag = np.ones(N - 1) # Establish a one dimensional matrix having 999 entries with all elements being 1.0
laplacian = (np.diag(diag) + np.diag(off_diag, -1) + np.diag(off_diag, 1)) / dx**2

# np.diag(diag) extracts only the diagonal component from variable diag
# np.diag(off_diag, -1) extracts the subdiagonal component from off_diag
# np.diag(off_diag, 1) extracts the superdiagonal component from off_diag
# dx**2 here represents delta x**2
# Combining them together gives us laplacian matrix

"""We are seeing that laplacian variable should have diagonal component of -2.0 with subdiagonal and superdiagonal of 1"""
"""Remember that Laplacian matrix is a matrix that behaves as an operator which acts as second-order scalar differentiation"""

"""Step 2: Declaring the hamiltonian matrix, H in form of Laplacian"""
H = -(hbar**2) / (2 * m) * laplacian

# Apply boundary conditions (wavefunction zero at x=0 and x=L)
# This is implicit in the finite difference method as we exclude the boundary points

"""Solving for both eigenvalues and eigenvectors of the Hamiltonian using np.linalg.eigh()"""
# Solve the eigenvalue problem
eigenvalues, eigenvectors = np.linalg.eigh(H)

# Extract the first three eigenvalues and eigenvectors
E_numerical = eigenvalues[:3]
psi_numerical = eigenvectors[:, :3]

# Analytical solutions for comparison
n_values = np.array([1, 2, 3])
E_analytical = (n_values**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Print the numerical and analytical energies
print("Numerical Energies:")
for i, E in enumerate(E_numerical):
    print(f"E_{i+1} = {E:.5f}")

print("\nAnalytical Energies:")
for i, E in enumerate(E_analytical):
    print(f"E_{i+1} = {E:.5f}")

# Normalize the eigenfunctions
psi_numerical = psi_numerical / np.sqrt(dx)

# Plot the first three eigenfunctions
plt.figure(figsize=(10, 6))
for i in range(3):
    plt.plot(x, psi_numerical[:, i], label=f"n={i+1}")

plt.title("First Three Energy Eigenfunctions of a Particle in a Box")
plt.xlabel("Position x")
plt.ylabel("Wavefunction ψ_n(x)")
plt.legend()
plt.grid(True)
plt.show()
