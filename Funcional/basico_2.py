def somar(a):
    def finalizar_soma(b):
        return a + b
    return finalizar_soma

print(somar(3)(7))

salario_base = 2113.50
somar_com_salario_base = somar(salario_base)

print(somar_com_salario_base(500))