#Задание №6*
#Напишите программу банкомат.
#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денег

MULT = 50
PERCENT = 0.015
EXTRA_PERCENT = 0.03
RICH_PERCENT = 0.01
MIN_CASH = 30
MAX_CASH = 600
MAX_COUNT = 1
MAX_SCORE = 5_000_000
count = 1
total_score = 0
MENU_ADD = 1
MENU_TAKE = 2
MENU_QUIT = 0

while True:
    print (f'Введите: \n'
           f'{MENU_ADD} для добавления денежных средств \n'
           f'{MENU_TAKE} для снятия денежных средств \n'
           f'{MENU_QUIT} или любую клавишу для выхода из меню')
    num = float(input("Ваш выбор: "))

    if num == MENU_ADD:
        add_money = int(input("Внесите сумму пополнения. Внимание! Сумма пополнения должна быть кратна 50: "))

        if add_money % MULT == 0:
            if count % 3 == 0 and total_score > MAX_SCORE:
                add_money = add_money - add_money * (EXTRA_PERCENT + RICH_PERCENT)
                #print(add_money, RICH_PERCENT, EXTRA_PERCENT)

            elif count % 3 == 0:
                add_money = add_money - add_money * EXTRA_PERCENT
                #print(add_money, EXTRA_PERCENT)

            elif total_score > MAX_SCORE:
                add_money = add_money - add_money * RICH_PERCENT
                #print(add_money, RICH_PERCENT)

            total_score += add_money

        else:
            print(f'Сумма должна быть кратной {MULT}! Повторите еще раз')
            total_score += 0

    elif num == MENU_TAKE:
        take_money = int(input(f'Укажите сумму снятия. Внимание! Сумма снятия должна быть кратна {MULT} : '))
        cash_percent = take_money * PERCENT

        if take_money % MULT == 0 and take_money <= total_score:
            if count % 3 == 0 and total_score > MAX_SCORE:
                take_money = take_money + take_money * (EXTRA_PERCENT + RICH_PERCENT)
                print(take_money, total_score, RICH_PERCENT, EXTRA_PERCENT)

            elif count % 3 == 0:
                take_money = take_money + take_money * EXTRA_PERCENT
                print(take_money, EXTRA_PERCENT)

            elif total_score > MAX_SCORE:
                if MIN_CASH < cash_percent < MAX_CASH:
                    take_money = take_money + take_money * (RICH_PERCENT + PERCENT)
                    print(take_money, cash_percent)

                elif cash_percent < MIN_CASH:
                    take_money = take_money + take_money * RICH_PERCENT + MIN_CASH
                    print(take_money, cash_percent, MIN_CASH)

                elif cash_percent > MAX_CASH:
                    take_money = take_money + take_money * RICH_PERCENT + MAX_CASH
                    print(take_money, cash_percent, MAX_CASH)

            else:
                if MIN_CASH < cash_percent < MAX_CASH:
                    take_money = take_money + take_money * PERCENT
                    print(take_money, cash_percent)

                elif cash_percent < MIN_CASH:
                    take_money = take_money + MIN_CASH
                    print(take_money, cash_percent, MIN_CASH)

                elif cash_percent > MAX_CASH:
                    take_money = take_money + MAX_CASH
                    print(take_money, cash_percent, MAX_CASH)

            total_score -= take_money

        else:
            print(f'Сумма должна быть кратной {MULT}, сумма снятия не больше {total_score}! Повторите еще раз')
            total_score += 0

    else:
        break

    count += 1
    print('У вас на счету:  ', total_score)
    print('cont:  ', count)