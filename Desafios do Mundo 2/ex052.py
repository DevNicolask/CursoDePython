# Desafio: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

analizador = 0
numero = int(input('Digite um número: '))
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print(f' {cont} ', end='')
        analizador += 1
    else:
        print(f' {cont} ', end='')
print()
if analizador == 2:
    print(f'Seu número É PRIMO. Ele foi divisivel {analizador} '
          f'vezes.')
else:
    print(f'Seu número NÃO É PRIMO. Ele foi divisivel {analizador} '
          f'vezes.')
