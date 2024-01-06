# Versão Normal.
a = int(input('Quantos dias o carro foi alugado? '))
b = float(input('Quantos quilômetros foram rodados '))
print(f'O total a pagar é {(60 * a)+(0.15 * b):.2f} reais.')

# Versão Colorida.
"""
a = int(input('\033[1;34mQuantos dias o carro foi alugado? \033[m'))
b = float(input('\033[1;32mQuantos quilômetros foram rodados \033[m'))
print(f'\033[1;35mO total a pagar é \033[1;31m{(60 * a)+(0.15 * b):.2f}\033[m\033[1;35m reais.\033[m')"""
