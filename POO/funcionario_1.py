class Funcionario:
    def __init__(self, salario):
        self.nome = 'Teste'
        #O __ (duplo underscore) antes de salario torna esse atributo privado. Isso significa que você não deveria acessá-lo diretamente de fora da classe. É uma forma de proteger dados sensíveis.
        self.__salario = salario


    # Getter: É um método comum para acessar um atributo privado. Você chama como uma função
    def get_salario(self):
        return self.__salario
    
    #O @property transforma o método em uma propriedade. Agora você pode acessar salario como se fosse um atributo normal, mas por baixo dos panos está executando um método:
    @property
    def salario(self):
        return self.__salario

    #O @salario.setter permite modificar o atributo com validação.
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 1300:
            raise ValueError('O salário não pode ser menor do que o mínimo')
        self.__salario = novo_salario


func = Funcionario(1000)
print(func.get_salario())

func.salario = 3000

print(func.salario)

#Resumo do fluxo do código:

#Cria funcionário com salário 1000
#Imprime usando getter tradicional: 1000
#Modifica salário para 3000 (usando o setter)
#Imprime usando property: 3000

#A vantagem do @property e @setter é que você usa a sintaxe simples de atributos, mas com a segurança de validação e encapsulamento dos métodos!