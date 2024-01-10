# Desafio: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será 
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

N = int(input('\033[1;35mDigite um número \033[m')) # Pede o número que vai ser convertido ao usuário.
print('\033[1;36m=-=\033[m'*10)
print('\033[1;36m     CONVERSOR DE BASES\033[m')
print('\033[1;36m=-=\033[m'*10)
print('\033[1;31m1 - BINÁRIO\033[m')
print('\033[1;32m2 - OCTAL\033[m')
print('\033[;33m3 - Hexadecimal\033[m')
print('\033[1;36m=-=\033[m'*10)
# Pede ao usuário qual a base de conversão.
conversao = int(input('\033[1;35mPara qual base você quer fazer a conversão? \033[m'))
# Análise de situações possíveis.
# Conversão para binário.
if conversao == 1:
    print('\033[1;31mConvertendo para base binária...\033[m')
    print(f'\033[1;31mO número {N} na base binária é {bin(N)[2:]}\033[m') # Utilizei a função: bin()
# Conversão para octal.
elif conversao == 2:
    print('\033[1;32mConvertendo para base octal...\033[m')
    print(f'\033[1;32mO número {N} na base octal é {oct(N)[2:]}\033[m') # Utilizei a função: oct()
# Conversão para hexadecimal.
elif conversao == 3:
    print('\033[1;33mConvertendo para base hexadecimal...\033[m')
    print(f'\033[1;33mO número {N} na base hexadecimal é {hex(N)[2:]}\033[m') # Utilizei a função: hex()
# usuário não digitou nenhum dos outros comandos. Encerra o programa
else:
    print('\033[1;35mNenhuma conversão selecionada, encerrando...\033[m')
