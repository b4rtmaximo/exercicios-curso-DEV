valor1 = int(input('Informe o Primeiro Número: '))
valor2 = int(input('Informe o Segundo Número: '))

resultado = 0
operacao = input('Informe a operação [+ - * /]: ')

match operacao:
    case '+': 
        resultado = valor1 + valor2
    case '-': 
        resultado = valor1 - valor2
    case '*' | 'x': 
        resultado = valor1 * valor2
    case '/':
        resultado = valor1 / valor2
    case _:
        print('Operação não encontrada.')

print(f'O resultado é {resultado}.')

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

nome = 'Leonardo Silva Pareira Matos'
partes_nome = nome.split()

match partes_nome:
    case [primeiro]:
        sigla = primeiro[:2].upper()
 #   case [primeiro, segundo]:
 #       sigla = primeiro[0] + segundo[0].upper()
    case [primeiro, nomes_do_meio, ultimo]:
        sigla = primeiro[0] + ultimo[0].upper()
    case _:
        sigla = 'US'

print(f'A sigla do usuário {nome} é {sigla}')
