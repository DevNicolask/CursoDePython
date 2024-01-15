# Desafio: Faça um programa que calcule a soma de todos os números impares que são multiplos de três, e que seencontram
# no intervalo de 1 até 500.

quantidade = 0
soma = 0
for contador in range(1, 500):
    if contador % 2 == 1 and contador % 3 == 0:
        quantidade += 1
        soma += contador
print(f'\033[1;35mA soma de todos os\033[m \033[1;36m{quantidade}\033[m \033[1;35mnúmeros ímpares e múltiplos de 3, '
      f'no intervalo de 1 ate 500 é\033[m \033[1;36m{soma}.\033[m')
 