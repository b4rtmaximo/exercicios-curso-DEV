numeros = (1, 2, 3, 4, 5, 2)
print(numeros)

print(numeros[0])
#print(numeros[10]) #ERRO

misto = ('a', 'b', 'c', 7)
print(len(misto))

tupla = (1)
print(type(tupla))
# ✕
tupla = (1,)
print(type(tupla))

print(numeros.count(2))
print(numeros.index(5))
print(len(numeros))
print(min(numeros))
print(max(numeros))
print(sorted(numeros))
print(sum(numeros))
print(all(numeros)) # se tiver apenas elementos verdadeiros, retorna True