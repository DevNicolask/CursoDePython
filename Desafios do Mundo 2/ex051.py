"""
Desafio: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""

numero = float(input('Digite o primeiro termo dessa PA: '))
razao = float(input('Digite a razão  dessa PA: '))
print(f'Os 10 primeiros termos dessa PA é: ', end='')
for cont in range(0, 10):
    PA = numero + (razao * cont)
    print(f'{PA} -> ', end='')
print('Acabou!')
