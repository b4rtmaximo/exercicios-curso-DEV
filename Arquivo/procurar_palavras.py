import os
from listar import listar_arquivos


def ler_arquivos(pasta, arquivos):
    conteudo = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        with open (caminho, 'r') as file:
            conteudo.extend(file.read().splitlines())

    return conteudo    


def remover_numeros(linhas):
    return [linha for linha in linhas if not linha.isdigit()]


def remover_tempos(linhas_sem_numeros):
    return [linha for linha in linhas_sem_numeros if not '-->' in linha]


def contar_palavras(linhas):
    palavras = {}

    for linha in linhas:
        linha = linha.translate(
            str.maketrans('', '', '-"#$&!?.,!?;:()[]{}')
        )
        for palavra in linha.split():
            palavra = palavra.lower()
            palavras[palavra] = palavras.get(palavra, 0) + 1

    palavras = sorted(palavras.items(), key=lambda item: item[1], reverse=True)

    return palavras


def main():
    pasta = os.path.join(
        os.path.dirname(__file__), 'legendas'
    )

    legendas = listar_arquivos(pasta, "srt")
    linhas = ler_arquivos(pasta, legendas)
    linhas_sem_numeros = remover_numeros(linhas)
    linhas_filtradas = remover_tempos(linhas_sem_numeros)

    palavras = contar_palavras(linhas_filtradas)

    print(palavras)  


main()