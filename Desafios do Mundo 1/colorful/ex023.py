# Desafio: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

a = int(input('\033[1;35mDigite um número de 0 a 9999 \033[m'))
print(f'\033[1;35mO algarismo das unidades:\033[m \033[1;34m{a % 10}\033[m')
print(f'\033[1;35mO algarismo das dezenas é:\033[m \033[1;34m{a // 10 % 10}\033[m')
print(f'\033[1;35mO algarismo das centenas é:\033[m \033[1;34m{a // 100 % 10}\033[m')
print(f'\033[1;35mO algarismo da unidade de milhar é:\033[m \033[1;34m{a // 1000 % 10}\033[m')
#print(f'\033[1;35mO algaridmo das dezenas:\033[m \033[1;34m{((a % 100) - (a % 10)) / 10:.0f}\033[m')
#print(f'\033[1;35mO algarismo das centenas é:\033[m \033[1;34m{((a % 1000) - (a % 100)) / 100:.0f}\033[m')
#print(f'\033[1;35mO algarismo das unidades de milhar é:\033[m \033[1;34m{((a % 10000) - (a % 1000)) / 1000:.0f}\033[m')

