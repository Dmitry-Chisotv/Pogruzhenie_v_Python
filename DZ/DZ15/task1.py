#  Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Добавить логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging
from math import gcd

logging.basicConfig(level=logging.ERROR, filename='log1.log', encoding='utf-8')
log = logging.getLogger(__name__)


def calculate(frac_1: str, frac_2: str):
    try:
        frac_3 = str(frac_1).split("/")
        frac_4 = str(frac_2).split("/")

        a = int(frac_3[0])
        b = int(frac_3[1])
        c = int(frac_4[0])
        d = int(frac_4[1])
        sum_chysl = a * d + c * b
        prod_chysl = a * c
        new_znam = b * d
        sum_del = gcd(sum_chysl, new_znam)
        prod_del = gcd(prod_chysl, new_znam)

        if a == 0 or b == 0 or c == 0 or d == 0:
            log.error('0! НЕ ДОПУСТИМО ДЛЯ УСЛОВИЙ ЗАДАЧИ')
            return None
        else:
            return print(f'Сумма введенных дробей {int(sum_chysl / sum_del)}/{int(new_znam / sum_del)}, '
                         f'их произведение {int(prod_chysl / prod_del)}/{int(new_znam / prod_del)}')

    except ValueError as e:
        log.error('Неверный формат строки!')
        return None


def pars():
    parser = argparse.ArgumentParser(description='Calculate fractions.')
    parser.add_argument('frac1', type=str, help='First fraction in the format "a/b"')
    parser.add_argument('frac2', type=str, help='Second fraction in the format "a/b"')
    args = parser.parse_args()

    frac_1 = args.frac1
    frac_2 = args.frac2

    result = calculate(frac_1, frac_2)
    if result is not None:
        print(result)


if __name__ == '__main__':
    print(pars())
