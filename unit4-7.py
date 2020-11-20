from functools import reduce


def prod(x, y):
    return x * y


def fact(z):
    yield reduce(prod, [el for el in range(1, z + 1)])


while True:
    try:
        n = int(input('Введите целое положительное число: '))
        for el in fact(n):
            print(el)
            break
    except ValueError:
        print('Введите целое положительное число: ')
