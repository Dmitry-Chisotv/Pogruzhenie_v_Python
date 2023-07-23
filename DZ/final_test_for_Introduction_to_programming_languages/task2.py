"""Напишите программу, которая спирально заполнит числами от 1 до 16 двумерный массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

Указание:
При заполнении массива использовать циклы."""


def spiral_fill(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    x, y = 0, 0
    num = 1

    for i in range(n * n):
        matrix[x][y] = num
        num += 1

        dx, dy = directions[direction_idx]
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < n and 0 <= new_y < n) or matrix[new_x][new_y] != 0:
            direction_idx = (direction_idx + 1) % 4
            dx, dy = directions[direction_idx]
            new_x, new_y = x + dx, y + dy

        x, y = new_x, new_y

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:02d}" for num in row))

if __name__ == '__main__':
    matrix = spiral_fill(4)
    print_matrix(matrix)




