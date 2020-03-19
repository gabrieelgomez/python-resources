class Car:

    def __init__(self, model, brand, color):
        self.model   = model
        self.brand   = brand
        self.color   = color
        self._status = 'resting'
        self._engine = Engine(cylinders=4)

    def speed_up(self, type='slow'):
        if type == 'fast':
            self._engine.inyect_gasoline(10)
        else:
            self._engine.inyect_gasoline(3)

        self._status = 'moving'


class Engine:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders    = cylinders
        self.type         = type
        self._temperature = 0

    def inyect_gasoline(self, quantity):
        pass

if __name__ == '__main__':
    car = Car('Civic', 'Honda', 'Silver')
    print(car._status)
    car.speed_up('fast')
    print(car._status)