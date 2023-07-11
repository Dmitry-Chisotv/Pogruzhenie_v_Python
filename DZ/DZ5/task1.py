"""Напишите функцию, которая принимает на вход строку
— абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла."""


def separate_way(str):
    tmp = text.split('\\')[-1]
    c = text.split('.')[-1]
    b = tmp.split('.')[0]
    a = text.split(tmp)[0]
    res = (a, b, c)
    return res


if __name__ == '__main__':
    text = 'C:\ Users\9199\Downloads\way.avi'
    print(separate_way(text))





