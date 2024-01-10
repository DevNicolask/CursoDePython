# Desafio: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Versão Não colorida.
L = float(input('Qual é a largura dessa parede? '))
h = float(input('Qual é a altura dessa parede? '))
print(f'Sabendo-se que 1 litro de tinta pinta exatamente 2 m² da parede:\n'
      f'Serão necessários {(L*h)/2:.2f} litros de tinta para pintar completamente essa parede de área {L*h:.2f}m².')

# Versão Colorida.
"""
L = float(input('\033[1;35mQual é a largura dessa parede? (Metros) \033[m'))
h = float(input('\033[1;32mQual é a altura dessa parede? (Metros) \033[m'))
print(f'\033[1;34mSabendo-se que 1 litro de tinta pinta exatamente 2 m² da parede:\n'
      f'\033[1;37mSerão necessários {(L*h)/2:.2f} litros de tinta para pintar completamente essa parede de área {L*h:.2f}m².\033[m')"""
 