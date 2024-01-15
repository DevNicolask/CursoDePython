# Desafio: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoa = 0
peso = float(input(f'\033[1;35mDigite o peso da\033[m \033[1;36m{pessoa + 1}ª pessoa (Kg): \033[m'))
menorpeso = peso
maiorpeso = peso
for pessoa in range(1, 5):
    peso = float(input(f'\033[1;35mDigite o peso da\033[m \033[1;36m{pessoa + 1}ª pessoa (Kg): \033[m'))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print()
print(f'\033[1;35mA pessoa com o\033[m \033[1;36mMAIOR\033[m \033[1;35mpeso tem\033[m \033[1;35m{maiorpeso}Kg.\033[m\n'
      f'\033[1;35mE a pessoa com o\033[m \033[1;36mMENOR\033[m \033[1;35mpeso tem\033[m \033[1;35m{menorpeso}Kg.\033[m')
 