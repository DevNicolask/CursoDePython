# Desafio: Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.

# Versão Não colorida.
a = float(input('Temperatura em graus célcius: '))
print(f'Essa temperatura em fahrenheit é igual a {(9*a/5)+32:.2f}°F e em Kelvin é {a+273:.0f} K.')

# Versão Colorida.
"""
a = float(input('\033[1;35mTemperatura em graus célcius: \033[m'))
print(f'\033[1;36mEssa temperatura em fahrenheit é igual a \033[1;31m{(9*a/5)+32:.2f}°F\033[m'
      f'\033[1;36m e em Kelvin é\033[m \033[1;37m{a+273:.0f} K\033[m.')"""
 