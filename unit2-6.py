products_list = ('название', 'цена', 'количество', 'ед')
products_mane = {}
list_all = []
analit_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
i = 0
while True:
    print('Вы находитесь в главном меню.'
          'Для ввода данных нажмите "в". \n'
          'Для вывода статистики нажмите "а". \n'
          'Для выхода из программы введите "с".')
    user_change = input('Выберете значение из меню: ')
    if user_change == 'с':
        break
    elif user_change == 'в':
        i += 1
        for product in products_list:
            products_add = input(f'Введите {product}: ')
            products_mane.update({
                product: products_add if product == 'название' or product == 'ед' else int(products_add)
            })

            y = analit_dict.get(product)
            y.append(products_add if product == 'название' or product == 'ед' else int(products_add))
            if product == 'ед':
                list(set(analit_dict.get(product)))

        products_tuple = (i, products_mane)
        list_all.append(products_tuple)
        products_mane = {}
        print(list_all)
        continue
    elif user_change == 'а':

        print(analit_dict)
        continue
    else:
        continue
