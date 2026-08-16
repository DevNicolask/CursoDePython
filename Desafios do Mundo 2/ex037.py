"""
Desafio: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será 
a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
N = int(input('Digite um número ')) # Pede o número que vai ser convertido ao usuário.
print('=-='*10)
print('     CONVERSOR DE BASES')
print('=-='*10)
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - Hexadecimal')
print('=-='*10)

# Pede ao usuário qual a base de conversão.
conversao = int(input('Para qual base você quer fazer a conversão? '))

"""
Análise de situações possíveis.
Conversão para binário.
"""
if conversao == 1:
    print('Convertendo para base binária...')
    print(f'O número {N} na base binária é {bin(N)[2:]}') # Utilizei a função: bin()

# Conversão para octal.
elif conversao == 2:
    print('Convertendo para base octal...')
    print(f'O número {N} na base octal é {oct(N)[2:]}') # Utilizei a função: oct()

# Conversão para hexadecimal.
elif conversao == 3:
    print('Convertendo para base hexadecimal...')
    print(f'O número {N} na base hexadecimal é {hex(N)[2:]}') # Utilizei a função: hex()

# Usuário não digitou nenhum dos outros comandos. Encerra o programa.
else:
    print('Nenhuma conversão selecionada, encerrando...')
