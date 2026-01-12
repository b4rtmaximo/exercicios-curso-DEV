class NomePessoa:
    def __init__(self, completo):
        self.__completo = completo

    @property
    def completo(self):
        return self.__completo
    
    @property
    def primeiro_nome(self):
        return self.__completo.split()[0]
    
    @property
    def sobrenome(self):
        return self.__completo.split()[-1]