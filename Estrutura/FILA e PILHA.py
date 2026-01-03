
#Exercício FILA
#1. Crie uma fila vazia usando deque.
#2. Adicione 3 nomes na fila.
#3. Retire o primeiro nome da fila e mostre quem foi atendido.
#4. Mostre quem é o próximo da fila.
#5. (Desafio) Crie uma fila de prioridade para representar atendimento médico
# (gravidade: 1 = mais urgente).

from collections import deque

fila = deque()
for i in range(3):
    nome = input('Nome: ')
    fila.append(nome)
paciente_agora = fila.popleft()
print(f'Paciente atendido: {paciente_agora}')
print(f'Próximo atendimento: {fila[0]}')


import heapq

atendimento = []
while True:
    try:
        resposta = input('Cadastrar para atendimento? [S/N]: ').upper().strip()[0]
        if resposta == 'N':
            break
        nome_paciente = input('Paciente: ').strip().upper()
        print('1️⃣ - emergência\n2️⃣ - urgência\n3️⃣ - sem urgência')
        gravidade = int(input('Gravidade: '))
        if gravidade == 1:
            heapq.heappush(atendimento,(1, nome_paciente))
        elif gravidade == 2:
            heapq.heappush(atendimento,(2, nome_paciente))
        elif gravidade == 3:
            heapq.heappush(atendimento,(3, nome_paciente))
        if gravidade not in [1, 2, 3]:
            print('Gravidade inválida! Digite 1, 2 ou 3.')
            continue
    except (ValueError, TypeError) :
        print('ERRO. Digite novamente!')
print("Fila com prioridade:", atendimento)

#_______________________________________________________________________________________

#Exercício PILHA
#1. Crie uma pilha vazia.
#2. Adicione os números 1, 2 e 3 na pilha.
#3. Retire o último número e mostre na tela.
#4. Mostre qual número ficou no topo da pilha.

pilha = []
for i in range(3):
    pilha.append(i+1)
print(f'Pilha: {pilha}')
último = pilha.pop()
print(f'Último ítem retirado da pilha: {último}')
print(f'Número que está no topo: {pilha[-1]}')