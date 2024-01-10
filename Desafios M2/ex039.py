# Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar 
# ao serviço  militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o 
# tempo que falta ou que passou do prazo.

ano = int(input('\033[1;35mDigite seu ano de nascimento \033[m')) # Pede o ano de nascimento do usuário.
alistamento = 2024 - ano
# Análise de situações possíveis.
# Se o jovem tem 18 anos.
if alistamento == 18:
    print('\033[1;36mEstá na hora de se alistar! Você ja tem 18 anos.\033[m') 
# Se o jovem tem menos de 18 anos. E calculo da quantidade de anos que falta até a maioridade do jovem.
elif alistamento < 18:
    print(f'\033[1;36mVocê ainda não completou 18 anos, por isso você deve esperar {18 - (2024 - ano)} anos para poder se alistar.\033[m')
# Se o jovem tem 19 anos. Ou seja passou apenas um ano do alistamento.
elif ((2024 - ano) - 18) == 1:
    print('\033[1;36mVocê deve se alistar, pois você tem 18 anos e passou um ano do período de alistamento.\033[m')
# Se o jovem tem mais de 19 anos. Ou seja passou mais de um ano do alistamento, o algoritmo calcula quanto.
else:
    print(f'\033[1;36mVocê deve se alistar, pois você tem 18 anos e passou {(2024 - ano) - 18} anos do período de alistamento.\033[m')
