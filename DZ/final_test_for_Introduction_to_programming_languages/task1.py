"""Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2"""


def sort_rows_in_descending_order(matrix):
    sorted_matrix = []
    for row in matrix:
        sorted_row = sorted(row, reverse=True)
        sorted_matrix.append(sorted_row)
    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(num) for num in row))

matrix = [
[1, 4, 7, 2],
[5, 9, 2, 3],
[8, 4, 2, 4]
]
sorted_matrix = sort_rows_in_descending_order(matrix)
print_matrix(sorted_matrix)