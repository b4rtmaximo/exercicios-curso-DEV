from .email import Email

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = Email(email)

    def __str__(self) -> str :
        return f'Usuário: {self.nome}\nE-mail: {self.email}'
        