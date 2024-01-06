# Versão Normal.
# Forma que eu fiz. utilizando o teorema de Pitágoras.
from math import sqrt, hypot

a = float(input('Me diga o tamanho do primeiro cateto. '))
b = float(input('Me diga o tamanho do segundo cateto. '))
print(f'O tamanho da hipotenusa desse triangulo é {sqrt(a**2+b**2):.2f}')

# Forma que o professor Guanabara fez.

a = float(input('Me diga o primeiro cateto. '))
b = float(input('Me diga o segundo cateto. '))
print(f'A hipotenusa será {hypot(a, b):.2f}.')

# Versão Colorida.
"""
# Forma que eu fiz. utilizando o teorema de Pitágoras.
from math import sqrt

a = float(input('\033[1;34mMe diga o tamanho do primeiro cateto. \033[m'))
b = float(input('\033[1;34mMe diga o tamanho do segundo cateto. \033[m'))
print(f'\033[1;36mMeO tamanho da hipotenusa desse triangulo é {sqrt(a**2+b**2):.2f}\033[m')

# Forma que o professor Guanabara fez.
from math import hypot

a = float(input('\033[1;34mMe diga o primeiro cateto. \033[m'))
b = float(input('\033[1;34mMe diga o segundo cateto. \033[m'))
print(f'\033[1;36mA hipotenusa será {hypot(a, b):.2f}\033[m')"""
