from OTUS.src.figure import Figure


class Square(Figure):
    name = 'square'

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr_square(self):
        return self.a * 4

    def area_square(self):
        return self.a ** 2


