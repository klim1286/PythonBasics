class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        pass


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Общий доход: {self._income["wage"] + self._income["bonus"]}')


employee = Position('Andrei', 'Soo', 'N/A', 165000, 50000)
employee2 = Position('Nikolay', 'Nemo', 'Director', 150000, 500500)

employee.get_full_name()
employee.get_total_income()
employee2.get_full_name()
employee2.get_total_income()
