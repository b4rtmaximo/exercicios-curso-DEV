class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


lista_clientes = [
    Cliente('João', 'joao@empresa.com.br'),
    Cliente('Maria', 'maria@empresa.com.br'),
    Cliente('Ana', 'ana@empresa.com.br'),
    Cliente('Pedro', 'pedro@empresa.com.br'),
    Cliente('Marta', 'marta@empresa.com.br'),
    Cliente('Cleber', 'cleber@empresa.com.br'),

]

somente_email = list(map(lambda cliente: cliente.email, lista_clientes))

print(somente_email)
                     