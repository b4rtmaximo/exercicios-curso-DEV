def remover_nome(nome):
    def remover_da_lista(lista):
        return [n for n in lista if n != nome]
    return remover_da_lista

remover_maria = remover_nome('Maria')
remover_joao = remover_nome('João')

lista_1 = ['Ana', 'Pedro', 'Maria', 'João', 'Maria']
lista_2 = ['Gui', 'Rebeca', 'Maria', 'Chico', 'Tereza']

print(remover_maria(lista_1))
print(remover_joao(lista_1))
print(remover_maria(lista_2))
print(remover_joao(lista_2))

print(remover_nome('Gui')(lista_2))

#remover_maria e remover_joao são funções personalizadas criadas dinamicamente
#Cada uma "capturou" um valor diferente de nome e o mantém na memória
#Isso é chamado de closure - a função interna mantém acesso ao escopo da função externa mesmo depois que ela terminou