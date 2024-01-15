# Desafio: Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as 
# informações possíveis sobre ele.

# Versão Não colorida.
a = input('Digite algo ')
print(f'{a} é de qual tipo primtivo? ', type(a))
print(f'{a} é numérico? ', a.isnumeric())
print(f'{a} é alfabético? ', a.isalpha())
print(f'{a} é alfa numérico? ', a.isalnum())
print(f'{a} é um espaço? ', a.isspace())
print(f'{a} tem apenas letras maiúsculas? ', a.isupper())
print(f'{a} team apenas letras minúsculas? ', a.islower())
print(f'{a} tem a inicial maiúscula?(capitalizated) ', a.istitle())

# Versão Colorida, utilizando um dicionário!
"""cores = {
    'reset': '\033[m',
    'preto': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'violeta': '\033[1;35m',
    'ciano': '\033[1;36m',
    'cinza': '\033[1;37m'
        }
a = input(f'{cores['azul']}Digite algo {cores['reset']}')
print(f'{cores['ciano']}{a} é de qual tipo primtivo? {cores['reset']}', type(a))
print(f'{cores['verde']}{a} é numérico? {cores['reset']}', a.isnumeric())
print(f'{cores['cinza']}{a} é alfabético? {cores['reset']}', a.isalpha())
print(f'{cores['vermelho']}{a} é alfa numérico? {cores['reset']}', a.isalnum())
print(f'{cores['violeta']}{a} é um espaço? {cores['reset']}', a.isspace())
print(f'{cores['preto']}{a} tem apenas letras maiúsculas? {cores['reset']}', a.isupper())
print(f'{cores['azul']}{a} team apenas letras minúsculas? {cores['reset']}', a.islower())
print(f'{cores['verde']}{a} tem a inicial maiúscula?(capitalizated) {cores['reset']}', a.istitle())"""
