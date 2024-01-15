# Desafio: Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agor utilizando um
# laço 'for'.

contador = 0
numero = int(input('\033[1;35mEscreva o número que você quer a tabuada: \033[m'))
for contador in range(0, 11):
    print(f'\033[1;36m{numero} * {contador:2} = {numero * contador}\033[m')
