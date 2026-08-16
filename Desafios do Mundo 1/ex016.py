# Desafio: Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.

from math import floor, trunc

# 1ª Forma que eu usei para resolver o desafio.
n = float(input('Diga-me um número real. '))
print(f'A parte inteira de {n} é {int(n)}.')

# 2ª Forma que eu usei pra resolver o desafio.
n = float(input('Me diga um número real. '))
print(f'A parte inteira do número {n} é {floor(n)}')

# Forma que o Professor Guanabara fez pra resolver o desafio.
n = float(input('Me diga um número real. '))
print(f'A parte inteira do número {n} é {trunc(n)}')
