def my_func(x, y, z):
    if y >= x <= z:
        return y + z
    elif x >= y <= z:
        return x + z
    elif x >= z <= y:
        return x + y


while True:
    try:
        a1 = int(input('Введите первое число: '))
        a2 = int(input('Введите второе число: '))
        a3 = int(input('Введите третье число: '))
    except ValueError:
        print('Неверное значение, попробуйте еще раз')
        continue
    print(my_func(a1, a2, a3))
    break
