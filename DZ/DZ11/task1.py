""" Создайте класс Матрица. Добавьте методы для:
а. вывода на печать,
б. сравнения,
в. сложения,
г. *умножения матриц"""


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.validate_matrix()

    def validate_matrix(self):
        for row in self.data:
            if len(row) != self.cols:
                raise ValueError("Матрица должна иметь одинаковое количество значений в каждой строке")

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.data])

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Нельзя проводить операцию сложения, так как размеры матриц не совпадают")
        result_data = []
        for i in range(self.rows):
            result_data.append([self.data[i][j] + other.data[i][j] for j in range(self.cols)])
        return Matrix(result_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Нельзя проводить операцию умножения, "
                             "так как количество столбцов первой матрицы не равно количеству строк второй матрицы")
        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                elem = sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)])
                row.append(elem)
            result_data.append(row)
        return Matrix(result_data)

if __name__ == '__main__':
    matrix1_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2_data = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    matrix3_data = [[1, 2], [3, 4], [5, 6]]
    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)
    matrix3 = Matrix(matrix3_data)

    print("Сравнение матриц 1 и 2:", matrix1 == matrix2)
    print("Сравнение матриц 1 и 1:", matrix1 == matrix1)
    print("Сложение матриц 1 и 2:")
    sum_matrix = matrix1 + matrix2
    print(sum_matrix)
    print("Умножение матриц 1 и 3:")
    mul_matrix = matrix1 * matrix3
    print(mul_matrix)
