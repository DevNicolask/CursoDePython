# Desafio: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

numero = float(input('\033[1;36mDigite o primeiro termo dessa PA: \033[m'))
razao = float(input('\033[1;36mDigite a razão  dessa PA: \033[m'))
print(f'\033[1;36mOs 10 primeiros termos dessa PA é: \033[m', end='')
for cont in range(0, 10):
    PA = numero + (razao * cont)
    print(f'\033[1;35m{PA} -> \033[m', end='')
print('\033[1;36mAcabou!\033[m')
