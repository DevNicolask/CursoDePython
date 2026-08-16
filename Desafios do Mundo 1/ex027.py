# Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

a = str(input('Escreva seu nome. ')).strip()
b = a.split()
print(f'Muito prazer em te conhecer {a}!\nO seu primeiro nome é {b[0]} e seu ultimo nome é {b[-1]}.')
