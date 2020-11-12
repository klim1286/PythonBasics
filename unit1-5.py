proceeds = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))


if proceeds > cost: # если прибыль
    print(f'Рентабельность фирмы: {(proceeds - cost) / proceeds * 100:.2f}%')
    employees = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль фирмы на одного сотрудника {(proceeds - cost) / employees:.2f}')
elif proceeds < cost: # если убыток
    print('Ваша фирма в убытке')
else: # если 0
    print('Ваша фирма вышла в 0')
