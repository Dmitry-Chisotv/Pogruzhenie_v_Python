# Задача № 4
# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = input('Введите строку текста: ')
count = 0
letters_list = dict()

words = sorted(list(text.replace('.', '').replace(' -', '').replace(',', '').replace(':', '').replace(' —', '').replace('  ', '').\
    replace(' ', '').lower()))

key_letters = []
count_letters = []
i = 0
cnt = 1
ch = words[0]

for c in words[1:]:
    if c != ch:
        key_letters.append(ch)
        count_letters.append(cnt)
        ch = c
        cnt = 1

    elif c == words[-1]:
        key_letters.append(c)
        cnt += 1
        count_letters.append(cnt)

    else:
        cnt += 1

letters_list_2 = dict(zip(key_letters, count_letters))

for item in words:
    if words.count(item) in words:
        letters_list[item].append(words.count(item))
    else:
        letters_list[item] = [words.count(item)]

print(letters_list)
print(letters_list_2)
