from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} {choice(["вперед", "назад", "на лево", "на право"])}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed >= 60:
            print(f'{self.name} превысила скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed >= 40:
            print(f'{self.name} превысила скорость!')


class PoliceCar(Car):
    pass


mazeratty = SportCar(100, 'blue', 'mazeratty', False)
cruma = TownCar(100, 'black', 'cruma', False)
lada = WorkCar(60, 'yellow', '2107', False)
crown = PoliceCar(100, 'white', 'victoriya', True)

mazeratty.go()
mazeratty.turn()
mazeratty.show_speed()
mazeratty.stop()

cruma.go()
cruma.turn()
cruma.show_speed()
cruma.stop()

lada.go()
lada.turn()
lada.show_speed()
lada.stop()

crown.go()
crown.turn()
crown.show_speed()
crown.stop()
