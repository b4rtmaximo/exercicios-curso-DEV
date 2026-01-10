from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = reduce(lambda a, b: a + b, numeros)

print(total)

#A reduce() reduz um iterável a um único valor, aplicando uma função acumuladora repetidamente.

#A função recebe 2 parâmetros: acumulador e elemento atual, e retorna o novo acumulador.

#Multiplicação (fatorial):

numeros = [1, 2, 3, 4, 5]
produto = reduce(lambda acum, num: acum * num, numeros)
print(produto)  # 120 (5!)

#Resumo:

#reduce(): transforma uma lista em um único valor
#Aplica a função repetidamente, acumulando o resultado
#Útil para operações personalizadas que não têm função built-in
#Geralmente, loops ou funções built-in são mais legíveis

#Mnemônico:

#map(): 1 para 1 (transforma cada elemento)
#filter(): N para N ou menos (seleciona elementos)
#reduce(): N para 1 (reduz a um único valor)