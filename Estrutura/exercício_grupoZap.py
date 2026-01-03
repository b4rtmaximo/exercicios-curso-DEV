#Simulação de Cliente (Business Partner)

assinatura = input('Possui a assinatura do plano? [S/N]: ')[0].upper()
conclusao = int(input('Percentual do curso concluído[0-100]: '))

if assinatura == 'S' and conclusao >= 80:
    print('Módulo liberado!')
else:
    print('Módulo Bloqueado: ')
    if assinatura == 'N':
        print('Você não é um assinante.')
    if conclusao < 80:
        print('Você não completou o mínimo do Módulo Básico.')

#Fitness Pro 

usuario_logado = True
status_pagamento = True

if usuario_logado and status_pagamento:
    print("Acesso liberado ao Painel Premium.")
else:
    print("Acesso negado ao Painel de Premium.")
    if not usuario_logado:
        print("ERRO: Você precisa fazer login primeiro.")
    if not status_pagamento:
        print("ERRO: Por favor, regularize seu pagamento da mensalidade.")


## Desafio construção de condições

### 1. Intervalo Fechado
#- **Descrição:** Construa a condição que verifica se o **número de anos de uma pessoa** é 
# **maior ou igual a 18** **E** **menor que 60** (período de contribuição padrão).

idade = int(input('Informe quantos anos você tem: '))
if idade >= 18 and idade < 60:
    print(f'Idade = {idade}. Período de contribuição padrão')
else:
    print(f'Idade = {idade}. Fora do período de contribuição')

### 2. Acesso Duplo
#- **Descrição:** Construa a condição que verifica se um usuário pode acessar um recurso 
#se ele for **Estudante Ativo** **OU** se ele tiver um **Código de Autorização Válido**.

status_estudante = True
codigo_autorizacao = True
if status_estudante or codigo_autorizacao:
    print('Acesso Concedido.')
else:
    print('Acesso Negado.')

### 3. Exclusão de Status
#- **Descrição:** Construa a condição que verifica se o **status de uma transação** **NÃO é igual** a "Cancelada".

status_transacao = "Aprovada"
if status_transacao != "Cancelada":
    print('Transação OK')
else:
    print('Transação não autorizada - Status: Cancelada')

### 4. Combo de Filtros
#- **Descrição:** Construa a condição que libera um *download* se o **nível de assinatura** for 
#"Premium" **E** o **crédito disponível** for suficiente, **OU** se o **tipo de conteúdo** for "Gratuito".

nivel_assinatura = input('Informe o seu plano [Free/Premium]: ').lower()
credito = int(input('Informe o número de créditos: '))
tipo_conteudo = input('Conteúdo Gratuito?[S/N]: ').upper()
if tipo_conteudo == 'S' or (nivel_assinatura == 'premium' and credito > 0):
    print('Download Liberado!')
else:
    print('Download Bloqueado!')

### 5. Checagem de Limite
#- **Descrição:** Construa a condição que verifica se a **quantidade atual de itens no estoque** 
#é **menor que 10** **OU** se a **quantidade atual de itens no estoque** é **igual a 0**.

estoque_atual = int(input('Informe a quantidade de ítens do estoque: '))
if estoque_atual < 10 or estoque_atual == 0:
    if estoque_atual == 0:
        print('ESTOQUE ZERADO!')
    else:
        print(f'Atenção! Estoque possui somente {estoque_atual} ítens. Realizar a compra de novos produtos.')
else:
    print(f'Estoque OK! --> {estoque_atual} ítens.')

### 6. Dupla Condição Negativa
#- **Descrição:** Construa a condição que verifica se um **candidato** **NÃO está na lista de espera
#** **E** se o **seu tempo de experiência** **NÃO é maior que 5 anos**.

candidato_lista = input('Encontra-se na lista de espera? [S/N]: ')[0].upper()
tempo_xp = int(input('Possui quantos anos de experiência?: '))
if candidato_lista == 'N' and tempo_xp < 5:
    print('Você não está na lista e não possui experiência suficiente.')
else:
    if candidato_lista == 'S' and tempo_xp < 5:
        print('Você está na lista, mas não possui experiência suficiente.')
    elif candidato_lista == 'N' and tempo_xp > 5:
        print('Você possui experiência suficiente, mas não está na lista.')
    else:
        print('Você não está na lista e possui experiência suficiente!')