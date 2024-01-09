ano = int(input('\033[1;35mDigite seu ano de nascimento \033[m'))
alistamento = 2024 - ano
if alistamento == 18:
    print('\033[1;36mEstá na hora de se alistar! Você ja tem 18 anos.\033[m')
elif alistamento < 18:
    print(f'\033[1;36mVocê ainda não completou 18 anos, por isso você deve esperar {18 - (2024 - ano)} anos para poder se alistar.\033[m')
elif ((2024 - ano) - 18) == 1:
    print('\033[1;36mVocê deve se alistar, pois você tem 18 anos e passou um ano do período de alistamento.\033[m')
else:
    print(f'\033[1;36mVocê deve se alistar, pois você tem 18 anos e passou {(2024 - ano) - 18} anos do período de alistamento.\033[m')
