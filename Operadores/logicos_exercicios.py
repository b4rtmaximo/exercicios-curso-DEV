trabalho_terca = bool(int(input('O trabalho de terça-feira foi concluído? [SIM=1 NÃO=0]: ')))
trabalho_quinta = bool(int(input('O trabalho de quinta-feira foi concluído? [SIM=1 NÃO=0]: ')))

print('Vamos comprar tv grande?', trabalho_terca and trabalho_quinta) #AND
print('Vamos comprar tv pequena?', trabalho_terca != trabalho_quinta) #XOR
print('Vamos tomar o sorvete?', trabalho_terca or trabalho_quinta)    #OR
print('Vamos ficar em casa?', not (trabalho_terca or trabalho_quinta)) #NOT