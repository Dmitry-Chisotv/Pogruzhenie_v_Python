"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции."""

__all__ = ['pad_zeros', 'capitalize_first_letter', 'generate_hash', 'process_csv']

import csv
import json


def pad_zeros(num, length):
    return str(num).zfill(length)


def capitalize_first_letter(name):
    return name.capitalize()


def generate_hash(name, identifier):
    return hash(name + str(identifier))


def process_csv(input_file, output_file):
    data = []

    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  

        for row in reader:
            identifier = pad_zeros(int(row[0]), 10)
            name = capitalize_first_letter(row[2])
            level = int(row[0])
            hash_value = generate_hash(name, identifier)

            json_data = {
                header[0]: level,
                header[1]: identifier,
                header[2]: name,
                'hash': hash_value
            }

            data.append(json_data)

    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)


if __name__ == '__main__':
    input_file = 'task3_my_csv.csv'
    output_file = 'task3_my_csv.json'
    process_csv(input_file, output_file)