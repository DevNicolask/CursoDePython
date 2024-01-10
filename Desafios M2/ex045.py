# Desafio: Crie um programa que faça o computador jogar Jokenpô com você.

# FAzendo o Pedra, Papel e Tesoura!
from random import choice

# Pergunta ao usuário o nome dele pra melhorar a interação no jogo.
nome = str(input('\033[1;35mDigite seu nome. \033[m'))

# Pergunta se o usuário quer jogar.
resp = str(input(f'\033[1;35mVamos jogar Jokenpô {nome}?[S/n] \033[m'))
if resp.upper() == 'S' or resp.upper() == 'SIM':

    # Caso o usuário queira jogar, o computador escolhe um ítem da lista e pede ao usuário que faça o mesmo.
    print('\033[1;34mVou escolher entre pedra, papel ou tesoura.'
          f'Escolha uma dessas opções pra você também {nome}.\033[m')
    lista = ['PEDRA', 'PAPEL', 'TESOURA']

    # Chama a função choice da lib. Random, que faz a escolha de um dos ítens da lista.
    Jcomp = choice(lista)
    Jnome = str(input(f'\033[1;35mO que você escolheu? \033[m'))

    # Início Condições resposta do jogo.
    # Deu empate.
    if Jcomp.upper() == Jnome.upper():
        print(f'\033[1;36mO jogador {nome} EMPATOU com o COMPUTADOR com \033[m \033[1;35m{Jcomp.upper()}\033[m.')

    # O computador ganhou. Condições em que isso ocorre.
    elif (Jcomp.upper() == 'PEDRA' and Jnome.upper() == 'TESOURA' or Jcomp.upper() == 'TESOURA' and Jnome.upper() ==
          'PAPEL' or Jcomp.upper() == 'PAPEL' and Jnome.upper() == 'PEDRA'):
        print(f'\033[1;35mO computador GANHOU com\033[m \033[1;31m{Jcomp.upper()}\033[m \033[1;35mcontra {nome} '
              f'com\033[m \033[1;31m{Jnome.upper()}\033[m')
        print(f'\033[1;35mMais sorte da próxima vez {nome}\033[m')

    # O jogador ganhou.
    else:
        print(f'\033[1;36mO jogador {nome} GANHOU com\033[m \033[1;35m{Jnome.upper()}\033[m '
              f'\033[1;36mcontra COMPUTADOR com \033[m \033[1;35m{Jcomp.upper()}\033[m')
        print(f'\033[1;36mMuito bem {nome}! Você é muito bom nesse jogo.\033[m')

    # Fim das condições de resposta do jogo.
else:

    # Se o usuário não quiser jogar Jokenpõ ele finaliza o programa
    print('\033[1;33mVamos jogar outra hora então...\033[m')
