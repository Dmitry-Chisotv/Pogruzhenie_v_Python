"""Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""

__all__ = ['generate_random_string', 'generate_files_in_directory']


import os
import random
import string

def generate_random_string(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def generate_files_in_directory(directory, num_files=10, file_extension=".txt"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    existing_files = set(os.listdir(directory))
    generated_files = []

    for i in range(num_files):
        file_name = generate_random_string() + file_extension
        while file_name in existing_files:
            file_name = generate_random_string() + file_extension

        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            pass

        generated_files.append(file_name)
        existing_files.add(file_name)

    print(f"{num_files} files generated in directory: {directory}")
    print("Generated files:", generated_files)


if __name__ == '__main__':
    generate_files_in_directory("path/to/directory", num_files=5, file_extension=".txt")
















