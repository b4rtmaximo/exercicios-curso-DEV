class Email:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @property
    def dominio(self):
        return self.__valor.split('@')[1]
    
    @property
    def usuario(self):
        return self.__valor.split('@')[0]
    
    def __str__(self) -> str:
        return self.valor