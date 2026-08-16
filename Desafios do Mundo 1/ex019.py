# Desafio: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
nome1 = str((input('Me diga o nome do primeiro aluno ')))
nome2 = str((input('Me diga o nome do segundo aluno ')))
nome3 = str((input('Me diga o nome do terceiro aluno ')))
nome4 = str((input('Me diga o nome do terceiro aluno ')))
lista = [nome1, nome2, nome3, nome4]
print('O aluno escolhido foi ', choice(lista))
