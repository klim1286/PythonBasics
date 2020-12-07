loc = {1: 'Бухгалтерия', 2: 'Финансисты', 3: 'Директор'}
model_print = {1: 'HP LaserJet P2035', 2: 'HP LaserJet Pro M203dn', 3: 'HP LaserJet Pro M15w',
               4: 'KYOCERA FS-1040', 5: 'KYOCERA ECOSYS P2040dn', 6: 'KYOCERA ECOSYS P2335dw',
               7: 'Canon i-SENSYS LBP112', 8: 'Canon i-SENSYS LBP226dw', 9: 'Canon i-SENSYS LBP162dw'
               }
model_scan = {1: 'Fujitsu ScanPartner SP1120', 2: 'Fujitsu fi-7260', 3: 'Fujitsu SP-1425',
              4: 'HP ScanJet Pro 2000 s2', 5: 'HP ScanJet Pro 2500 f1', 6: 'HP ScanJet Pro N4000 snw1',
              7: 'Brother ADS-2200', 8: 'Brother ADS-3000N', 9: 'Brother ADS-3600W'
              }
model_xerox = {1: 'CANON imageRUNNER 2204', 2: 'Kyocera TASKalfa 181 1102KJ3NL0', 3: 'CANON imageRUNNER C3025',
               4: 'Xerox WorkCentre Copier 5230', 5: 'CANON imageRUNNER C3025i', 6: 'Xerox WorkCentre 6400X',
               7: 'HP Color LaserJet Enterprise 700 M775f', 8: 'CANON imageRUNNER 1435iF',
               9: 'Canon imageRUNNER C1225IF'
               }


class Warehous:
    def __init__(self):
        self.units = {}
        self.data = []

    def equipments_in(self, *equipments):
        for equipment in equipments:
            self.units.update({'equipment': equipment.typemod, 'cost': equipment.cost, 'model': equipment.model,
                               'location': 'sklad'})
            self.data.append(self.units)
            self.units = {}
        return self.data

    def count_equ(self):
        printer, scaner, xerox = 0, 0, 0
        printer_out, scaner_out, xerox_out = [], [], []
        for count in self.data:
            if count['equipment'] == 'printer' and count['location'] == 'sklad':
                printer_out.append(f'ID: {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                printer += 1
            elif count['equipment'] == 'scaner' and count['location'] == 'sklad':
                scaner_out.append(f'ID: {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                scaner += 1
            elif count['equipment'] == 'xerox' and count['location'] == 'sklad':
                xerox_out.append(f'ID: {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                xerox += 1
        return f'**********************************************\n' \
               f'На складе находится: \n' \
               f'Принтеров: {printer} шт. \n' \
               f'{"".join(printer_out)}\n' \
               f'Сканеров: {scaner} шт.\n' \
               f'{"".join(scaner_out)}\n' \
               f'Ксероксов: {xerox} шт. \n' \
               f'{"".join(xerox_out)}' \
               f'**********************************************' \


    def moving_equ(self, id, location):
        self.data[id].update({'location': loc[location]})
        print(f'Техника {self.data[id]} выдана {loc[location]}')

    def __str__(self):
        return f'{self.data}\n'


class Equipment:
    def __init__(self, model, cost):
        self.model = model  # Модель
        self.cost = cost  # Цена


class Printer(Equipment):
    typemod = 'printer'

    def __init__(self, model, cost, technology='laser', speed=10, color='black'):
        super().__init__(model, cost)
        self.technology = technology  # Технология печати
        self.speed = speed  # Скорость печати
        self.color = color  # Цвет печати


class Scaner(Equipment):
    typemod = 'scaner'

    def __init__(self, model, cost, type='Планшетный', resolution='1800*600'):
        super().__init__(model, cost)
        self.type = type  # Тип сканера
        self.resolution = resolution  # Разрешение сканирования


class Xerox(Equipment):
    typemod = 'xerox'

    def __init__(self, model, cost, resolution='1800*600'):
        super().__init__(model, cost)
        self.resolut1ion = resolution  # Разрешение копии


printer1 = Printer('HP', 5000)
scaner1 = Scaner('Canon', 3590)
printer2 = Printer('Canon', 4990)
printer3 = Printer('Kyocera', 12990)
xerox = Xerox('Canon', 3590)
sklad = Warehous()
sklad.equipments_in(printer1, scaner1, printer2, printer3)  # Оприходование техники на склад


# sklad.moving_equ(2, 'accounting department')  # Передача техники
# print(sklad.count_equ()) # Вывод техники на складе


def main_menu():
    print('Вы находитесь в главном меню \n'
          '1 - Принять технику на склад \n'
          '2 - Переместить технику со склада \n'
          '3 - Просмотреть технику на складе \n'
          '0 - Выход')
    return input('Выберете номер нужного пункта меню и нажмите Ввод: ')


def menu_1():
    print('Вы находитесь в меню "Принять технику на склад" \n'
          '1 - Принтер \n'
          '2 - Сканер \n'
          '3 - Ксерокс \n'
          '0 - Главное меню \n')
    return input('Выберете номер нужного пункта меню и нажмите Ввод: ')


def print_mod_eq(mod_eq):
    txt = ''
    z = 0
    for i in mod_eq:
        if z == 5:
            txt += '\n'
            z = 0
        txt += f'{i}:{mod_eq[i]} | '
        z += 1
    return txt


def chose_eq(type_eq):
    if type_eq == 1:
        while True:
            print(print_mod_eq(model_print))
            type_mod = int(input("Выбирете модель цифрами: "))
            if 1 > type_mod or type_mod > len(model_print):
                print('Такой модели нет, выберете из списка:')
            else:
                cost = int(input("Введите стоимость оборудования: "))
                return model_print[int(type_mod)], cost
    elif type_eq == 2:
        while True:
            print(print_mod_eq(model_scan))
            type_mod = int(input("Выбирете модель цифрами: "))
            if 1 > type_mod or type_mod > len(model_print):
                print('Такой модели нет, выберете из списка:')
            else:
                cost = int(input("Введите стоимость оборудования: "))
                return model_scan[int(type_mod)], cost
    elif type_eq == 3:
        while True:
            print(print_mod_eq(model_xerox))
            type_mod = int(input("Выбирете модель цифрами: "))
            if 1 > type_mod or type_mod > len(model_print):
                print('Такой модели нет, выберете из списка:')
            else:
                cost = int(input("Введите стоимость оборудования: "))
                return model_xerox[int(type_mod)], cost


while True:
    try:
        mm = int(main_menu())
        if mm == 3:
            print(sklad.count_equ())
            continue
        elif mm == 1:

            while True:
                n1 = int(menu_1())
                if n1 < 4 and n1 > 0:
                    num = int(input('Какое количество оборудования вы хотите добавить? \nВведите число от 1 до 9: '))
                    if 0 < num < 10:
                        break
                    else:
                        print('Введите число от 1 до 9')
                        continue
                elif n1 == 0:
                    break
                else:
                    continue

            for _ in range(num):

                # Если выбран принтер
                if n1 == 1:
                    answer = chose_eq(n1)
                    sklad.equipments_in(Printer(answer[0], answer[1]))
                    print('Принтер успешно добавлен на склад')
                # Если выбран сканер
                elif n1 == 2:
                    answer = chose_eq(n1)
                    sklad.equipments_in(Scaner(answer[0], answer[1]))
                    print('Сканер успешно добавлен на склад')
                # Если выбран ксерокс
                elif n1 == 3:
                    answer = chose_eq(n1)
                    sklad.equipments_in(Xerox(answer[0], answer[1]))
                    print('Ксерокс успешно добавлен на склад')
                # Если выбран выход или ошибочный ввод
                elif n1 == 0:
                    break
                else:
                    continue

        elif mm == 2:
            while True:
                print(sklad.count_equ())
                id = int(input('Введите ID оборудования которое нужно передать: '))
                if id < 0 or id > len(sklad.data) - 1:
                    print('Введите существующий ID оборудования которое нужно передать: ')
                    continue
                elif sklad.data[id]['location'] != 'sklad':
                    print('Оборудование уже переданно в другое подразделение\n'
                          'Введите ID оборудования которое нужно передать: ')
                    continue
                else:
                    break

            while True:
                division = int(input(f'{loc} \nВведите номер подразделения для передачи оборудования:'))
                if division < 1 or division > len(loc):
                    print('Выберете подразделение из списка: ')
                    continue
                else:
                    sklad.moving_equ(id, division)
                    break
        elif mm == 0:
            break
        else:
            continue
    except (ValueError, TypeError):
        print('\n!!!!!!!!!Ошибка!!!!!!!!!!!!\n'
              'Введено не верное значение!\n'
              '!!!!!!!!!!!!!!!!!!!!!!!!!!')
        continue
    except NameError:
        continue
