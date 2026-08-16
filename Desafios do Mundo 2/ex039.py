"""
Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar 
ao serviço  militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o 
tempo que falta ou que passou do prazo.
Sujestão, fazer uma atualização no algoritmo para que ele pergunte o sexo da pessoa, se for Homen, a pessoa prescisa fazer o alistamento 
obrigatóriamente, se for mulhar, a pessoa não prescisa fazer o alistamento.
"""

from datetime import date
sexo = str(input('Qual é o seu sexo?[Homem/Mulher] ')).strip().upper() # pergunta o sexo da pessoa.
if sexo == 'MULHER':
    print('Você não prescisa fazer o alistamento militar obrigatório')
else:
    ano = int(input('Digite seu ano de nascimento ')) # Pede o ano de nascimento do usuário.
    ano_atual = date.today().year # Utiliza a função date para descobrir o ano atual.
    alistamento = ano_atual - ano # Calcula a idade do jovem.

# Mostra que idade uma pessoa que nasceu do ano de nascimento do jovem deverá ter no ano atual. 
    print(f'Quem nasceu em {ano} tem {alistamento} anos de idade em '
        f'{ano_atual}') 
    
# Análise de situações possíveis.
# Se o jovem tem 18 anos.
    if alistamento == 18:
        print('Está na hora de se alistar! Você ja tem 18 anos.')

# Se o jovem tem menos de 18 anos. E calculo da quantidade de anos que falta até a maioridade do jovem.
    elif alistamento < 18:
        print(f'Você ainda não completou 18 anos , por isso você deve esperar '
              f'{18 - (2024 - ano)} anos para poder se alistar.')

# Mostra em que ano será o alistamento do jovem.
        print(f'Seu alistamento será em {ano_atual + (18 - (2024 - ano))}')

# Se o jovem tem 19 anos. Ou seja passou apenas um ano do alistamento.
    elif ((2024 - ano) - 18) == 1:
        print('Você deve se alistar, pois você tem 18 anos e passou um ano do período '
              'de alistamento.')

# Mostra em que ano foi o alistamento do jovem.
        print(f'Seu alistamento foi em {ano_atual - 1}')
        
# Se o jovem tem mais de 19 anos. Ou seja passou mais de um ano do alistamento, o algoritmo calcula quanto.
    else:
        print(f'Você deve se alistar, pois você tem 18 anos e passou {(2024 - ano) - 18} anos do período'
              f'de alistamento.')

# Mostra em que ano foi o alistamento da pessoa.
        print(f'Seu alistamento será em {ano_atual - ((2024 - ano) - 18)}')
 