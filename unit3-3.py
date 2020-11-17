def my_func(a1, a2, a3):
    if a2 >= a1 <= a3:
        return a2 + a3
    elif a1 >= a2 <= a3:
        return a1 + a3
    elif a1 >= a3 <= a2:
        return a1 + a2

while True:
    try:
        a1 = int(input('Введите первое число: '))
        a2 = int(input('Введите второе число: '))
        a3 = int(input('Введите третье число: '))
    except :
        print('Неверное значение, попробуйте еще раз')
        continue
    print(my_func(a1, a2, a3))
    break

