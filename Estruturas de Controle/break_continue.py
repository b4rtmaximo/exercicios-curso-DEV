numeros = [1, 4, 7, 8, 10, 13, 14]

for n in numeros:
    if n % 2 == 0:
        continue
    print(n, end=' ')

print()

for n in numeros:
    if n == 8:
        break
    print(n, end= ' ')