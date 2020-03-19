class Washer:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._spin_dry()

    def _fill_water_tank(self, temperature):
        print(f'Filling tank with {temperature} water' )

    def _add_soap(self):
        print('Add soap')

    def _wash(self):
        print('Washing clothes')

    def _spin_dry(self):
        print('Spin dry clothes')


if __name__ == '__main__':
    washer = Washer()
    washer.wash()
