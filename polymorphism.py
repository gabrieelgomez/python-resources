class Person:

    def __init__(self, name):
        self.name = name

    def get_moving(self):
        print('Walking')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print("I'm moving on a bicycle")


def main():
    person = Person('Gabriel')
    person.get_moving()

    ciclyst = Cyclist('Máximo')
    print(ciclyst.name)
    ciclyst.get_moving()


if __name__ == '__main__':
    main()