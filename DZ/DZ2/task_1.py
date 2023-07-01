# Задача №1
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input("Введите целое число: "))

SYSTEM = 16

def dec_to_n(number: int, SYSTEM: int) -> str:
    tmp_num: int = number
    new_num: str = ''

    while tmp_num != 0:
        mod: int = int(tmp_num % SYSTEM)
        if mod < 10:
            mod = str(mod)
        elif mod == 10:
            mod = str('a')
        elif mod == 11:
            mod = str('b')
        elif mod == 12:
            mod = str('c')
        elif mod == 13:
            mod = str('d')
        elif mod == 14:
            mod = str('e')
        elif mod == 15:
            mod = str('f')

        new_num = mod + new_num
        tmp_num //= SYSTEM

    return new_num

num2: str = dec_to_n(num, SYSTEM)

print(f'Число {num} в шестнадцатеричной системе будет равно - {num2}')
print(f'Проверка числа {num} через функцию hex - {hex(num)}')
