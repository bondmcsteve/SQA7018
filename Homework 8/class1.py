class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position  # Position vector [x, y, z]
        self.velocity = velocity  # Velocity vector [vx, vy, vz]
        self.mass = mass

    def apply_force(self, force, dt):
        # F = m * a => a = F / m
        acceleration = [f / self.mass for f in force]
        # Update velocity: v = v + a * dt
        self.velocity = [v + a * dt for v, a in zip(self.velocity, acceleration)]

    def update_position(self, dt):
        # Update position: x = x + v * dt
        self.position = [p + v * dt for p, v in zip(self.position, self.velocity)]

    def __str__(self):
        return f"Particle(position={self.position}, velocity={self.velocity}, mass={self.mass})"


class ChargedParticle(Particle):
    k_e = 8.9875517873681764e9  # Coulomb's constant in N·m²/C²

    def __init__(self, position, velocity, mass, charge):
        super().__init__(position, velocity, mass)
        self.charge = charge  # Charge in Coulombs

    def electric_force(self, other):
        # Calculate the electric force exerted on this particle by another charged particle
        r_vector = [other_p - self_p for self_p, other_p in zip(self.position, other.position)]
        r_squared = sum(comp ** 2 for comp in r_vector)
        if r_squared == 0:
            raise ValueError("Particles are at the same position.")
        r_magnitude = r_squared ** 0.5
        force_magnitude = ChargedParticle.k_e * self.charge * other.charge / r_squared
        # Force vector: F = (force_magnitude) * (r_vector / r_magnitude)
        force = [force_magnitude * (comp / r_magnitude) for comp in r_vector]
        return force

    def __str__(self):
        return (f"ChargedParticle(position={self.position}, velocity={self.velocity}, "
                f"mass={self.mass}, charge={self.charge})")


# Create two ChargedParticle instances
particle1 = ChargedParticle(position=[0.0, 0.0, 0.0],
                            velocity=[0.0, 0.0, 0.0],
                            mass=1.0,
                            charge=1e-6)  # 1 μC

particle2 = ChargedParticle(position=[0.01, 0.0, 0.0],  # 1 cm apart
                            velocity=[0.0, 0.0, 0.0],
                            mass=1.0,
                            charge=-1e-6)  # -1 μC

# Compute the electric force between them
force_on_p1 = particle1.electric_force(particle2)
force_on_p2 = [-f for f in force_on_p1]  # Newton's third law

# Time step
dt = 0.01  # seconds

# Apply the force to each particle and update positions
particle1.apply_force(force_on_p1, dt)
particle2.apply_force(force_on_p2, dt)

particle1.update_position(dt)
particle2.update_position(dt)

# Show updated positions
print("After applying forces and updating positions:")
print(particle1)
print(particle2)
