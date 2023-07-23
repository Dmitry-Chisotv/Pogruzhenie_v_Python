""""Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла."""

__all__ = ['pickle_to_csv']

import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):

    with open(pickle_file, 'rb') as pkl_file:
        data = pickle.load(pkl_file)

    headers = list(data[0].keys())

    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    pickle_file_path = r"C:\Users\79199\Downloads\Lessons_Python\DZ\DZ8\task3_my_csv.pickle"
    csv_file_path = r"C:\Users\79199\Downloads\Lessons_Python\DZ\DZ8\task6_my.csv"
    pickle_to_csv(pickle_file_path, csv_file_path)