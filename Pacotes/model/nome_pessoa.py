from utils.validador import Validador

class NomePessoa:
    def __init__(self, completo, atributo='Nome'):
        self.__completo = Validador(completo, atributo). nao_nulo().nao_vazio().tamanho_max(120).tamanho_min(4).qtde_min_palavras(2).valor

    @property
    def completo(self):
        return self.__completo
    
    @property
    def primeiro_nome(self):
        return self.__completo.split()[0]
    
    @property
    def sobrenome(self):
        return self.__completo.split()[-1]
    
    def __str__(self) -> str:
        return self.__completo