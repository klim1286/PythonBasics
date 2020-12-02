class Stationery:  # Канцелярская пренадлежность
    def __init__(self, title):
        self.title = title

    def draw(self):  # запуск отрисовки
        print(self.title)


class Pen(Stationery):
    def draw(self):
        print(f'\033[34m{self.title * 2}')


class Pencil(Stationery):
    def draw(self):
        print(f'\033[36m{self.title[:-1:2]}')


class Handle(Stationery):
    def draw(self):
        print(f'\033[31m{self.title[::-1]}')


pen = Pen('Просто строка')
pen.draw()

pencil = Pencil('Просто строка')
pencil.draw()

handle = Handle('Просто строка')
handle.draw()
