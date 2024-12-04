import numpy as np

"""Declare class"""
class Barometric:
    def __init__(self, T):
        self.T = T
        self.g = 9.81
        self.R  = 8.314
        self.M = 0.02896
        self.p0 = 100.0

    def value(self, h):
        return self.p0 * np.exp(-self.M * self.g * h / (self.R * self.T))

class Barometric1:
    def __init__(self, T): # Values here are public
        self.T = T

    def value(self, h): # Values here are private
        g = 9.81; R = 9.314
        M = 0.02896; p0 = 100.0
        return p0 * np.exp(-M * g * h/ (R * self.T))

class Barometric2:
    def __init__(self, T):
        """"Fill up the codes here"""


from math import sin, exp, pi
from numpy import linspace


def make_table(f, tstop, n):
    for t in linspace(0, tstop, n):
        print(t, f(t))


def g(t):
    return sin(t) * exp(-t)


make_table(g, 2 * pi, 11)

b1 = Barometric(2469)
make_table(b1.value, 2 * pi, 11)