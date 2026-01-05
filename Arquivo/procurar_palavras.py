import os
from listar import listar_arquivos

def main():
    pasta = os.path.join(
        os.path.dirname(__file__), 'legendas'
    )

    legendas = listar_arquivos(pasta, "srt")
    print(legendas)


main()