# Versão Normal.
from math import sin, cos, tan, radians

n = float(input('Diga um ângulo em graus. '))
print(f'O SENO de {n} é {sin(radians(n)):.2f}.\nO COSSENO de {n} é {cos(radians(n)):.2f}.\n'
      f'A TANGENTE de {n} é {tan(radians(n)):.2f}.')

# Versão Colorida.
"""
from math import sin, cos, tan, radians

n = float(input('\033[1;34mDiga um ângulo em graus. \033[m'))
print(f'\033[1;35mO SENO de {n} é {sin(radians(n)):.2f}.\nO COSSENO de {n} é {cos(radians(n)):.2f}.\n'
      f'A TANGENTE de {n} é {tan(radians(n)):.2f}.\033[m')"""
