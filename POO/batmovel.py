class Carro():
    def dirigir(self):
        return 'Você esta dirigindo'
    

class Barco():
    def navegar(self):
        return 'Você esta navegando.'
    

class Aviao():
    def voar(self):
        return 'Você esta voando'
    

class Carro_Anfibio(Carro, Barco):
    pass


class Carro_Voador(Carro, Aviao):
    pass


class Batmovel(Carro,Aviao,Barco):
    pass



carro = Carro_Anfibio()
print(carro.dirigir())
print(carro.navegar())

carro = Carro_Voador()
print(carro.voar())
print(carro.dirigir())

carro = Batmovel()
print(carro.dirigir())
print(carro.navegar())
print(carro.voar())


