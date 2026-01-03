funcionario = {
    'nome': 'João Pedro',
    'idade': 31,
    'cidade': 'SP',
    'ativo': True
}

print(funcionario['nome'])

funcionario['profissao'] = 'Engenheiro Eletricista'
print(funcionario['profissao'])

print(funcionario.get('nome'))

print(funcionario.get('salario')) #apesar do valor ñ existir, o .get não gera ERRO
print(funcionario.get('salario', 0)) 

print(funcionario.keys())   #chaves
print(funcionario.values()) #valores
print(funcionario.items())  #tudo

funcionario['ativo'] = False
funcionario.update({
    'idade': 27, 
    'ativo': True, 
    'profissao': 'reporter'
})

cidade = funcionario.pop('cidade') #dicionáro perde o atributo 'cidade'
print(cidade)

funcionario.clear()
print(funcionario)