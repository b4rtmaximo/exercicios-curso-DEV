base_dois = []

for i in range(1,21):
    base_dois.append( 2 ** i)
print(base_dois)

# Modelo: [expressão for ... if ...]
base_dois_LC = [2 ** i for i in range (1, 21)]
print(base_dois_LC)


base_dois_LC = [2 ** i for i in range (1, 21) if i % 2 == 0]
print(base_dois_LC)

numeros = [x * x for x in range(30) if x % 3 != 0]
print(numeros)