frutas = {'banana', 'maça', 'laranja', 'banana'}
print(frutas)  #não permite valores duplicados

frutas.add('uva')
print(frutas)  #não é indexado e não garante ordenação

frutas.remove('banana')
print(len(frutas))
frutas.clear()

conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5}

uniao = conjunto_1.union(conjunto_2)
print(uniao)

intersecao = conjunto_1.intersection(conjunto_2)
print(intersecao)

diferenca = conjunto_1.difference(conjunto_2)
print(diferenca)

conjunto_2.update({7,5,6})
print(conjunto_2)