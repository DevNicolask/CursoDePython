# Desafio: Faça um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

quantpar = 0
soma = 0
for cont in range(1, 7):
    numero = float(input(f'\033[1;35mDigite o {cont}° número: \033[m'))
    if numero % 2 == 0:
        quantpar += 1
        soma += numero
print(f'\033[1;35mA soma de todos os\033[m \033[1;36m{quantpar}\033[m \033[1;35mnúmeros pares que você digitou é\033[m'
      f' \033[1;36m{soma}.\033[m')
