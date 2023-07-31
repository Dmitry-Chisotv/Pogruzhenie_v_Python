"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений."""


class Rectangle:
    """Added of new class for Rectangle"""
    def __init__(self, width: float, height: float = None):
        """Added parameters width and height."""
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimetr(self):
        """Calculated of Perimetr of the Rectangle."""
        return (self.height + self.width) * 2

    def calc_area(self):
        """Calculated of Area of the Rectangle."""
        return self.height * self.width

    def __add__(self, other):
        """Calculated of new Perimetr and new sides of the biggest Rectangle."""
        perimetr = self.calc_perimetr() + other.calc_perimetr()
        width = self.width + other.width
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """Calculated of new Perimetr and new sides of the small Rectangle."""
        if self.calc_perimetr() < other.calc_perimetr():
            self, other = other, self
        perimetr = self.calc_perimetr() - other.calc_perimetr()
        width = abs(self.width - other.width)
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        """Printed results of the actions."""
        return f'Новый периметр =  {self.calc_perimetr()}, длинна = {self.width}, высота = {self.height}'


if __name__ == '__main__':
    new_rect = Rectangle(10, 20)
    # print(f'{new_rect.calc_area()=}')
    # print(f'{new_rect.calc_perimetr()=}')

    new_square = Rectangle(5)
    # print(f'{new_rect.calc_area()=}')
    # print(f'{new_rect.calc_perimetr()=}')

    print(new_rect + new_square)
    print(new_rect - new_square)
    print(f'Документация класса: {Rectangle.__doc__ = }')
    print(f'Документация класса: {new_square.__init__.__doc__ = }')
    print(f'Документация класса: {new_rect.__doc__ = }')
    print(f'Документация класса: {new_square.calc_perimetr.__doc__ = }')
    print(f'Документация класса: {new_rect.__add__.__doc__ = }')
    print(f'Документация класса: {new_square.__sub__.__doc__ = }')
    print(f'Документация класса: {new_square.__str__.__doc__ = }')


















