#Peça ao usuário que digite um número total em segundos.
#Converta o valor para horas, minutos e segundos.
tempo = int(input('Digite o tempo em segundos: '))
minutos = (tempo % 3600) / 60
hora = tempo // 3600
segundos = tempo % 60
print(f'{tempo} segundos = {hora} H {round(minutos)} MIN {segundos} SEG')