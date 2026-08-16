# Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

a = str(input('\033[1;35mEscreva seu nome. \033[1;35m')).strip()
b = a.split()
print(f'\033[1;35mMuito prazer em te conhecer\033[1;35m \033[1;36m{a}!\033[m\n\033[1;35mO seu primeiro nome é\033[m'
      f'\033[1;36m{b[0]}\033[m \033[1;35me seu ultimo nome é\033[m \033[1;36m{b[-1]}\033[m.')
