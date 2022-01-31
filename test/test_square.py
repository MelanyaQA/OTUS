from OTUS.src.square import Square


def test_check_square_condition():
    square1 = Square(2)
    if square1.a * 4 == square1.perimetr:
        print('This is square!')
    else:
        raise ValueError('Фигура не является квадратом!')


def test_area_square():
    square3 = Square(3)
    assert square3.a ** 2 == square3.area




