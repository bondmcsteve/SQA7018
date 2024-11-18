import numpy as np

# Constants
gamma = 1.4
R = 8.314  # J/(mol*K)
M = 0.0288  # kg/mol
T0 = 302  # Initial temperature in K
lapse_rate = 6  # K/km (temperature lapse rate in Kelvin per kilometer)
theta = np.radians(12)  # Convert pitch angle to radians


# Define the acceleration function
def acceleration(t):
    return 2.198 + (2.842e-2) * t + (1.061e-3) * t ** 2


# Integration using the trapezoidal rule
def integrate_trapezoidal(y, dt):
    return np.cumsum((y[:-1] + y[1:]) / 2 * dt)


# Define function to calculate temperature at a given altitude
def temperature(z):
    return T0 - lapse_rate * z / 1000  # Convert lapse rate to K per meter


# Calculate speed of sound as a function of altitude z
def speed_of_sound(z):
    T = temperature(z)
    return np.sqrt(gamma * R * T / M)


# Simulation setup
time_end = 135.2  # Duration of stage-one burn in seconds
t = np.linspace(0, time_end, 1000)  # Time array
dt = t[1] - t[0]  # Time step

# Calculate velocity by integrating acceleration using trapezoidal integration
a_values = acceleration(t)
v_values = integrate_trapezoidal(a_values, dt)

# Calculate distance by integrating velocity using trapezoidal integration
distance_values = integrate_trapezoidal(v_values, dt)

# Final distance after stage-one burn
distance_at_burn_end = distance_values[-1]
print(f"Distance traveled by the rocket at the end of stage-one burn: {distance_at_burn_end:.2f} meters")

# Altitude and speed check for reaching Mach 1
mach_1_reached = False
for i in range(1, len(t)):
    # Calculate altitude based on the vertical component of velocity
    z = integrate_trapezoidal(v_values * np.sin(theta), dt)[i]
    rocket_speed = v_values[i]
    sound_speed = speed_of_sound(z)

    # Check if rocket speed matches or exceeds speed of sound
    if rocket_speed >= sound_speed and not mach_1_reached:
        mach_1_time = t[i]
        mach_1_altitude = z
        mach_1_reached = True
        break

print(f"Rocket reaches Mach 1 at time: {mach_1_time:.2f} seconds")
print(f"Altitude at Mach 1: {mach_1_altitude:.2f} meters")
