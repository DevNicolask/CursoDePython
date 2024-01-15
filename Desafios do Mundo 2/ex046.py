# Desafio: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com pausa de 1 segundo entre eles.

from time import sleep  # Importei da lib 'time', a função sleep pra  dar um delay entre a contagem.

for contador in range(10, -1, -1):
    print(f'\033[1;35mContagem regressiva até os fogos de artifício estourarem:\033[m \033[1;36m{contador}!\033[m')
    sleep(1)
print(' ' * 15, '\033[1;31mBUM! BOOM!! POW!!! ESTOUROU!!! 🧨🎆🎆🎆\033[m')
 