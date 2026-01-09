def repetir(func, vezes=1):
    for _ in range(vezes):
        func()


def bom_dia():
    print('Bom dia!')


bom_dia()

repetir(bom_dia)

#Funções como objetos: Note que em repetir(bom_dia) você passa a função sem os parênteses (), ou seja, está passando a própria função como argumento, não o resultado dela
#Parâmetros padrão: O parâmetro vezes=1 define um valor padrão se não for especificado
#Higher-order function: repetir é uma função que recebe outra função como argumento