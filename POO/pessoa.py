class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Bia', 25)
p1.nome = 'Pedro'
print(p1.nome, p1.idade)

p2 = Pessoa('Ana', 81)
print(p2.nome, p2.idade)