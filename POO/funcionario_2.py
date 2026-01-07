class FuncionarioV2:
    def __init__(self, salario):
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    def movimentacao_salarial(self, percentual):
        if percentual < 0:
            raise ValueError('Percentual inválido')
        self.__salario = self.__salario + (self.salario * percentual/100) 


func = FuncionarioV2(2000)
func.movimentacao_salarial(50)
print(func.salario)
