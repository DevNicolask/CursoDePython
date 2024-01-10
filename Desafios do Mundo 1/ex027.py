# Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

# Versão Não colorida.
a = str(input('Escreva seu nome. ')).strip()
b = a.split()

# Minha Versão.
print(f'Muito prazer em te conhecer {a}!\nO seu primeiro nome é {b[0]} e seu ultimo nome é {b[-1]}.')

# Versão do Professor Guanabara.
# print(f'Muito prazer em te connhecer {a}.\nSeu primeiro nome é {b[0]} e seu ultimo nome é {b[len(b) - 1]}!')

# Versão Colorida.
"""
a = str(input('\033[1;35mEscreva seu nome. \033[1;35m')).strip()
b = a.split()

# Minha versão
print(f'\033[1;35mMuito prazer em te conhecer\033[1;35m \033[1;36m{a}!\033[m\n\033[1;35mO seu primeiro nome é\033[m '
      f'\033[1;36m{b[0]}\033[m \033[1;35me seu ultimo nome é\033[m \033[1;36m{b[-1]}\033[m.')

# Versão do Professor Guanabara.
# print(f'\033[1;35mMuito prazer em te connhecer\033[m \033[1;36m{a}.\033[m\n\033[1;35mSeu primeiro nome é\033[m '
#      f'\033[1;36m{b[0]}\033[m \033[1;35me seu ultimo nome é\033[m \033[1;36m{b[len(b) - 1]}.\033[m!')"""
 