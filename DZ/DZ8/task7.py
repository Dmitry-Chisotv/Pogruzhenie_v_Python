"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку"""

__all__ = ['csv_to_pickle_string']

import csv
import pickle

def csv_to_pickle_string(csv_file):
    data = []

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        for row in reader:
            data.append(dict(zip(headers, row)))

    pickle_string = pickle.dumps(data)

    return pickle_string


if __name__ == '__main__':
    csv_file_path = r"C:\Users\79199\Downloads\Lessons_Python\DZ\DZ8\task6_my.csv"
    pickle_string = csv_to_pickle_string(csv_file_path)
    print(pickle_string)