"""Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов."""

__all__ = ['count_f', 'logger', 'check_parametr', 'gess_number']

from typing import Callable
from random import randint
import os
import json
from functools import wraps

def count_f(num: int = 1):
    def deco(func: Callable):
        results = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco

def logger(func: Callable):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        json_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1)
        return result

    return wrapper

def check_parametr(func: Callable):
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT = 10

    @wraps(func)
    def wrapper(number: int, count: int, *args, **kwargs):
        if number > MAX_NUM or number < MIN_NUM:
            number = randint(MIN_NUM, MAX_NUM)
        if count > MAX_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)
        result = func(number, count, *args, **kwargs)

        return result

    return wrapper

@count_f(3)
@check_parametr
@logger
def gess_number(number: int, count: int) -> Callable[[], None]:
    for i in range(1, count + 1):
        print(f'Попытка # {i}')
        num_input = int(input('Введите число: '))
        if num_input == number:
            print(f'Вы угадали! Загаданное число - {number}')
            break
        elif num_input < number:
            print(f'Введенное число {num_input} меньше загаданного числа')
        else:
            print(f'Введенное число {num_input} больше загаданного числа')

if __name__ == '__main__':
    game = gess_number(25, 5)
    print(game)