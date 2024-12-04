import numpy as np

class RegularPolygon:
    def __init__(self, num_sides, side_length):
        self._num_sides = num_sides
        self._side_length = side_length

    @property
    def num_sides(self):
        return(self._num_sides)

    @property
    def side_length(self):
        return(self._side_length)

# Defining the Triangle class
class Triangle(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(3, side_length)

    @property
    def area(self):
        return ((np.sqrt(3) * self.side_length**2) / 4)

    @property
    def perimeter(self):
        return self.side_length * self._num_sides

tri1 = Triangle(2)
print(tri1.area)
print(tri1.perimeter)