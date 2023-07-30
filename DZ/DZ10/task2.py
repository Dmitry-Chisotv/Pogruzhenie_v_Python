"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра."""

import json
import os

class UserManagement:
    def __init__(self, path: str):
        self.path = path
        self.tmp_set = set()
        self.my_dict = {}

    def load_data(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r', encoding='utf-8') as j:
                self.my_dict = json.load(j)
                for _, vol in self.my_dict.items():
                    self.tmp_set.update(vol.keys())
        else:
            self.my_dict = {i: {} for i in range(1, 8)}

    def add_user(self):
        while True:
            name = input('Введите ваше имя: ')
            id_num = input('Введите ваш id: ')
            level = int(input('Введите ваш уровень доступа (1-7): '))
            if id_num in self.tmp_set and self.my_dict[level].get(id_num) is None:
                continue
            self.tmp_set.update(id_num)
            self.my_dict[level].update({id_num: name})
            with open(self.path, 'w', encoding='utf-8') as j:
                json.dump(self.my_dict, j, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    user_manager = UserManagement('task2.json')
    user_manager.load_data()
    user_manager.add_user()







