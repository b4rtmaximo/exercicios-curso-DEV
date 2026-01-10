try:
    divisor = int(input('Informe um divisor: '))
    resultado = 1000 / divisor
    print(f'O resultado da divisão é {resultado}')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except Exception as e:
    print('Um erro aconteceu.',end='')
    print(e)
