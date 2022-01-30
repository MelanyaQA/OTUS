from OTUS.src.figure import Figure
from math import pi

class Circle(Figure):
    name = 'circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius




