primeiro_nome = 'Guilherme'
sobrenome = 'Bianco'

nome_completo = primeiro_nome + ''+ sobrenome
print(nome_completo)

h = input('Hora: ')
m = input('Minuto: ')
s = input('Segundo: ')

tempo_formatado = '{}h {}m {}s'
print(tempo_formatado.format(h,m,s))

texto = """Este é o exemplo
de uma string
que ocupa várias linhas.""" 
print(texto)
print(texto.upper())
print(texto.find('ocupa'))
print(texto.split())

lista_palavras = texto.split()
print('-'.join(lista_palavras))

print(len(texto))

valor = '456'
print(valor.isnumeric())

real = '123.456'
print(real.replace('.',''))