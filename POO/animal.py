class Animal():
    def __init__(self, nome):
        self.nome = nome

    def expressar(self):
        return f'O {self.nome} esta fazendo um som.'


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)


    def expressar(self):
        return f'{super().expressar()}... au au au'


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)


animal1 = Animal('Animal')
print(animal1.expressar())

animal2 = Cachorro('Rex')
print(animal2.expressar())

animal3 = Gato('Lua')
print(animal3.expressar())