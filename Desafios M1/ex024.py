# Desafio: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# Versão Não colorida.
a = str(input('Digite a cidade em que você nasceu ')).strip()
b = a.lower().split()
print(f'Você nasceu em uma cidade com nome \"Santo\" no começo? {b[0] == 'santo'}')
print(f'O nome da sua cidade tem "Santo" {a.lower().count('santo')} vezes.')

# Versão Colorida.
"""
a = str(input('\033[1;34mDigite a cidade em que você nasceu \033[m')).strip()
b = a.lower().split()
print(f'\033[1;34mVocê nasceu em uma cidade com nome \"Santo\" no começo?\033[m \033[1;35m{b[0] == 'santo'}\033[m')
print(f'\033[1;35mO nome da sua cidade tem "Santo"\033[m \033[1;35m{a.lower().count('santo')} vezes.\033[m')"""
 