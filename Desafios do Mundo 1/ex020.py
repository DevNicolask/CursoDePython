# Desafio: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre 
# a ordem sorteada.

# Versão Não colorida.
from random import shuffle

nome1 = str(input('Diga o nome do primeiro aluno: '))
nome2 = str(input('Diga o nome do segundo aluno: '))
nome3 = str(input('Diga o nome do terceiro aluno: '))
nome4 = str(input('Diga o nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A sequência de alunos escolhida foi:')
print(lista)

# Versão Colorida.
"""
from random import shuffle

nome1 = str(input('\033[1;35mDiga o nome do primeiro aluno: \033[m'))
nome2 = str(input('\033[1;35mDiga o nome do segundo aluno: \033[m'))
nome3 = str(input('\033[1;35mDiga o nome do terceiro aluno: \033[m'))
nome4 = str(input('\033[1;35mDiga o nome do quarto aluno: \033[m'))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('\033[1;34mA sequência de alunos escolhida foi: \033[m')
print(lista)"""
