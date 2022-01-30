from OTUS.src.square import Square


def test_check_square_condition():
    square1 = Square(2, 2, 2, 2)
    if square1.a == square1.b == square1.c == square1.d:
        print('This is square!')
    else:
        raise ValueError('Фигура не является квадратом!')

def test_perimetr_square():
    square2 = Square(4, 4, 4, 4)
    assert square2.a * 4 == square2.perimetr

def test_area_square():
    square3 = Square(2, 2, 2, 2)
    assert square3.a ** 2 == square3.area




