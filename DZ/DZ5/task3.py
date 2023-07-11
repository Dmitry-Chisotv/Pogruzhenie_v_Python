""""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def numbers_gen(numbers_count: int):
    num1 = 0
    num2 = 1
    count = 1
    # yield num1, num2
    yield num1
    yield num2

    while count <= numbers_count:
        num = num1 + num2
        count +=1
        num1, num2 = num2, num
        yield num


if __name__ == '__main__':
    for number in numbers_gen(10):
        print(number, end=' ')
