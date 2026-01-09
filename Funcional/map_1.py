def dobro(n):
    return n * 2


lista_1 = [1, 2, 3, 4, 5]

resultado_1 = map(dobro, lista_1)
print(list(resultado_1))

resultado_2 = map(lambda x: x * 3, lista_1)
print(list(resultado_2))

#A map() aplica uma função a cada elemento de um iterável (lista, tupla, etc.) e retorna um objeto map com os resultados.

#map() retorna um objeto map, não uma lista diretamente
#Por isso você precisa converter com list() se quiser ver os resultados
