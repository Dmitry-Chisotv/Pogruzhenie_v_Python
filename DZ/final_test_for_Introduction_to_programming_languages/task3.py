"""Напишите программу вычисления функции Аккермана с помощью рекурсии.
Даны два неотрицательных числа m и n."""

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

if __name__ == '__main__':
    m = 3
    n = 4
    result = ackermann(m, n)
    print(f"A({m}, {n}) = {result}")