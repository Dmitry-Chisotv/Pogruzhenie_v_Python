"""Задача №2
Напишите функцию принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def task_2(**kwargs):
    dict_for_task = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        dict_for_task[value] = key
    return dict_for_task


def hashable(obj):
   try:
       hash(obj)
       return True
   except TypeError:
       return False


dict_for_task = task_2(arg1=300, arg2='text', arg3='Byby', arg4=5.15, arg6=True)
print(dict_for_task)

