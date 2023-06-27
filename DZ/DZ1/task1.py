# Задача №1*
# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPS = 10
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1

while count <= ATTEMPS:
    print('Попытка ', count)
    count +=1

    num_of_user = int(input(f'Введите число между {LOWER_LIMIT} и {UPPER_LIMIT}: '))
    if num_of_user != num:
        if num_of_user > num:
            print(f'Введенное число {num_of_user} больше задуманного')
        elif num_of_user < num:
            print(f'Введенное число {num_of_user} меньше задуманного')
    else:
        break

else:
    print('Сожалею, попытки закончились')
    quit()

print('Поздравляю, было задумано число  ', num)
