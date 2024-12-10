# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:33:00 2024

@author: User
"""

class RigidBody:
    def __init__(self, mass):
        self.mass = mass

    def moment_of_inertia(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


class SolidSphere(RigidBody):
    def __init__(self, mass, radius):
        super().__init__(mass)
        self.radius = radius

    def moment_of_inertia(self):
        I = (2/5) * self.mass * self.radius ** 2
        return I


class SolidCylinder(RigidBody):
    def __init__(self, mass, radius):
        super().__init__(mass)
        self.radius = radius

    def moment_of_inertia(self):
        I = (1/2) * self.mass * self.radius ** 2
        return I


class RectangularPrism(RigidBody):
    def __init__(self, mass, a, b):
        super().__init__(mass)
        self.a = a  # Side length a
        self.b = b  # Side length b

    def moment_of_inertia(self):
        I = (1/3) * self.mass * (self.a ** 2 + self.b ** 2)
        return I


# Create instances
sphere = SolidSphere(mass=5.0, radius=0.3)        # Mass in kg, radius in meters
cylinder = SolidCylinder(mass=5.0, radius=0.3)
prism = RectangularPrism(mass=5.0, a=0.4, b=0.5)  # a and b in meters

# Compute and print moments of inertia
print("Moments of Inertia:")
print(f"Solid Sphere: {sphere.moment_of_inertia():.4f} kg·m²")
print(f"Solid Cylinder: {cylinder.moment_of_inertia():.4f} kg·m²")
print(f"Rectangular Prism: {prism.moment_of_inertia():.4f} kg·m²")
