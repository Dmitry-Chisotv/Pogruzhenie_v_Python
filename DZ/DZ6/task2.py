"""Задача №2
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки."""

import random
__all__ = ['are_queens_attacking_each_other', 'generate_random_queens_arrangement', 'main']


def are_queens_attacking_each_other(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def generate_random_queens_arrangement():
    queens = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    return queens


def main():
    # if are_queens_attacking_each_other(queens) == True:
    #     print(f'Комбинация {queens} - Истина')
    #
    # else:
    #     print(f'Комбинация {queens} - Ложь')

    count = 0

    while count < 3:
        queens = generate_random_queens_arrangement()
        if are_queens_attacking_each_other(queens) == True:
            count += 1
            print(f'Успешно! {queens}')

        # else:
        #     print(f'fake + {queens}')


if __name__ == "__main__":
    # queens = [(3, 5), (7, 8), (8, 2), (5, 1), (4, 3), (1, 4), (6, 6), (2, 7)]
    # queens = [(7, 6), (6, 8), (5, 1), (4, 5), (3, 7), (8, 3), (2, 2), (1, 4)]
    # queens = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]
    # queens = [(2, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]
    # queens = [(8, 4), (2, 6), (1, 3), (5, 5), (3, 2), (7, 8), (4, 7), (6, 1)]
    print(main())


