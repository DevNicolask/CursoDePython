# Desafio: Crie um programa que faça o computador jogar Jokenpô com você.

# Fazendo o Pedra, Papel e Tesoura!
from random import choice
from time import sleep

print('\033[1;35m=-=\033[m' * 10)
print('\033[1;36m           JO KEN PÔ\033[m')
print('\033[1;35m=-=\033[m' * 10)
# O computador escolhe um ítem da lista e pede ao usuário que faça o mesmo.
print(f'''\033[1;34mEscolha uma dessas opções: 
    [0] - PEDRA.
    [1] - PAPEL.
    [2] - TESOURA.\033[m''')
lista = ['PEDRA', 'PAPEL', 'TESOURA']

# Chama a função choice da lib. Random, que faz a escolha de um dos ítens da lista.
Jcomp = choice(lista)

# Pede a jogada do jogador, que poe ser 0, 1 ou 2. Caso contrário mostra uma mensagem de ERRO.
posição = int(input(f'\033[1;34mO que você quer jogar? \033[m'))
if posição == 0 or posição == 1 or posição == 2:
    Jogador = lista[posição]
    print('\033[1;35m=-=\033[m' * 10)

# Mostra o Jo Ken Po. Com intervalo de tempo entre o nome usando a função sleep da lib. time
    print('\033[1;36mJo\033[m')
    sleep(1)
    print('\033[1;36mKEN\033[m')
    sleep(1)
    print('\033[1;36mPO!!!\033[m')
    sleep(1)
    print('\033[1;35m=-=\033[m' * 10)

# Início Condições resposta do jogo.
# Deu empate.
    if Jcomp == Jogador:
        print(f'\033[1;36mO jogador EMPATOU com o COMPUTADOR. \n'
            f'Ambos jogaram \033[m \033[1;35m{Jcomp}\033[m.')

# O computador ganhou. Condições em que isso ocorre.
    elif (Jcomp == 'PEDRA' and Jogador == 'TESOURA' or Jcomp == 'TESOURA' and Jogador ==
        'PAPEL' or Jcomp == 'PAPEL' and Jogador == 'PEDRA'):
        print(f'\033[1;36mO computador GANHOU com\033[m \033[1;31m{Jcomp}\033[m \n'
            f'\033[1;36mContra o Jogador com\033[m \033[1;31m{Jogador}\033[m')
        print(f'\033[1;36mMais sorte da próxima vez Jogador\033[m')

# O jogador ganhou. Condições em que isso ocorre.
    elif (Jogador == 'PEDRA' and Jcomp == 'TESOURA' or Jogador == 'TESOURA' and Jcomp ==
        'PAPEL' or Jogador == 'PAPEL' and Jcomp == 'PEDRA'):
        print(f'\033[1;36mO jogador GANHOU com\033[m \033[1;35m{Jogador}\033[m \n'
            f'\033[1;36mContra COMPUTADOR com \033[m \033[1;35m{Jcomp}\033[m')
        print(f'\033[1;36mParabéns Jogador! Você GANHOU!!!\033[m')

# Jogada inválida. Mostra uma mensagem de ERRO.
else:
    print(f'\033[1;36mERRO! Aparentemente você não jogou nenhuma opção válida, '
          'tente novamente.\033[m.')
print('\033[1;35m=-=\033[m' * 10)

# Fim das condições de resposta do jogo.
 