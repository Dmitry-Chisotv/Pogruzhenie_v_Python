"""Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины"""


class NegativeValueError(Exception):
    def __init__(self, value_name, value):
        self.value_name = value_name
        self.value = value

    def __str__(self):
        return f"Ошибка: {self.value_name} не может быть отрицательным.\n" \
               f"Были введены значения: {self.value}"

class InvalidRectangleError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"InvalidRectangleError: {self.message}"

class Rectangle:
    def __init__(self, width: float, height: float = None):
        if not (isinstance(width, (int, float)) and (height is None or isinstance(height, (int, float)))):
            raise ValueError("Ширина и высота должны быть цифровыми значениями.")

        if width < 0 or (height is not None and height < 0):
            raise NegativeValueError("Ширина" if height is None else "Ширина и высота", (width, height))

        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        return (self.height + self.width) * 2

    def calc_area(self):
        return self.height * self.width

if __name__ == '__main__':
    # try:
    #     new_rect = Rectangle(8, -2)
    #     print(f'{new_rect.calc_area()=}')
    #     print(f'{new_rect.calc_perimeter()=}')
    # except NegativeValueError as e:
    #     print(e)

    # try:
    #     new_rect = Rectangle(8, "hello")
    #     print(f'{new_rect.calc_area()=}')
    #     print(f'{new_rect.calc_perimeter()=}')
    # except ValueError as e:
    #     print(e)
    #
    try:
        new_rect = Rectangle(8)
        print(f'{new_rect.calc_area()=}')
        print(f'{new_rect.calc_perimeter()=}')
    except NegativeValueError as e:
        print(e)

