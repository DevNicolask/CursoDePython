# Desafio: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoa = 0
peso = float(input(f'Digite o peso da {pessoa + 1}ª pessoa (Kg): '))
menorpeso = peso
maiorpeso = peso
for pessoa in range(1, 5):
    peso = float(input(f'Digite o peso da {pessoa + 1}ª pessoa (Kg): '))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print()
print(f'A pessoa com o MAIOR peso tem {maiorpeso}Kg.\n'
      f'E a pessoa com o MENOR peso tem {menorpeso}Kg.')
