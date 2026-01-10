def executar_divisao(tentativa=1):
    try:
        divisor = int(input('Informe o divisor: '))
        return 1000 / divisor
    except Exception as e:
        if tentativa > 5:
            raise e
        print(f'Ocorreu um erro: {e}')
        print(f'Número de tentativas: {tentativa}')
        return executar_divisao(tentativa + 1)
    
resultado = executar_divisao()
print(f'O resultado da divisão é {resultado}')

#O raise é usado para lançar (ou levantar) uma exceção manualmente. É como você está dizendo: "ocorreu um erro aqui, pare a execução normal!".

#Diferença importante:

#print("erro") → apenas exibe uma mensagem, o código continua
#raise Exception("erro") → para o programa e lança um erro

#É como a diferença entre avisar que algo está errado versus realmente interromper tudo porque algo crítico falhou!