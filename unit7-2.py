from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def cost(self):
        return "Это абстрактный метод"


class Coat(Clothes):
    def cost(self):
        return Coat(round(self.param / 6.5 + 0.5, 2))

    def __str__(self):
        return f'Необходимо материала для пальто: {self.param}'


class Costume(Clothes):
    def __str__(self):
        return f'Необходимо материала для костюма: {self.param}'

    @property
    def cost(self):
        return Costume(2 * self.param + 0.3)


coat = Coat(178)
print(coat.cost())

costume = Costume(60)
print(costume.cost)
