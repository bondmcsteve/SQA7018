import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lx, Ly = 10, 10  # Domain size
Nx, Ny = 101, 101  # Grid points
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)  # Grid spacing
dt = 0.01  # Time step (adjust based on CFL condition)
T = 100.0  # Total time
alpha = 2.0  # Width of Gaussian
cx, cy = 5.0, 5.0  # Center of initial condition
x0, y0 = 7.0, 5.0  # Circulation center
v0 = 0.1  # Circulation speed

# Grid
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Initial condition
U = np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / alpha ** 2)

# Velocity field (circulation at constant speed)
vx = -v0 * (Y - y0) / np.sqrt((X - x0) ** 2 + (Y - y0) ** 2 + 1e-8)  # Add small value to avoid division by zero
vy = v0 * (X - x0) / np.sqrt((X - x0) ** 2 + (Y - y0) ** 2 + 1e-8)

# Time stepping loop
U_new = np.copy(U)
for n in range(int(T / dt)):
    # Central differences for spatial derivatives
    dUdx = (np.roll(U, -1, axis=1) - np.roll(U, 1, axis=1)) / (2 * dx)
    dUdy = (np.roll(U, -1, axis=0) - np.roll(U, 1, axis=0)) / (2 * dy)

    # Update equation
    U_new = U - dt * (vx * dUdx + vy * dUdy)

    # Update U
    U = np.copy(U_new)

    # Optional: Visualization during the loop
    if n % 50 == 0:
        plt.clf()
        plt.contourf(X, Y, U, levels=50, cmap='jet')
        plt.colorbar()
        plt.title(f"Time: {n * dt:.2f}")
        plt.pause(0.01)

# Final plot
plt.contourf(X, Y, U, levels=50, cmap='jet')
plt.colorbar()
plt.title("Final Solution")
plt.show()
