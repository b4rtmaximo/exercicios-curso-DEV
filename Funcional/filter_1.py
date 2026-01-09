numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado_1 = filter(lambda n: n % 2 == 0, numeros)

print(list(resultado_1))

resultado_2 = list(filter(lambda n: n < 5, numeros))

print(resultado_2)

#A filter() filtra elementos de um iterável, mantendo apenas aqueles que atendem a uma condição (retornam True).