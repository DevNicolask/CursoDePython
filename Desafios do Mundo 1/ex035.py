# Desafio: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

# Mostra o Menú do Analizador de triângulos.
print('', '-=' * 30)
print(' ' * 15, 'ANALIZADOR DE TRIÂNGULOS')
print('-=' * 30, '')

# Pede o comprimento das retas que formam o triângulo.
a = int(input('Digite o comprimento da primeira reta. '))
print('-=' * 30)
b = int(input('Digite o comprimento da segunda reta. '))
print('-=' * 30)
c = int(input('Digite o comprimento da terceira reta. '))
print('-=' * 30)

# Testa as condições de existência de um triângulo.
if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f'Suas retas ({a}, {b} e {c}) FORMAM um triângulo.')
else:
    print(f'Suas retas ({a}, {b} e {c}) NÃO FORMAM um triângulo.')
print('-=' * 30)
