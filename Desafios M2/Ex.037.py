N = int(input('\033[1;35mDigite um número \033[m'))
print('\033[1;36m=-=\033[m'*10)
print('\033[1;36m     CONVERSOR DE BASES\033[m')
print('\033[1;36m=-=\033[m'*10)
print('\033[1;31m1 - BINÁRIO\033[m')
print('\033[1;32m2 - OCTAL\033[m')
print('\033[;33m3 - Hexadecimal\033[m')
print('\033[1;36m=-=\033[m'*10)
conversao = int(input('\033[1;35mPara qual base você quer fazer a conversão? \033[m'))
if conversao == 1:
    print('\033[1;31mConvertendo para base binária...\033[m')
    print(f'\033[1;31mO número {N} na base binária é {bin(N)[2:]}\033[m')
elif conversao == 2:
    print('\033[1;32mConvertendo para base octal...\033[m')
    print(f'\033[1;32mO número {N} na base octal é {oct(N)[2:]}\033[m')
elif conversao == 3:
    print('\033[1;33mConvertendo para base hexadecimal...\033[m')
    print(f'\033[1;33mO número {N} na base hexadecimal é {hex(N)[2:]}\033[m')
else:
    print('\033[1;35mNenhuma conversão selecionada, encerrando...\033[m')
