from OTUS.src.figure import Figure
from OTUS.src.circle import Circle

class Rectangle(Figure):
    name = 'rectangle'
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area_rectangle(self):
        if self.a != self.b:
            return self.a * self.b

    def perimetr_rectangle(self):
        if self.a != self.b:
            return (self.a + self.b) * 2

    def add_area_rect(self):
        return Rectangle.area_rectangle() + Circle.area_circle()

