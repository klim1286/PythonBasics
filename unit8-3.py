class OnlyNumbers(Exception):
    def __init__(self, exp):
        self.exp = exp


def is_number(x):
    if x.isdigit():
        return int(x)
    elif x.count('.') == 1:
        priv = x.split('.')
        if priv[0].isdigit() and priv[1].isdigit():
            return float(x)
        else:
            raise OnlyNumbers('Не введено число!')
    else:
        raise OnlyNumbers('Не введено число!')


print('для выхода из программы введите "stop"')
ls = []
while True:
    try:
        a = input('Введите число: ')
        if a.upper() == 'STOP':
            print(ls)
            break
        else:
            if a[0] == '-':
                ls.append(is_number(a[1:]) * -1)
            else:
                ls.append(is_number(a))
    except (ValueError, OnlyNumbers) as txt:
        print(txt)
        continue
