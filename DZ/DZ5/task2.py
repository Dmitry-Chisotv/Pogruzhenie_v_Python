"""Напишите однострочный генератор словаря,
который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии
 в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


colleagues = ['Nick', 'Ben', 'Dave']
salary = [200_000, 300_000, 400_000]
bonus_list = ['25%', '15%', '10%']

import decimal

money_dict = {name: staff * decimal.Decimal(bonus[:-1]) / 100
    for name, staff, bonus in zip(colleagues, salary, bonus_list)}

print(money_dict)



