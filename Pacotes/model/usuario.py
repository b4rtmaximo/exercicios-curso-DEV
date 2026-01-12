from .email import Email
from .nome_pessoa import NomePessoa

class Usuario:
    def __init__(self, nome, email):
        self.nome = NomePessoa(nome, 'Nome Usuário')
        self.email = Email(email, 'E-mail Usuário')

    def __str__(self) -> str :
        return f'Usuário: {self.nome}\nE-mail: {self.email}'
        