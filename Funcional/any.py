lista = [True, True, True, True]
r = any(lista)

print(r)

lista2 = [1, 2, 3, 5, 7]
r2 = any(n % 2 == 0 for n in lista2)

if r:
    print('Pelo menos um número é par.')
else:
    print('Nenhum número é par.')