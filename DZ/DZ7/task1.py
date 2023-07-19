"""Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""


__all__ = ['pad_number_with_zeros', 'get_file_extension', 'generate_unique_name', 'rename_files']

import os

def pad_number_with_zeros(number, num_digits):
    return str(number).zfill(num_digits)

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]

def generate_unique_name(directory, desired_name, num_digits, original_name_part, target_extension):
    i = 1
    while True:
        new_name = f"{desired_name}_{pad_number_with_zeros(i, num_digits)}_{original_name_part}{target_extension}"
        new_path = os.path.join(directory, new_name)
        if not os.path.exists(new_path):
            return new_name
        i += 1

def rename_files(directory, desired_name, num_digits, original_name_range, source_extension, target_extension, new_name_prefix=""):
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and get_file_extension(file) == source_extension:
            original_name_part = file[original_name_range[0]-1:original_name_range[1]]
            new_name = generate_unique_name(directory, desired_name, num_digits, original_name_part, target_extension)
            if new_name_prefix:
                new_name = f"{new_name_prefix}_{new_name}"
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)

            if file != new_name:
                os.rename(old_file_path, new_file_path)


if __name__ == '__main__':
    source_directory = "path/to/source/directory"
    desired_name = "new_file"
    num_digits = 3
    original_name_range = (3, 6)
    source_extension = ".txt"
    target_extension = ".renamed.docx"
    new_name_prefix = "custom_prefix"

    rename_files(source_directory, desired_name, num_digits, original_name_range, source_extension, target_extension, new_name_prefix)