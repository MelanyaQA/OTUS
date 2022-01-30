from OTUS.src.circle import Circle
from math import pi

def test_perimetr_circle():
    circle1 = Circle(3)
    assert 2 * pi * circle1.radius == circle1.perimeter_circle()

def test_area_circle():
    circle2 = Circle(5)
    assert pi * (circle2.radius ** 2) == circle2.area_circle()


