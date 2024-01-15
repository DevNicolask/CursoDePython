# Desafio: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('\033[1;35mOs números pares entre 1 e 50 são: \033[m', end='')
for contador in range(2, 51, 2):
    print(f'\033[1;36m{contador}, \033[m', end='')
print('\033[1;35mAcabou!\033[m')
