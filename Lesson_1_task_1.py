# name = 'Alex'
#age = None
#print (name, age)
#print (name, age, sep=' (<*>) ', end=' !!! ')
#print (name, age)

#res = input('Print your number ')
#print ("Ты написал ", res)

#age = int(input("Сколько тебе лет? "))
#ADULT = 18
#how_old = ADULT - age
#print (how_old, " осталось до совершеннолетия")

#pwd = 'text'
#res = input("Введите пароль ")
#if pwd == res:
#    print("Доступ разрешен")
#    my_math = int(input("Сколько будет 2+2 "))
#    if my_math == 4:
#        print("Krasava")
#    else:
#        ("Учись считать")
#else:
#    print("Доступ запрещен!")
#print("Работа завершена")

#color = input("Введите любимый цвет ")
#if color == "красный":
#    print('ты любишь корриду')
#elif color == 'белый':
#    print('Ты хочешь пожениться')
#elif color == 'черный':
#    print('Лучше бы не говорил')
#else:
 #   print('Хрен тебя знает')

color = input("Введите любимый цвет ")
match color == "красный":
    case "красный" | "синий": 
        print('ты любишь корриду')
    case "желтый" | 'белый':
        print('Ты хочешь пожениться')
    case "зеленый" | 'черный':
        print('Лучше бы не говорил')
    case _:
        print('Хрен тебя знает')

#      

#year = int(input("year in format YYYY: "))
#if year %4 != 0 or year % 100 == 0 and year % 400 != 0 :
#    print('obychny')
#else:
#    print('vysokosny')

#data = [0, 1, 1, 2 , 3, 5, 8, 13, 21]
#num = int(input('vvedite chislo '))
#if num in data:
#    print('Leonardo is happy')

#data = [0, 1, 1, 2 , 3, 5, 8, 13, 21]
#num = int(input('vvedite chislo '))
#if num not in data:
#    print('Leonardo is sad')

#my_math = int(input("Сколько будет 2+2 ="))
#print ('correct' if 2 + 2 == my_math else "are you sure?")

#num  = float(input('Print your number '))
#count = 0
#while count < num:
#    print (count)
 #   count += 2

#num  = float(input('Print your number '))
#STEP = 2
#limit = num - STEP
#count = -STEP
#while count < limit:
#    count += STEP
 #   if count %12 ==0:
#        continue
#    print (count)   # num=20; print (2,4,6,8,10,14,16,18)

min_limit = 0
max_limit = 10
while True:
    print ('Vveite chislo mezhdu ', min_limit, 'i', max_limit)
    num  = float(input())
    if num < min_limit or num > max_limit:
        print('neverno')
    else:
        break
print ('Bylo vvedeno chislo  ', num)


min_limit = 0
max_limit = 10
count = 1
num = None

while count < 4:
    print('Popytka ', count)
    count +=1

    print ('Vveite chislo mezhdu ', min_limit, 'i', max_limit)
    num  = float(input())
    if num < min_limit or num > max_limit:
        print('neverno')
    else:
        break

else:
    print ('Popytki zakonchilis')
    quit()

print ('Bylo vvedeno chislo  ', num)

#data = [0, 1, 1, 2 , 3, 5, 8, 13, 21]
#for item in data:
#    print(item)

num = int(input('vvedite chislo '))
for i in range(0, num, 2):   #выводятся числа от 0 до num с шагом 2
    print(i)

animals = ['cat', 'dog', 'rat', 'wolf', 'dragon']
for i, animal in enumerate (animals, start=1):
    print(i, animal)