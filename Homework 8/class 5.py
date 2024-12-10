import math
import time
from functools import wraps

# Decorator to time a method
def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        print(f"{method.__name__} executed in {(end_time - start_time):.6f} seconds")
        return result
    return timed

class Particle:
    def __init__(self, position, velocity):
        self.position = position  # (x, y, z)
        self.velocity = velocity  # (vx, vy, vz)

    def move(self, dt):
        self.position = tuple(p + v * dt for p, v in zip(self.position, self.velocity))

    @staticmethod
    def distance(p1, p2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1.position, p2.position)))

class ChargedParticle(Particle):
    def __init__(self, position, velocity, charge):
        super().__init__(position, velocity)
        self.charge = charge

    def electric_field(self, other):
        k = 8.9875517873681764e9  # Coulomb's constant
        r_vec = tuple(o - s for s, o in zip(self.position, other.position))
        r_mag = math.sqrt(sum(r ** 2 for r in r_vec))
        if r_mag == 0:
            return (0, 0, 0)
        e_field = tuple(k * other.charge * r / r_mag ** 3 for r in r_vec)
        return e_field

    @timeit
    def interact(self, other):
        if isinstance(other, ChargedParticle):
            e_field = self.electric_field(other)
            force = tuple(self.charge * e for e in e_field)
            # Assuming unit mass for simplicity
            acceleration = force  # F = ma, m=1
            self.velocity = tuple(v + a for v, a in zip(self.velocity, acceleration))

class MagneticParticle(Particle):
    def __init__(self, position, velocity, magnetic_moment):
        super().__init__(position, velocity)
        self.magnetic_moment = magnetic_moment  # (mx, my, mz)

    def magnetic_field(self, other):
        # Simplified magnetic field calculation
        mu0 = 4 * math.pi * 1e-7  # Permeability of free space
        r_vec = tuple(s - o for s, o in zip(self.position, other.position))
        r_mag = math.sqrt(sum(r ** 2 for r in r_vec))
        if r_mag == 0:
            return (0, 0, 0)
        factor = mu0 / (4 * math.pi * r_mag ** 3)
        m = other.magnetic_moment
        B = tuple(factor * (3 * r * sum(m_i * r_i for m_i, r_i in zip(m, r_vec)) / r_mag ** 2 - m_i) for r, m_i in zip(r_vec, m))
        return B

    @timeit
    def interact(self, other):
        if isinstance(other, MagneticParticle):
            b_field = self.magnetic_field(other)
            # Simplified Lorentz force: F = m x B
            force = (
                self.magnetic_moment[1] * b_field[2] - self.magnetic_moment[2] * b_field[1],
                self.magnetic_moment[2] * b_field[0] - self.magnetic_moment[0] * b_field[2],
                self.magnetic_moment[0] * b_field[1] - self.magnetic_moment[1] * b_field[0],
            )
            # Assuming unit mass for simplicity
            acceleration = force  # F = ma, m=1
            self.velocity = tuple(v + a for v, a in zip(self.velocity, acceleration))

# Create instances
cp1 = ChargedParticle(position=(0, 0, 0), velocity=(0, 0, 0), charge=1e-6)
cp2 = ChargedParticle(position=(0, 0, 0.1), velocity=(0, 0, 0), charge=-1e-6)

mp1 = MagneticParticle(position=(1, 0, 0), velocity=(0, 0, 0), magnetic_moment=(1, 0, 0))
mp2 = MagneticParticle(position=(1, 0.1, 0), velocity=(0, 0, 0), magnetic_moment=(0, 1, 0))

# Make them interact
cp1.interact(cp2)
mp1.interact(mp2)

# Move particles
dt = 0.01  # time step
cp1.move(dt)
cp2.move(dt)
mp1.move(dt)
mp2.move(dt)

# Print new positions and velocities
print("Charged Particles:")
print(f"cp1 position: {cp1.position}, velocity: {cp1.velocity}")
print(f"cp2 position: {cp2.position}, velocity: {cp2.velocity}")

print("Magnetic Particles:")
print(f"mp1 position: {mp1.position}, velocity: {mp1.velocity}")
print(f"mp2 position: {mp2.position}, velocity: {mp2.velocity}")
