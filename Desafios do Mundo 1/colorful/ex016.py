# Desafio: Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.

from math import floor, trunc

# 1ª Forma que eu usei para resolver o desafio.
n = float(input('\033[1;35mDiga-me um número real. \033[m'))
print(f'\033[1;36mA parte inteira de {n} é {int(n)}.\033[m')

# 2ª Forma que eu usei pra resolver o desafio.
n = float(input('\033[1;35mMe diga um número real. \033[m'))
print(f'\033[1;36mA parte inteira do número {n} é {floor(n)}\033[m')

# Forma que o Professor Guanabara fez pra resolver o desafio.
n = float(input('\033[1;35mMe diga um número real. \033[m'))
print(f'\033[1;36mA parte inteira do número {n} é {trunc(n)}\033[m')
