numero = int(input('Escreva um número: '))
if numero > 0:
    print(f'O número {numero} é POSITIVO. ', end='')
else:
    print(f'O número {numero} é NEGATIVO. ', end='')

if numero % 2 == 0:
    print('E tbm é PAR.')
elif numero % 2 != 0:
    print('E tbm é ÍMPAR.')    
else:
    print('O número é ZERO')
    

print('FIM')

# ———————————————————————————————————————————————————————————————————————————————————— #

'''
Escreva um programa que pergunte a velocidade de um carro de um usuário. Caso ultrapasse
80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor 
da multa, cobrando R$ 5 por km acima de 80 km/h.
'''

velocidade_veiculo = float(input('Qual a velocidade do veículo?[km/h]: '))
if velocidade_veiculo > 80:
    print('Você foi multado por excesso de velocidade!')
    print(f'Multa: R$ {(velocidade_veiculo - 80)*5:.2f}')
else:
    print('Dentro do limite de velocidade.')

'''
Faça um programa que leia 3 números e mostre qual o maior e qual o menor.
'''
num1 = int(input('Número Um: '))
num2 = int(input('Número Dois: '))
num3 = int(input('Número Três: '))
if num1 == num2 == num3:
    print('Os valores são iguais')
else:
    if num1 >= num2 and num1 >= num3:
        print(f'{num1} é o maior.')
    elif num2 >= num1 and num2 >= num3:
        print(f'{num2} é o maior.')
    else:
        print(f'{num3} é o maior.')

    if num1 <= num2 and num1 <= num3:
        print(f'{num1} é o menor.')
    elif num2 <= num1 and num2 <= num3:
        print(f'{num2} é o menor.')
    else:
        print(f'{num3} é o menor.')

    