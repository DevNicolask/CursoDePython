# Código Normal
from random import choice
a = str((input('Me diga o name do primeiro aluno ')))
b = str((input('Me diga o name do segundo aluno ')))
c = str((input('Me diga o name do terceiro aluno ')))
d = str((input('Me diga o name do terceiro aluno ')))
e = [a, b, c, d]
print('O aluno escolhido foi ', choice(e))

# Código colorido.'
"""
from random import choice

a = str((input('\033[1;34mMe diga o nome do primeiro aluno \033[m')))
b = str((input('\033[1;36mMe diga o nome do segundo aluno \033[m')))
c = str((input('\033[1;34mMe diga o nome do terceiro aluno \033[m')))
d = str((input('\033[1;36mMe diga o nome do terceiro aluno \033[m')))
e = [a, b, c, d]
print('\033[1;35mO aluno escolhido foi \033[m', choice(e))"""
