from OTUS.src.figure import Figure
from math import pi

class Circle(Figure):
    name = 'circle'

    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return pi * (self.radius ** 2)

    def perimeter_circle(self):
        return 2 * pi * self.radius



