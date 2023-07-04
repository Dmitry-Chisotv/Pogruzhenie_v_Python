# Задача 1
#Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

array = [1, True, True, False, 'texttext', 2, 1, 3.21, 'texttext', 1, 5, 6, 3, 2]
array_res = []

for item in array:
    if array.count(item) >= 2:
        array_res.append(item)

print(list(set(array_res)))