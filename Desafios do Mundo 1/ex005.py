# Desafio: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

# Versão Não colorida.
n = int(input('Digite um número '))
print(f'O antecessor de {n} é {n-1} e seu sucessor é {n+1}')

# Versão Colorida.
"""
n = int(input('\033[1;35m Digite um número \033[m'))
print(f'\033[1;36m O antecessor de {n} é\033[m \033[1;32m{n-1}\033[m \033[1;36me seu sucessor é\033[m \033[1;34m{n+1}\033[m')"""
 