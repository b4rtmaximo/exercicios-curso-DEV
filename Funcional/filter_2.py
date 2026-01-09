class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self) -> str:
        return f'Cliente: {self.nome},  {self.email}'

#__init__: construtor que inicializa nome e email
#__str__: define como o objeto será exibido quando usar print()
#O método __str__ é essencial aqui - sem ele, o print() mostraria algo como <__main__.Cliente object at 0x...> ao invés do texto formatado!


lista_clientes = [
    Cliente('João', 'joao@empresa.com.br'),
    Cliente('Maria', 'maria@empresa.com'),
    Cliente('Ana', 'ana@empresa.com.br'),
    Cliente('Pedro', 'pedro@empresa.com'),
    Cliente('Marta', 'marta@empresa.com.br'),
    Cliente('Cleber', 'cleber@empresa.com.br'),
]

filtro_pontocom = list(filter(lambda cliente: '.com' in cliente.email and '.br' not in cliente.email, lista_clientes ))

for clientes in filtro_pontocom:
    print(clientes)