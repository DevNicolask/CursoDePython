# Desafio: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

# Mostra o Menú do Analizador de triângulos.
print('\033[1;33m', '-=' * 30)
print(' ' * 15, 'ANALIZADOR DE TRIÂNGULOS')
print('-=' * 30, '\033[0m')

# Pede o comprimento das retas que formam o triângulo.
a = int(input('\033[34mDigite o comprimento da primeira reta. \033[m'))
print('\033[1;33m-=\033[m' * 30)
b = int(input('\033[34mDigite o comprimento da segunda reta. \033[m'))
print('\033[33m-=\033[m' * 30)
c = int(input('\033[34mDigite o comprimento da terceira reta. \033[m'))
print('\033[33m-=\033[m' * 30)

# Testa as condições de existência de um triângulo.
if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f'\033[1;31mSuas retas ({a}, {b} e {c}) FORMAM um triângulo.\033[m')
else:
    print(f'\033[1;32mSuas retas ({a}, {b} e {c}) NÃO FORMAM um triângulo.\033[m')
print('\033[33m-=\033[m' * 30)
