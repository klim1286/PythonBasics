while True:
    f = int(input('Введите номер месяца: '))
    if 1 <= f <= 12:
        season = [
            'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
            'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима'
        ]

        month = {
            1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
            7: 'Июль', 8: 'Август', 9: 'Сеньябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
        }
        print(f'Месяц: {month[f]}. Время года: {season[f-1]}')
        break
    else:
        continue