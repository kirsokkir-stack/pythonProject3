class Animals:

    def __init__(self): #2, тому що 2 раза на день їсть
        self.eat = 'eat'
        self.breath = 'breath'

    def get_eat(self):
        return self.eat

    def get_breath(self):
        return self.breath

class Cat(Animals):

    def __init__(self):
        super().__init__()

smyrh = Cat() #smyrh це ім'я
print(f'Smyrh super {smyrh.get_eat()}')
print(f'Smyrh super {smyrh.get_breath()}')

class Dog(Animals):

    def __init__(self):
        super().__init__()

rembo = Dog()
print(f'Rembo super {smyrh.get_eat()}')
print(f'Rembo super {smyrh.get_breath()}')
