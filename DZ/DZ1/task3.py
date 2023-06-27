# Задача №3
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря

EVERY_FOUR = 4
HUNDRED = 100
FOURHUNDRED = 400

year = int(input("Введите год: "))
if year % EVERY_FOUR != 0 or year % HUNDRED == 0 and year % FOURHUNDRED != 0:
    print(f'Год {year} являтся обычным')
else:
    print(f'Год {year} являтся высокосным')
