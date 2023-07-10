"""Задача №3
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""



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
history_of_transactions = []


def add_cash(cash):
    globals()
    if count % 3 == 0 and total_score > MAX_SCORE:
        cash = cash - cash * (EXTRA_PERCENT + RICH_PERCENT)

    elif count % 3 == 0:
        cash = cash - cash * EXTRA_PERCENT

    elif total_score > MAX_SCORE:
        cash = cash - cash * RICH_PERCENT

    return cash


def recive_cash(take_money):
    globals()
    if count % 3 == 0 and total_score > MAX_SCORE:
        take_money = take_money + take_money * (EXTRA_PERCENT + RICH_PERCENT)

    elif count % 3 == 0:
        take_money = take_money + take_money * EXTRA_PERCENT

    elif total_score > MAX_SCORE:
        if MIN_CASH < cash_percent < MAX_CASH:
            take_money = take_money + take_money * (RICH_PERCENT + PERCENT)

        elif cash_percent < MIN_CASH:
            take_money = take_money + take_money * RICH_PERCENT + MIN_CASH

        elif cash_percent > MAX_CASH:
            take_money = take_money + take_money * RICH_PERCENT + MAX_CASH

    else:
        if MIN_CASH < cash_percent < MAX_CASH:
            take_money = take_money + take_money * PERCENT

        elif cash_percent < MIN_CASH:
            take_money = take_money + MIN_CASH

        elif cash_percent > MAX_CASH:
            take_money = take_money + MAX_CASH

    return take_money


while True:
    print (f'Введите: \n'
           f'{MENU_ADD} для добавления денежных средств \n'
           f'{MENU_TAKE} для снятия денежных средств \n'
           f'{MENU_QUIT} или любую клавишу для выхода из меню')
    num = float(input("Ваш выбор: "))

    if num == MENU_ADD:
        add_money = int(input("Внесите сумму пополнения. Внимание! Сумма пополнения должна быть кратна 50: "))

        if add_money % MULT == 0:

            if __name__ == '__main__':
                total_score += add_cash(add_money)
                history_of_transactions.append(add_money)

        else:
            print(f'Сумма должна быть кратной {MULT}! Повторите еще раз')
            total_score += 0

    elif num == MENU_TAKE:
        take_money = int(input(f'Укажите сумму снятия. Внимание! Сумма снятия должна быть кратна {MULT} : '))
        cash_percent = take_money * PERCENT

        if take_money % MULT == 0 and take_money <= total_score:

            if __name__ == '__main__':

                recive_cash(take_money)
                total_score -= take_money
                history_of_transactions.append(take_money * -1)

        else:
            print(f'Сумма должна быть кратной {MULT}, сумма снятия не больше {total_score}! Повторите еще раз')
            total_score += 0

    else:
        break

    count += 1
    print('У вас на счету:  ', total_score)
    print(history_of_transactions)