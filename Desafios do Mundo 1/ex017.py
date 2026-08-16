# Desafio: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa na tela.

# Forma que eu fiz. utilizando o teorema de Pitágoras.
from math import sqrt

a = float(input('Me diga o tamanho do primeiro cateto. '))
b = float(input('Me diga o tamanho do segundo cateto. '))
print(f'O tamanho da hipotenusa desse triangulo é {sqrt(a**2+b**2):.2f}')
