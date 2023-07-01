# Задача №2
#  Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей.
# Для проверки своего кода используйте модуль fractions.
from math import gcd

frac_1 = str(input("Введите первую дробь вида “a/b”: ")).split("/")
frac_2 = str(input("Введите вторую дробь вида “a/b”: ")).split("/")

a = int(frac_1[0])
b = int(frac_1[1])
c = int(frac_2[0])
d = int(frac_2[1])

sum_chysl = a * d + c * b
prod_chysl = a * c
new_znam = b * d
sum_del = gcd(sum_chysl, new_znam)
prod_del = gcd(prod_chysl, new_znam)

print(f'Сумма введенных дробей {int(sum_chysl/sum_del)}/{int(new_znam/sum_del)}, их произведение {int(prod_chysl/prod_del)}/{int(new_znam/prod_del)}')

import fractions
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print(f'Проверка суммы введенных дробей {(f1 + f2)}, их произведение {(f1 * f2)}')
