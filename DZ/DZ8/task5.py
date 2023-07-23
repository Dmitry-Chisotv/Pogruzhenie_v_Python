"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов."""

__all__ = ['json_to_pickle']

import os
import json
import pickle

def json_to_pickle(directory):
    for file in os.listdir(directory):
        if file.endswith('.json'):
            json_file_path = os.path.join(directory, file)
            pickle_file_path = os.path.join(directory, file.replace('.json', '.pickle'))

            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

            with open(pickle_file_path, 'wb') as pickle_file:
                pickle.dump(data, pickle_file)

if __name__ == '__main__':
    directory_path = r"C:\Users\79199\Downloads\Lessons_Python\DZ\DZ8"
    json_to_pickle(directory_path)