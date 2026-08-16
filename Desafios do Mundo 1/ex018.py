# Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e 
# tangente desse ângulo.

from math import sin, cos, tan, radians

n = float(input('Diga um ângulo em graus. '))
print(f'O SENO de {n} é {sin(radians(n)):.2f}.\nO COSSENO de {n} é {cos(radians(n)):.2f}.\n'
      f'A TANGENTE de {n} é {tan(radians(n)):.2f}.')
