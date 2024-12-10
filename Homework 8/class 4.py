import math

class Planet:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    # Property for mass
    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if value <= 0:
            raise ValueError("Mass must be a positive number.")
        self._mass = value

    # Property for radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    # Static method for gravitational constant
    @staticmethod
    def gravitational_constant():
        return 6.67430e-11  # N·m²/kg²

    # Method to compute surface gravity
    def surface_gravity(self):
        G = self.gravitational_constant()
        return G * self.mass / self.radius ** 2

    # Class method to create a Planet from density
    @classmethod
    def from_density(cls, density, radius):
        if density <= 0:
            raise ValueError("Density must be a positive number.")
        volume = (4/3) * math.pi * radius ** 3
        mass = density * volume
        return cls(mass, radius)

# Create an instance with given mass and radius
earth = Planet(mass=5.97e24, radius=6.371e6)

# Create an instance from density
earth_density = Planet.from_density(density=5514, radius=6.371e6)

# Print out the surface gravity of both planets
print(f"Surface gravity (from mass): {earth.surface_gravity():.2f} m/s²")
print(f"Surface gravity (from density): {earth_density.surface_gravity():.2f} m/s²")
