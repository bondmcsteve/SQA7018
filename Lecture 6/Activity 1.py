'''
reading and processing large log files 
line-by-line without loading the entire file into memory.
'''


def read_large_file(file_path):
    """A generator function to read a large file line-by-line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def count_occupied_orbitals_logs(file_path):
    """Count the number of lines containing the word 'Occup= 2.0' in a large log file."""
    Occup = 0
    for line in read_large_file(file_path):
        if 'Occup= 2.0' in line:
            Occup += 1
    return Occup


log_file_path = 'BK713-BK726-BK77.molden'  # Replace with your actual log file path
print(f"Number of 'Occupied' Orbitals: {count_occupied_orbitals_logs(log_file_path)}")

'''
Generators are useful for real-time data acquisition from sensors, 
which often produce a continuous stream of data that needs to be processed on the fly
Generator allows for real-time processing and response without overwhelming memory.
'''

import random
import time


def sensor_data_stream():
    """A generator that simulates real-time sensor data streaming."""
    while True:
        # Simulating a sensor reading
        yield random.uniform(20.0, 25.0)
        time.sleep(0.5)  # Simulate data acquisition delay


# Using the generator to process data

for reading in sensor_data_stream():
    print(f"Sensor Reading: {reading:.2f} °C")
    # Break or perform some analysis conditionally
    if reading > 24.5:
        print("Threshold exceeded! Taking action.")
        break

'''The generator simulate_particle_motion produces the position of a particle over time, 
simulating its motion step-by-step. This approach is useful for modeling physical systems 
without storing large arrays of data'''


def simulate_particle_motion(initial_position, velocity, time_steps, dt):
    """A generator to simulate particle motion under uniform velocity."""
    position = initial_position
    for _ in range(time_steps):
        yield position
        position += velocity * dt


initial_position = 0.0
velocity = 2.5  # m/s
time_steps = 10
dt = 0.1  # time step in seconds

for position in simulate_particle_motion(initial_position, velocity, time_steps, dt):
    print(f"Particle Position: {position:.2f} m")