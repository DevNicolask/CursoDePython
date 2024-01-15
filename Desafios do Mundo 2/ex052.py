# Desafio: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

analizador = 0
numero = int(input('\033[1;35mDigite um número: \033[m'))
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print(f'\033[1;36m {cont} \033[m', end='')
        analizador += 1
    else:
        print(f'\033[1;31m {cont} \033[m', end='')
print()
if analizador == 2:
    print(f'\033[1;35mSeu número É PRIMO. Ele foi divisivel\033[m \033[1;36m{analizador}\033[m '
          f'\033[1;35mvezes.\033[m')
else:
    print(f'\033[1;35mSeu número NÃO É PRIMO. Ele foi divisivel\033[m \033[1;36m{analizador}\033[m '
          f'\033[1;35mvezes.\033[m')
 