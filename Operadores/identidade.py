                # Tipos Básicos - Imutáveis
a = 6
b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)

a = 6
b = 5 + 1
print(id(a))
print(id(b))
print(a == b)
print(a is b)

                # Tipos Básicos - Mutáveis
x = [1, 2, 3]
y = x
print(id(x))
print(id(y))
print(x == y)
print(x is y)

x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))
print(id(y))
print(x == y)
print(x is y) #valores de memórias diferentes, apesar de serem iguais