#Classe Abstrata: É uma classe que não pode ser instanciada (não pode criar objetos dela diretamente). Ela serve como um "modelo" que obriga as classes filhas a implementarem certos métodos.

from abc import ABC, abstractmethod

class Atendente(ABC):
    @abstractmethod
    def saudacao(self):
        pass
    

class AtendentePT(Atendente):
    def saudacao(self):
        return 'Bom dia!'


atendente_n1 = AtendentePT()
print(atendente_n1.saudacao())