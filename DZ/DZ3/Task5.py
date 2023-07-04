# Задача № 5
# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

things_for_trip = dict()
alex = {'полотенце', 'компас', 'спички', 'термос', 'консервы', 'кроссворд', 'телефон', 'котелок', 'матрас', 'футболка'}
bill = {'книга', 'компас', 'зажигалка', 'крупы', 'хлеб', 'карты', 'телефон', 'шорты', 'фонарь', 'пила'}
dave = {'полотенце', 'зеркало', 'огниво', 'термос', 'телефон', 'фонарь', 'батарейки', 'карту местности', 'свисток', 'перочиный нож'}

things_for_trip['alex'] = alex
things_for_trip['bill'] = bill
things_for_trip['dave'] = dave

things_for_everybody = alex & bill & dave
uniq_things_for_two = alex & bill - dave | alex & dave - bill | bill & dave - alex
uniq_things_for_one = alex - bill - dave | dave - bill - alex | bill - dave - alex

print(f'Список вещей для похода: {things_for_trip}')
print(f'У всех друзей есть с собой {things_for_everybody}')
print(f'Только двое друзей имеют следующие вещи: {uniq_things_for_two}')

for item in uniq_things_for_two:
    if item not in alex:
        print(f'Алекс не взял с собой {item}')
    elif item not in bill:
        print(f'Билл не взял с собой {item}')
    elif item not in dave:
        print(f'Дэйв не взял с собой {item}')

print(f'Только один из друзей имеет следующие вещи: {uniq_things_for_one}')