from OTUS.src.figure import Figure
from OTUS.src.circle import Circle

class Rectangle(Figure):
    name = 'rectangle'
    def __init__(self, a, b):
        self.a = a
        self.b = b


    @property
    def area(self):
        if self.a != self.b:
            return self.a * self.b

    @property
    def perimetr(self):
        if self.a != self.b:
            return (self.a + self.b) * 2

    def add_area_rect(self):
        return Rectangle.area + Circle.area


