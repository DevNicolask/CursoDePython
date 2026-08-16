# Desafio: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

a = int(input('Digite um número de 0 a 9999 '))
print(f'O algarismo das unidades: {a % 10}')
print(f'O algarismo das dezenas é: {a // 10 % 10}')
print(f'O algarismo das centenas é: {a // 100 % 10}')
print(f'O algarismo da unidade de milhar é: {a // 1000 % 10}')
# print(f'O algaridmo das dezenas: {((a % 100) - (a % 10)) / 10:.0f}')
# print(f'O algarismo das centenas é: {((a % 1000) - (a % 100)) / 100:.0f}')
# print(f'O algarismo das unidades de milhar é: {((a % 10000) - (a % 1000)) / 1000:.0f}')
