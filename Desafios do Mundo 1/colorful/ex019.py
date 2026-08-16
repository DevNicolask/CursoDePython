# Desafio: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

nome1 = str((input('\033[1;34mMe diga o nome do primeiro aluno \033[m')))
nome2 = str((input('\033[1;36mMe diga o nome do segundo aluno \033[m')))
nome3 = str((input('\033[1;34mMe diga o nome do terceiro aluno \033[m')))
nome4 = str((input('\033[1;36mMe diga o nome do terceiro aluno \033[m')))
lista = [nome1, nome2, nome3, nome4]
print('\033[1;35mO aluno escolhido foi \033[m', choice(lista))
