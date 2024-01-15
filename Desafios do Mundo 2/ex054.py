# Desafio: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
for pessoa in range(0, 7):
    ano = int(input(f'\033[1;35mDigite o ano de nascimento da\033[m \033[1;36m{pessoa + 1}ª pessoa: \033[m'))
    ano_atual = date.today().year
    if ano_atual - ano >= 21:
        maior += 1
print()
print(f'\033[1;35mForam digitadas\033[m \033[1;36m{maior}\033[m \033[1;35mpessoas que são\033[m \033[1;36mMAIOR\033[m '
      f'\033[1;35mde idade.\nE foram digitadas\033[m \033[1;36m{7 - maior}\033[m \033[1;35mpessoas que são\033[m '
      f'\033[1;36mMENOR\033[m \033[1;35mde idade.\033[m')
 