"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""

cycles = 20
digest = 98
cars = 45
myth = 321
s = 23

def replace_variables(old_name, new_name, value):
    if old_name.endswith('s') and len(old_name) > 1:
        globals()[new_name] = old_name[:-1]
        print(f' Новое название переменной {new_name} которое равно', end=' ')
        new_name = value
        print(f' {new_name} \n Старая переменная {old_name} принимает значение ', end=' ')
        old_name = None
        print(old_name)
    else:
        print(f' Переменная {old_name} сохраняет значение {value}')

replace_variables('cycles', 'cycles'[:-1], cycles)
replace_variables('digest', 'digest', digest)
replace_variables('cars', 'cars'[:-1], cars)
replace_variables('myth', 'myth', myth)
replace_variables('s', 's', s)

