class Calculadora:
    def __init__(self, valor_inicial=0):
        self.__valor = valor_inicial

    def somar(self, valor):
        self.__valor += valor
        return self

    def subtrair(self, valor):
        self.__valor -= valor
        return self

    def multi(self, valor):
        self.__valor *= valor
        return self

    def dividir(self, valor):
        self.__valor /= valor
        return self
        
    @property
    def valor(self):
        return self.__valor
    
    def __add__(self, outra_calc):
        return Calculadora(self.__valor + outra_calc.valor)
    
    def __eq__(self, outra_calc):
        return self.__valor == outra_calc.valor

    def __str__(self) -> str:
        return f'A calculadora tem um valor em memória de {self.__valor}'


calc1 = Calculadora(100)
calc1.somar(100)
calc1.subtrair(20)
calc1.multi(4)
calc1.dividir(2)
print(calc1.valor)

calc2 = Calculadora(1000).multi(3.1415) #Fluent API
print(calc2.valor)

calc3 = calc1 + calc2
print(calc3.valor)
print(calc3)

calc4 = calc1 + calc2
print(calc3 == calc4)
