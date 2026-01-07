class Funcionario:
    def __init__(self, salario):
        self.nome = 'Teste'
        self.__salario = salario


    # Getter
    def get_salario(self):
        return self.__salario
    

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 1300:
            raise ValueError('O salário não pode ser menor do que o mínimo')
            self.__salario = novo_salario


func = Funcionario(1000)
print(func.get_salario())

func.salario = 3000

print(func.salario)
