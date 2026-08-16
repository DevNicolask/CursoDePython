"""
Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras têm ao todo (sem considerar espaços).
- Quantas letras têm o primeiro nome.
"""

nome = str(input('Qual é o seu nome? ')).strip()
print('Analisando seu nome... ')
print(f'1. Seu nome com todas as letras maiuculas é: {nome.upper()}.')
print(f'2. Seu nome com todas as letras minusculas é: {nome.lower()}.')
print(f'3. Seu nome ao todo tem {len(nome) - nome.count(' ')} letras.')
# a = ''.join(nome.split())
# print(f'3. Seu nome ao todo tem {len(a)} letras.')
print(f'Seu ultimo nome tem {nome.find(' '[0])} letras')
b = nome.split()
print(f'4. E seu primeiro nome "{b[0]}" tem {len(b[0])} letras.')
