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

def replace_variables(name: str) -> str:
    if name.endswith('s') and len(name) > 1:
        new_name = name[:-1]
        print(new_name)
    elif name.endswith('s') and len(name) == 1:
        print(name)
    else:
        print(name)

if __name__ == "__main__":
    replace_variables('cycles')
    replace_variables('cycle')
    replace_variables('s')



# replace_variables('cycles', 'cycles'[:-1], cycles)
# replace_variables('digest', 'digest', digest)
# replace_variables('cars', 'cars'[:-1], cars)
# replace_variables('myth', 'myth', myth)
# replace_variables('s', 's', s)


