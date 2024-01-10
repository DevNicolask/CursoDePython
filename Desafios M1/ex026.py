# Desafio: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Versão Não colorida.
a = str(input('Digite uma frase. ')).lower().strip()
print('Analisando frase...')
print(f'A letra "A" aparece {a.count('a')} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição {a.find('a'[0]) + 1}.')
print(f'A letra "A" aparece pela ultima vez na posição {a.rfind('a'[0]) + 1}.')

# Versão Colorida.
"""
a = str(input('\033[1;35mDigite uma frase. \033[m')).lower().strip()
print('\033[1;36mAnalisando frase...\033[m')
print(f'\033[1;35mA letra\033[m \033[1;33m"A"\033[m \033[1;35maparece\033[m \033[1;36m{a.count('a')} vezes.\033[m')
print(f'\033[1;35mA letra\033[m \033[1;33m"A"\033[m \033[1;35maparece pela primeira vez na posição\033[m '
      f'\033[1;36m{a.find('a'[0]) + 1}\033[m')
print(f'\033[1;35mA letra\033[m \033[1;33m"A"\033[m \033[1;35maparece pela ultima vez na posição\033[m '
      f'\033[1;36m{a.rfind('a'[0]) + 1}\033[m')"""
