'''
Escreva um código que gere os números da Mega Sena. Primeiramente
solicite para o usuário informar a quantidade de números da aposta
 (entre 6 - 20) e depois gere uma lista com o tamanho solicitado com
números não repetidos entre 1 - 60.

'''
#———————————————————————————————————————————————————————————————————————————————————————————————————————————————

from random import randint, sample

quantidade_apostas = int(input('Informe quantos números [6 - 20]: '))

if 20 >= quantidade_apostas >= 6:
    aposta = []

    while len(aposta) < quantidade_apostas:
        numeros = randint(1, 60)
        if numeros not in aposta:
            aposta.append(numeros)
    
    aposta.sort()
    print(f'Números: \n{aposta}')

else:
    print('Quantidade inválida!')    

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————

quantidade_apostas = int(input('Informe quantos números [6 - 20]: '))

if 20 >= quantidade_apostas >= 6:
    aposta = sample(range(1, 61), quantidade_apostas)
    aposta.sort()
    print(f'Números: \n{aposta}')

else:
    print('Quantidade inválida!')  
