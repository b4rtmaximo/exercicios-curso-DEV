#começa do número 0 - 4
for n in range(5):
    print(n)

#de 1 - 5
for n in range(1, 6):
    print(n * '*')

#com saltos
for n in range(1, 26, 2):
    print(n * '✕')


#LISTAS
lista = [10, 20, 30, 40, 50]
for i in lista:
    print(i)

for indice, valor in enumerate(lista):
    print(f'{indice} - {valor}')


#TUPLAS
tupla = (2, 4, 6, 8)
for i in tupla:
    print(i, end=' ')


#SET
print()
sets = {1, 2, 3, 4, 5}
for i in sets:
    print(i)


#DICIONÁRIO
funcionario = {
    'nome': 'Maria',
    'salario': 7655.22,
    'idade': 35,
    'ativo': True
}

for chave in funcionario:
    print(chave)

for chave in funcionario.keys():
    print(chave, funcionario[chave])

for valor in funcionario.values():
    print(valor)

for chave, valor in funcionario.items():
    print(chave, valor)