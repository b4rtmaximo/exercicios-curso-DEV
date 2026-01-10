lista_nomes = ['Ana', 'Pedro', 'Maria', 'João', 'Becky']
lista_idades = [23, 48, 32, 39, 71]
lista_estados = ['SP', 'CE', 'RS', 'RJ', 'MG']

resultado = zip(lista_nomes, lista_idades, lista_estados)
#print(dict(resultado))
#print(list(resultado))

for nome, idade, estado in resultado:
    print(f'{nome} tem {idade} anos e mora no estado de {estado}')

#A zip() combina elementos de múltiplos iteráveis, criando tuplas com os elementos correspondentes de cada um.

#"Descompactar" com zip(*):
#Você pode "inverter" um zip usando *:
pares = [(1, 'a'), (2, 'b'), (3, 'c')]

numeros, letras = zip(*pares)
print(numeros)  # (1, 2, 3)
print(letras)