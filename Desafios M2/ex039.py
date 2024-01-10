# Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar 
# ao serviço  militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o 
# tempo que falta ou que passou do prazo.
# Sujestão, fazer uma atualização no algoritmo para que ele pergunte o sexo da pessoa, se for Homen, a pessoa prescisa fazer o alistamento 
# obrigatóriamente, se for mulhar, a pessoa não prescisa fazer o alistamento.

from datetime import date
sexo = str(input('\033[1;36mQual é o seu sexo?[Homem/Mulher] ')).strip().upper() # pergunta o sexo da pessoa.
if sexo == 'MULHER':
    print('\033[1;35mVocê não prescisa fazer o alistamento militar obrigatório\033[m')
else:
    ano = int(input('\033[1;35mDigite seu ano de nascimento \033[m')) # Pede o ano de nascimento do usuário.
    ano_atual = date.today().year # Utiliza a função date para descobrir o ano atual.
    alistamento = ano_atual - ano # Calcula a idade do jovem.
    # Mostra que idade uma pessoa que nasceu do ano de nascimento do jovem deverá ter no ano atual. 
    print(f'\033[1;36mQuem nasceu em\033[m \033[1;35m{ano}\033[m \033[1;36mtem\033[m \033[1;35m{alistamento}\033[m \033[1;36manos de idade em\033[m '
        f'\033[1;35m{ano_atual}\033[m') 
    # Análise de situações possíveis.
    # Se o jovem tem 18 anos.
    if alistamento == 18:
        print('\033[1;36mEstá na hora de se alistar! Você ja tem\033[m \033[1;35m18 anos.\033[m') 
    # Se o jovem tem menos de 18 anos. E calculo da quantidade de anos que falta até a maioridade do jovem.
    elif alistamento < 18:
        print(f'\033[1;36mVocê ainda não completou\033[m \033[1;35m18 anos\033[m \033[1;36m, por isso você deve esperar\033[m '
            f'\033[1;35m{18 - (2024 - ano)}\033[m \033[1;36manos para poder se alistar.\033[m')
    # Mostra em que ano será o alistamento do jovem.
        print(f'\033[1;36mSeu alistamento será em\033[m \033[1;35m{ano_atual + (18 - (2024 - ano))}\033[m')
    # Se o jovem tem 19 anos. Ou seja passou apenas um ano do alistamento.
    elif ((2024 - ano) - 18) == 1:
        print('\033[1;36mVocê deve se alistar, pois você tem\033[m \033[1;35m18 anos\033[m \033[1;36me passou um ano do período de alistamento.\033[m')
    # Mostra em que ano foi o alistamento do jovem.
        print(f'\033[1;36mSeu alistamento foi em\033[m \033[1;35m{ano_atual - 1}\033[m')
    # Se o jovem tem mais de 19 anos. Ou seja passou mais de um ano do alistamento, o algoritmo calcula quanto.
    else:
        print(f'\033[1;36mVocê deve se alistar, pois você tem 18 anos e passou\033[m \033[1;35m{(2024 - ano) - 18}\033[m \033[1;36manos do período '
            f'de alistamento.\033[m')
    # Mostra em que ano foi o alistamento da pessoa.
        print(f'\033[1;36mSeu alistamento será em\033[m \033[1;35m{ano_atual - ((2024 - ano) - 18)}\033[m')
