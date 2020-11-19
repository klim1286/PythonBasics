def split(x, y):
    sp = x / y
    sp = round(sp, 5)
    return sp


while True:
    try:
        a1 = float(input(f'Введите первое число: '))
        a2 = float(input(f'Введите второе число: '))
        print(f'Результат деления {split(a1,a2)}')
        break
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        continue
    except ValueError:
        print('Невозможно преобразовать строку в число!')
        continue
