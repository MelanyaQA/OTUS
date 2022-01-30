
from OTUS.src.rectangle import Rectangle
from OTUS.src.circle import Circle

def test_check_rectangle_condition():
    rect1 = Rectangle(2, 4, 2, 4)
    if rect1.a == rect1.c or rect1.b == rect1.d:
        print('This is rectangle!')
    else:
        raise ValueError('Введены неверные данные. Фигура не является прямоугольником')

def test_area_rectangle():
    rect2 = Rectangle(3, 4, 3, 4)
    if rect2.a != rect2.b:
        assert rect2.a * rect2.b == rect2.area_rectangle()

def test_perimetr_rectangle():
    rect3 = Rectangle(4, 3, 4, 3)
    if rect3.a != rect3.b:
        assert (rect3.a + rect3.b) * 2

def test_add_area_rect():
    rect4 = Rectangle(3, 5, 3, 5)
    circle4 = Circle(3)
    return rect4.area_rectangle() + circle4.area_circle()

