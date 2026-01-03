#Lista é uma estrutura indexada
#ìndices   0 1 2 3
numeros = [1,2,3,4]

frutas = ['maçã', 'banana', 'laranja']
mix = [True, 3.45, 6, 'banana',[1,2,3]]
print(mix)

#Acessar os elementos pelo índice
print(frutas[1]) #banana
print(mix[4][1]) #2
print(frutas[-1]) #laranja

numeros.append(100) #[1, 2, 3, 4, 100]
numeros.insert(0,100) #[100, 1, 2, 3, 4, 100]
numeros.remove(100) #[1, 2, 3, 4, 100]

lista = [1,2,3,4,4,6,7,8,4,2,4,3,2,1,0,4,8]
lista_nova = []
for i in range(len(lista)):
    if lista[i] != 4:
        lista_nova.append(lista[i])
print(lista_nova)
#ou
lista = [x for x in lista if x != 4]

# Pilha (Stack) → LIFO - pop()
pilha_livros = ['AAA', 'DDD', 'Hábitos Atômicos']
print(f'Acabei de ler o livro {pilha_livros.pop()}') #retira último elemento

# Fila (Queue) → FIFO - pop(0)
fila_lanchonete = ['Pedro', 'Enzo', 'Valentina', 'Dorinha']
print(f'Qual o seu pedido, {fila_lanchonete.pop(0)}?') #retira o primeiro elemento

numbers = [10,20,30]
indice_20 = numbers.index(20) # 1

numbers.append(10)
quantidade_10 = numbers.count(10) # 2

valores = [1,53,4,52,8,94,55]
valores.sort() #[1, 4, 8, 52, 53, 55, 94]
print(valores)

valores.reverse() # [94, 55, 53, 52, 8, 4, 1]
print(valores)

