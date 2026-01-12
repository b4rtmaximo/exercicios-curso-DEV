class SenhaForte:
    def __init__(self, valor):
        self.__valor = valor

        validacoes = [
            self.__tamanho_min(8),
            self.__tem_maiusculas(),
            self.__tem_mimusculas(),
            self.__tem_numeros(),
            self.__tem_caracteres_especiais()
        ]
    
        if not all(validacoes):
            raise ValueError('Senha é fraca')

    @property
    def valor(self):
        return self.__valor
    
    #Permite acessar a senha usando senha.valor ao invés de senha.__valor, mantendo o encapsulamento. A senha só pode ser lida, não modificada.
    
    def __tamanho_min(self, qtde):
        return len(self.valor) >= qtde
    
    def __tem_numeros(self):
        return any(letra.isdigit() for letra in self.valor)
    
    def __tem_maiusculas(self):
        return any(letra.isupper() for letra in self.valor)
    
    def __tem_mimusculas(self):
        return any(letra.islower() for letra in self.valor)
    
    def __tem_caracteres_especiais(self):
        return any(not letra.isalnum() for letra in self.valor)

try:
    senha = SenhaForte('#Senha123')
    print(senha.valor)
except ValueError as e:
    print(f'Ocorreu um erro: {e}')
finally:
    print('Programa finalizado.')

#A classe usa o conceito de Value Object (objeto de valor) - uma vez criada com uma senha válida, o objeto é imutável e garante que sempre contém uma senha forte.

