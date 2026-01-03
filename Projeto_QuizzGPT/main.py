
from rich.console import Console
from rich.prompt import Prompt
import json


console = Console()


def esperar_enter():
    console.input(
        prompt='Pressione ENTER para continuar...',
        password=True
    )


def main():
    console.clear()

    titulo = '[bold blue]Quiz GPT[/bold blue]'
    console.print(f'Bem vindo ao {titulo}!')

    gerar_quiz()


def gerar_quiz():
    pontos_usuario = 0
    continuar = 'S'
    
    topico = Prompt.ask('Qual o tópico do quiz?')
    
    while continuar.lower() != 'n':
        pergunta = gerar_pergunta(topico)
        opcoes = pergunta['opcoes']
        certa = pergunta['certa']

        console.print(f"\n[bold]{pergunta['enunciado']}[/bold]")

        for i, opcao in enumerate(opcoes, start=1):
            console.print(f'{i}. {opcao}')

        resposta_indice = int(Prompt.ask(
            prompt='Opção',
            choices=['1', '2', '3', '4']
        ))
        
        # Ajustar índice para lista (começa em 0)
        resposta = opcoes[resposta_indice - 1]
        resposta_certa = certa

        console.clear()
        
        if resposta == resposta_certa:
            console.print('[bold green]✓ Você acertou![/bold green]')
            pontos_usuario += 1
        else:
            console.print(f'[bold red]✗ Você errou.[/bold red] A resposta correta era: [bold]{resposta_certa}[/bold]')

        console.print(f'\nPontuação atual: [bold yellow]{pontos_usuario}[/bold yellow] ponto(s)\n')

        continuar = Prompt.ask(
            prompt='Deseja continuar?',
            choices=['S', 'n'],
            default='S'
        )

    console.print(f'\n[bold]Quiz finalizado![/bold]')
    console.print(f'Tópico: [cyan]{topico}[/cyan]')
    console.print(f'Pontuação final: [bold yellow]{pontos_usuario}[/bold yellow] ponto(s)')


def gerar_pergunta(topico):
    # Construir o JSON corretamente com o tópico
    pergunta_dict = {
        'enunciado': f'Você gosta do(a) {topico}?',
        'opcoes': ['Sim', 'Não', 'Que?', 'Nããããão'],
        'certa': 'Sim'
    }
    
    return pergunta_dict


if __name__ == '__main__':
    main()