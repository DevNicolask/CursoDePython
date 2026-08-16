"""
Desafio: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

maior = 0
for pessoa in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da {pessoa + 1}ª pessoa: '))
    ano_atual = date.today().year
    if ano_atual - ano >= 21:
        maior += 1
print()
print(f'Foram digitadas {maior} pessoas que são MAIOR '
      f'de idade.\nE foram digitadas {7 - maior} pessoas que são '
      f'MENOR de idade.')
