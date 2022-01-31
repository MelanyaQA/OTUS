from OTUS.src.figure import Figure
from OTUS.src.rectangle import Rectangle


class Square(Rectangle, Figure):
    name = 'square'

    def __init__(self, a):
        self.a = a


    @property
    def perimetr(self):
        return self.a * 4

    @property
    def area(self):
        return self.a ** 2
