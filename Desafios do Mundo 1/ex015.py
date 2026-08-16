"""
Desafio: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, 
a quantidade de dias pelos quais ele foi alugado e calcule o preço a pagar. Sabendo que o carro 
custa R$60 por dia e R$0,15 por Km rodado.
"""

a = int(input('Quantos dias o carro foi alugado? '))
b = float(input('Quantos quilômetros foram rodados '))
print(f'O total a pagar é {(60 * a)+(0.15 * b):.2f} reais.')
