class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return Cell(self.cell - other.cell)
        else:
            return 'Ошибка! Вычитание невозможно'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        try:
            return Cell(self.cell // other.cell)
        except ZeroDivisionError:
            return 'Ошибка! Деление невозможно'

    def make_order(self, row):
        # self.row = row
        st_new = ''
        for i in range(self.cell):
            if i % row == 0 and i != 0:
                st_new += '\n'
            st_new += '*'
        return st_new


cell1 = Cell(11)
cell2 = Cell(15)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell1.make_order(5))
