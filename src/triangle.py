from OTUS.src.figure import Figure
from OTUS.src.square import Square

class Triangle(Figure):
    name = 'triangle'
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimetr(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2

        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s

    def add_area_tr(self):
         return Triangle.area + Square.area






