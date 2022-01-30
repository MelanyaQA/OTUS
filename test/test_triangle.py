from OTUS.src.triangle import Triangle
from OTUS.src.square import Square


def test_check_triangle_condition():
    tr1 = Triangle(4, 2, 5)
    if tr1.a + tr1.b > tr1.c and tr1.b + tr1.c > tr1.a and tr1.a + tr1.c > tr1.b:
        print('This is triangle')
    else:
        raise ValueError('Введеные данные - неверные. Данная фигура - не является треугольником')

def test_perimetr():
    tr2 = Triangle(5, 3, 4)
    assert tr2.a + tr2.b + tr2.c == tr2.perimetr_triangle()


def test_area():
    test_triangle1 = Triangle(4, 3, 5)
    print(Triangle.name, 'area =', test_triangle1.area_triangle())

def test_add_tr():
    tr3 = Triangle(10, 5, 4)
    square3 = Square(2, 2, 2, 2)
    return tr3.area_triangle() + square3.area_square()






