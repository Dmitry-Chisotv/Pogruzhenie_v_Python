"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь."""

import math

class Circle:
    def __init__(self, r: float):
        self.radius = r

    def calc_perimetr(self):
        return 2 * math.pi * self.radius

    def calc_area(self):
        return  math.pi * self.radius ** 2


new_circle = Circle(3)
print(f'{new_circle.calc_area()=}')
print(f'{new_circle.calc_perimetr()=}')
