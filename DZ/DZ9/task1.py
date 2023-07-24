"""Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.

Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса"""

__all__ = ['quadratic_roots', 'generate_csv_file', 'find_roots_with_csv', 'save_to_json']


import math
import csv
import random
import json

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

def generate_csv_file(file_path, rows):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

def find_roots_with_csv(func):
    def wrapper(file_path):
        with open(file_path, newline='') as csv_file:
            reader = csv.reader(csv_file)
            results = []
            for row in reader:
                a, b, c = map(int, row)
                root1, root2 = func(a, b, c)
                result_dict = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'root1': root1,
                    'root2': root2
                }
                results.append(result_dict)
            return results
    return wrapper

def save_to_json(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        with open('results.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
            # json_file.write('\n')
        return results
    return wrapper

if __name__ == "__main__":
    csv_file_path = 'data.csv'
    generate_csv_file(csv_file_path, 100)


    @save_to_json
    @find_roots_with_csv
    def quadratic_roots_from_csv(a, b, c):
        return quadratic_roots(a, b, c)

    results = quadratic_roots_from_csv(csv_file_path)
    print(results)





