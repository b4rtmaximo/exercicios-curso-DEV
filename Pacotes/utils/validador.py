class Validador:
    def __init__(self, valor, atributo, erros=None):
        self.__valor = valor
        self.__atributo = atributo
        self.__erros = erros if erros is not None else []
    
    @property
    def valor(self):
        if self.__erros:
            raise ValueError(self.__erros)
        return self.__valor
    
    def nao_nulo(self):
        if self.__valor is None:
            self.__erros.append(f'{self.__atributo}: não pode ser nulo.')
        return self

    def nao_vazio(self):
        if self.__valor is None:
            return self
        
        if not self.__valor or not self.__valor.strip():
            self.__erros.append(f'{self.__atributo}: não pode ser vazio')
        return self
    
    def tamanho_min(self, minimo):
        if self.__valor is None:
            return self
        
        if len(self.__valor) < minimo:
            self.__erros.append(f'{self.__atributo}: deve possuir o tamanho mínimo de {minimo}')
        return self
    
    def tamanho_max(self, maximo):
        if self.__valor is None:
            return self
        
        if len(self.__valor) > maximo:
            self.__erros.append(f'{self.__atributo}: deve possuir o tamanho máximo de {maximo}')
        return self
    
    def qtde_min_palavras(self, qtde):
        if len(self.__valor.split()) < qtde:
            self.__erros.append(f'{self.__atributo}: deve possuir pelo menos {qtde} palavras.')
        return self
    
    def email(self):
        if self.__valor is None:
            return self
        
        if '@' not in self.__valor:
            self.__erros.append(f'{self.__atributo}: deve ser um e-mail válido')
        return self
    