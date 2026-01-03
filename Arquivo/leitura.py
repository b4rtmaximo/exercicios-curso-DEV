import os

pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, 'legendas_03.srt'
)
print(caminho_arquivo)


with open(caminho_arquivo, 'r') as arquivo:     #abrir um recurso que será fechado automaticamente quando o bloco termina
    conteudo = arquivo.read()
    print(conteudo)

with open(caminho_arquivo, 'r') as arquivo:     #Ler linha por linha
    linha = arquivo.readline()
    while linha:
        partes = linha.split()
        inicio = partes[0] if partes else ''

        print(inicio, end=', ')

        linha = arquivo.readline()

with open(caminho_arquivo, 'r') as arquivo:     #Ler linha por linha
    for linha in arquivo:
        print(linha[:5], end='*')