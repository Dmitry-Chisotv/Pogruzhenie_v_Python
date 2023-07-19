"""Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""


__all__ = ['create_directory_if_not_exists', 'sort_files_by_type']

import os
import shutil

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def sort_files_by_type(source_directory):
    file_categories = {
        "videos": [".mp4", ".avi", ".mkv"],
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "texts": [".txt", ".pdf", ".docx"]
    }

    create_directory_if_not_exists(source_directory)

    for root, _, files in os.walk(source_directory):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()

            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    target_directory = os.path.join(source_directory, category)
                    create_directory_if_not_exists(target_directory)
                    source_file_path = os.path.join(root, file)
                    target_file_path = os.path.join(target_directory, file)

                    if not os.path.exists(target_file_path):
                        shutil.move(source_file_path, target_file_path)
                    break


if __name__ == '__main__':
    source_directory = "path/to/source/directory"
    sort_files_by_type(source_directory)






