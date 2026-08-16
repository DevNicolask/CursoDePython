# Desafio: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome. ')).strip()

# Como o professor Guanabara Fez (Mais fácil!)
print(f'Seu nome tem \"Silva\"? {'silva' in nome.lower()}')

# Como eu fiz:
print(f'Seu nome tem "Silva"? {not (nome.lower().find('silva') == -1)}')
