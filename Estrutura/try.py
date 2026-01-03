localizador = 20
if localizador > 10:
	print('Tá de boa!')
elif localizador == 10:
	print("Felicia está por perto")
elif localizador >=7:
	print("Fiquem de olho!")
elif localizador >=3:
	print("Se escondam!")
else:
	print("É agora ou nunca")
	

livros_phineas = ['livro1', 'livro2', 'livro3']
livros_pherb = ['livroA', 'livroB', 'livroC', 'livroD', 'livroE']

print('Lista de Livros do Phineas:')
for livro in livros_phineas:
	print(livro)
print('Lista de Livros do Pherb:')
for livro in livros_pherb:
	print(livro)

if len(livros_pherb) > len(livros_phineas):
	print('O Pherb leu mais livros!')
elif len(livros_pherb) == len(livros_phineas):
	print('Phineas e Pherb leram a mesma quantidade de livros.')
else:
	print('O Phines leu mais livros!')
	
'''
Ela já tem 45, mas se os produtores acharem 12 cardigãs ou 31 suéteres, 
ela precisa comprar apenas mais 8 casacos. Se Emily convencer a Chanel, 
precisará de 2 casacos apenas. Se tudo der errado ela vai precisar comprar 18 casacos.'''

casacos_miranda = 45
numero_cardigans = int(input('Os produtores acharam quantos cardigãs?: '))
numero_sueteres = int(input('Os produtores acharam quantos suéteres?: '))
resposta_emily = input('Emily conseguiu convencer a Chanel? [S/N]: ')


if resposta_emily == 'S':
	print('Miranda precisa comprar mais 2 casacos.')
elif numero_cardigans == 12 or numero_sueteres == 31:
	print('Miranda precisa comprar mais 8 casacos.')
else:
	print('Miranda precisará comprar mais 18 casacos.')

#--------------------------------------------------------------------------------------------
'''Darth Vader quer saber se um novo recruta é sensível à Força para recrutá-lo imediatamente 
ou dispensá-lo.

- Se a variável `sensivel_a_forca` for `True`, imprima: "Bem-vindo ao Império. Sua jornada 
começa agora! 🌑"
- Caso contrário, imprima: "Próximo! Este não é o droid que estamos procurando."'''

sensivel_a_forca = True
if sensivel_a_forca == True:
	print("Bem-vindo ao Império. Sua jornada começa agora! 🌑")
else:
	print("Próximo! Este não é o droid que estamos procurando.")

#--------------------------------------------------------------------------------------------
'''Scooby e Salsicha querem saber quantos *Scooby Snacks* eles têm para o dia. Crie uma lista 
e use um *loop* para contar o total.

- Lista: `["snack", "snack", "vazio", "snack", "snack"]`
- Use um `for` para iterar e contar apenas os itens que são `"snack"`.'''

lanches = ["snack", "snack", "vazio", "snack", "snack"]
snacks = 0
for i in lanches:
	if i == 'snack':
		snacks += 1
print(f'Scooby e Salsicha têm {snacks} snacks.')

#--------------------------------------------------------------------------------------------
'''Bob Esponja precisa de um sistema para saber se pode aceitar um pedido de Hambúrguer de Siri.

- Se for *durante* o horário de pico (variável `horario_pico = True`), **E** 
tiver ingredientes (`tem_ingredientes = True`), aceite o pedido.
- Se for horário de pico, **MAS** faltar ingrediente, cancele.
- Se *não* for horário de pico, aceite o pedido, **independente** dos ingredientes.'''

horario_pico = True
tem_ingredientes = True

if not horario_pico or tem_ingredientes:
    print('Pedido aceito!')
else:
    print('Pedido cancelado!')

#--------------------------------------------------------------------------------------------
'''Os Vingadores precisam saber quantos membros são de "Nível Beta" (poder entre 50 e 75, inclusive) 
e quantos são "Nível Alfa" (acima de 75).

- Use um `for` para iterar e contar.
- Lista para usar: `niveis_poder = [90, 45, 60, 82, 75, 50, 30, 99]`'''

niveis_poder = [90, 45, 60, 82, 75, 50, 30, 99]
beta  = 0
alfa = 0
for i in niveis_poder:
	if i >= 50 and i <=75:
		beta += 1		
	elif i>75:
		alfa += 1
print(f'Membros Nível Beta: {beta}')
print(f'Membros Nível Alfa: {alfa}')		
#--------------------------------------------------------------------------------------------
'''O Império está procurando o planeta *Kyber* para coletar cristais. Use uma *flag* 
(bandeira booleana) para indicar se ele foi encontrado na lista de planetas explorados.

- Lista para usar: `planetas_explorados = ["Tatooine", "Hoth", "Endor", "Coruscant", "Naboo"]`'''

encontrado = False
planetas_explorados = ["Tatooine", "Hoth", "Endor", "Coruscant", "Naboo"]
for i in planetas_explorados:
	if i == 'Kyber':
		print('Planeta Kyber encontrado!')
		encontrado = True

if encontrado:
	print('Explorar cristais de Kyber')
else:
	print('Sem cristais para explorar.')
	
