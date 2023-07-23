"""Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.


***Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов."""

__all__ = ['get_directory_size', 'traverse_directory', 'save_to_pickle', 'traverse_and_save', 'save_to_csv', 'save_to_json']


import os
import json
import csv
import pickle

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def traverse_directory(directory):
    data = []

    for dirpath, dirnames, filenames in os.walk(directory):
        dir_size = get_directory_size(dirpath)

        for dirname in dirnames:
            obj_info = {
                'path': os.path.join(dirpath, dirname),
                'type': 'directory',
                'size_bytes': dir_size,
                'parent_directory': dirpath
            }
            data.append(obj_info)

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)

            obj_info = {
                'path': file_path,
                'type': 'file',
                'size_bytes': file_size,
                'parent_directory': dirpath
            }
            data.append(obj_info)

    return data

def save_to_json(data, output_file):
    with open(output_file + '.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

def save_to_csv(data, output_file):
    with open(output_file + '.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, output_file):
    with open(output_file + '.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def traverse_and_save(directory, output_file_prefix):
    data = traverse_directory(directory)
    save_to_json(data, output_file_prefix)
    save_to_csv(data, output_file_prefix)
    save_to_pickle(data, output_file_prefix)


if __name__ == '__main__':
    directory_path = r"C:\Users\79199\Downloads\Lessons_Python\DZ\DZ8"
    output_file_prefix = "result"
    traverse_and_save(directory_path, output_file_prefix)





