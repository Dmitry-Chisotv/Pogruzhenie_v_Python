# Задача № 3
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

from random import randint

volume_backpack = 50
real_backpack_volume = 0

things = {'полотенца': 1, 'компас': 1, 'спички': 1, 'термос': 2, 'консервы': 5, 'кроссворд': 1, 'телефон':1, \
        'котелок': 3, 'матрас': 5, 'футболки': 1, 'зеркало': 1, 'огниво': 1, 'фонарь': 1, 'батарейки': 1, \
        'карту местности': 1, 'свисток': 1, 'перочиный нож': 1, 'пила': 2, 'шорты': 1, 'дрова': 5, 'хлеб': 2, \
        'мяч': 2, 'дождевик': 2, 'куртка': 2, 'палатка': 15, 'канат': 2, 'крупы': 5, 'спальный мешок': 7, \
        'надувная лодка': 10, 'штаны': 2, 'кроссовки': 4, 'бадминтон': 4}

real_backpack1 = dict()

while real_backpack_volume < volume_backpack:
    real_backpack = list(things.items())
    key,val = real_backpack[randint(0, len(real_backpack)-1)]
    real_backpack_volume += int(val)

    if real_backpack_volume > volume_backpack:
        real_backpack_volume -= int(val)

    elif real_backpack_volume == volume_backpack:
        real_backpack1[key] = val
        break

    else:
        real_backpack1[key] = val

print(real_backpack1, real_backpack_volume)
