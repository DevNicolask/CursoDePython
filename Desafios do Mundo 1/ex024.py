# Desafio: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

a = str(input('Digite a cidade em que você nasceu ')).strip()
b = a.lower().split()
print(f'Você nasceu em uma cidade com nome \"Santo\" no começo? {b[0] == 'santo'}')
print(f'O nome da sua cidade tem "Santo" {a.lower().count('santo')} vezes.')
