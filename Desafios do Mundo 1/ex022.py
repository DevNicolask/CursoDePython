# Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras têm ao todo (sem considerar espaços).
# - Quantas letras têm o primeiro nome.

# Versão Não colorida.
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

# Versão Colorida.
"""
nome = str(input('\033[1;34mQual é o seu nome? \033[m')).strip()
print('\033[1;34mAnalisando seu nome...\033[m')
print(f'\033[1;35m1. Seu nome com todas as letras maiuculas é:\033[m \033[1;34m{nome.upper()}.\033[m')
print(f'\033[1;35m2. Seu nome com todas as letras minusculas é:\033[m \033[1;34m{nome.lower()}.\033[m')
print(f'\033[1;35m3. Seu nome ao todo tem\033[m \033[1;34m{len(nome) - nome.count(' ')} letras.\033[m')
# a = ''.join(nome.split())
# print(f'\033[1;35m3. Seu nome ao todo tem\033[m {len(a)} letras.')
print(f'\033[1;35mSeu ultimo nome tem\033[m \033[1;34m{nome.find(' '[0])} letras\033[m')
b = nome.split()
print(f'\033[1;35m4. E seu primeiro nome\033[m \033[1;34m"{b[0]}"\033[m \033[1;35mtem\033[m '
      f'\033[1;34m{len(b[0])} letras.\033[m')"""
 