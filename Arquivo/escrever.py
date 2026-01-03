import os

pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, 'novo_arquivo.txt'
)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Olá! Estou criando um arquivo com Python.')

linhas = [
    'Escrevendo multiplas linhas',
    'em um arquivo de texto',
    'com Python'
]

with open(caminho_arquivo, 'w') as arquivo:
    for linha in linhas:
        arquivo.writelines(f'{linha}\n')

with open(caminho_arquivo, 'a') as arquivo:
    arquivo.writelines('\n' + linha for linhas in linhas)