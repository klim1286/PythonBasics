all_data = 0


def my_sum(main_all):
    while True:
        new_line = input('Введите числа через пробел. Для выхода введите "q". ')
        data = new_line.split()
        for element in data:
            try:
                main_all += int(element)
            except ValueError:
                if element.upper() == 'Q':
                    return main_all
                else:
                    print('Если вы хотите выйти введите "q"')
                    continue
        print(main_all)


print(my_sum(all_data))
