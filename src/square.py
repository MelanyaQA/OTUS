from OTUS.src.figure import Figure
from OTUS.src.rectangle import Rectangle


class Square(Rectangle, Figure):
    name = 'square'

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @property
    def perimetr(self):
        return self.a * 4

    @property
    def area(self):
        return self.a ** 2
