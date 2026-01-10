lista = [True, True, True, True]
r = all(lista)

print(r)

lista2 = [True, 'Texto', 4, True]
r2 = all(lista2)

print(r2)

lista3 = [2, 4, 6, 8, 10]
r3 = all(n % 2 == 0 for n in lista3)

print(r3)

# retorna True se TODOS os elementos forem verdadeiros
#Para no primeiro False encontrado (eficiente)
#Lista vazia retorna True
#Muito útil para validações e verificações múltiplas