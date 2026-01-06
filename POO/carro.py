class Carro():
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def buzinar(self, qtde=1):
        for i in range(qtde):
            print(f'{self.marca} {self.modelo} ==> Biiiiii')

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10


carro_1 = Carro('BYD', 'Dolphin')
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.frear()
carro_1.buzinar(3)

print(carro_1.marca, carro_1.modelo, carro_1.velocidade)


carro_2 = Carro('Toyota', 'Yaris Cross')
        