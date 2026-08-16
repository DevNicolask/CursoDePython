# Desafio: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

a = int(input('Me diga um número qualquer. ')) # Pede um número ao usuário.

# Testa as possibilidades de acordo com o resto do número por 2.
if a % 2 == 0:
    print('Seu número é PAR.') # Se o número for par
else:
    print('Seu número é IMPAR.') # Se o número for impar
