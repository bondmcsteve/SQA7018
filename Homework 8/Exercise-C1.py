import numpy as np

class Particle:
    """Class declaration for input using init"""
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.dt = 0.001

    #Note : We also pass the
    def ForceOnParticle(self, force):
        """Method of applying F=ma equation to find acceleration acting on the particle"""
        acceleration = [f / self.mass for f in force] # Use list comprehension to iterate through all vector components
        """Finding new velocity after force acting on the particle"""
        self.velocity = [v + (a * self.dt) for v,a in zip(self.velocity, acceleration)]

    def PositionUpdate(self):
        """Updates the position of the particle, assume dt = 0.001"""
        position_update = [pos + (v * self.dt) for pos, v in zip(self.position, self.velocity)]


"""Subclass ChargedParticle initialization"""
class ChargedParticle(Particle):
    """Attribute initialization"""
    k_e = 8.9875517873681764e9
    def __init__(self, position, velocity, mass, ParticleCharge):
        super().__init__(position, velocity, mass)
        self.charge = ParticleCharge

    def ElectricForce(self, other):
        """"Electric force due to particles are given as (q1q0/(4*pi*permittivity))* r_vector/r_norm^3 or we can use Coulomb constant to represent 1/4*pi*permittivity"""

        r_vector = [other_pos - self_p for other_pos, self_pos in zip(other.position, self.position)]
        r_mag = (sum(VectorComponent ** 2 for VectorComponent in r_vector)) ** 0.5
        r_UnitVector = [vector / magnitude for vector, magnitude in zip(r_vector, r_mag)]

        """Calculating the force acting on a particle"""
        force = [ChargedParticle.k_e * self.charge * other.charge * UnitVector / (r_mag**2) for UnitVector in r_UnitVector]

        return force

