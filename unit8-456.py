loc = {1: 'Бухгалтерия', 2: 'Финансисты', 3: 'Директор'}


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
                printer_out.append(f'ID {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                printer += 1
            elif count['equipment'] == 'scaner' and count['location'] == 'sklad':
                scaner_out.append(f'ID {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                scaner += 1
            elif count['equipment'] == 'xerox' and count['location'] == 'sklad':
                xerox_out.append(f'ID {self.data.index(count)}, Модель: {count["model"]}, Цена: {count["cost"]}\n')
                xerox += 1
        return f'**********************************************\n' \
               f'На складе находится: \n' \
               f'Принтеров: {printer} шт. \n' \
               f'{"".join(printer_out)}\n' \
               f'Сканеров: {scaner} шт.\n' \
               f'{"".join(scaner_out)}\n' \
               f'Ксероксов: {xerox} шт. \n' \
               f'{"".join(xerox_out)}' \
               f'**********************************************'\


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
        self.resolution = resolution  # Разрешение копии


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


while True:
    try:
        mm = int(main_menu())
        if mm == 3:
            print(sklad.count_equ())
            main_menu()
        elif mm == 1:
            n1 = int(menu_1())
            while True:
                num = int(input('Какое количество принтеров вы хотите добавить? \nВведите число от 1 до 9: '))
                if 0 < num < 10:
                    break
                else:
                    print('Введите число от 1 до 9')
                    continue

            for _ in range(num):
                type_mod = input("Введите модель: ")
                cost = input("Введите стоимость оборудования: ")

                # Если выбран принтер
                if n1 == 1:
                    sklad.equipments_in(Printer(type_mod, cost))
                # Если выбран сканер
                elif n1 == 2:
                    sklad.equipments_in(Scaner(type_mod, cost))

                # Если выбран ксерокс
                elif n1 == 3:
                    sklad.equipments_in(Xerox(type_mod, cost))

                # Если выбран выход или ошибочный ввод
                else:
                    continue
        elif mm == 2:
            print(sklad.count_equ())
            id = int(input('Введите ID оборудования которое нужно передать: '))
            division = int(input(f'{loc} \nВведите номер подразделения для передачи оборудования:'))
            sklad.moving_equ(id, division)
        else:
            break
    except ValueError:
        print('Введено не целое число!\n ')
        continue
