class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculations(self):
        print(f'Масса асфальта: {self._length * self._width * 25 * 5 // 1000} т')


mass = Road(20, 5000)
mass.calculations()
