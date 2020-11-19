def my(a, b):
    degree = a
    for i in range(1, abs(b)):
        degree = degree * a
    value = 1 / degree
    print(f'Результат возведения в степень с помощью цикла: {value}')


def err():
    print('Ошибка! Введено значение не удовлетворяющее условию')


while True:
    try:
        x = input('Введите действительное положительное число: ')
        x = float(x)
        if x <= 0:
            err()
            continue
    except ValueError:
        err()
        continue
    try:
        y = input('Введите целое отрицательное число: ')
        y = int(y)
        if y >= 0:
            err()
            continue
    except ValueError:
        err()
        continue
    my(x, y)
    print(f'Результат возведения в степень: {x ** y}')
    break
