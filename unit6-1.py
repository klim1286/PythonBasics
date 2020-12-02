import time
from itertools import cycle
from random import randint


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        en = 0
        for state in cycle(self.__color):
            if en > randint(2, 5):
                break
            elif state == 'Красный':
                print(f'\033[31m{state}')
                time.sleep(7)
            elif state == 'Желтый':
                print(f'\033[33m{state}')
                time.sleep(2)
            elif state == 'Зеленый':
                print(f'\033[32m{state}')
                time.sleep(8)
            en += 1


run = TrafficLight()
run.running()
