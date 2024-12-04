import numpy as np

class Droplet:
    def __init__(self, dropvol):
        self.volume = dropvol

    def get_radius(self):
        return ((3/4) * (self.volume / np.pi)) ** (1/3)

    def __str__(self):
        return f'Radius calculates using r = ((3/4) * (self.volume / np.pi)) ** (1/3) ; radius = {self.get_radius()}'

    def __add__(self, other):
        return (Droplet(self.volume + other.volume))

    def __gt__(self, other):
        return f'True,ge'

    def __lt__(self, other):
        return f'True,le'

drop1 = Droplet(1)
drop2 = Droplet(2)

print(drop1.get_radius())
print(drop1)

print(drop1 < drop2)
