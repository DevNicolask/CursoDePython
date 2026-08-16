"""
Desafio: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.

Obs: Importei duas bibliotecas externas; random e Time.
Random: Vai fazer a função de escolher de forma aleatória um número de 0 a 5.
"""

from random import randint

# Time: Vai fazer a função de dar um determinado "tempo" de delay no código.
from time import sleep

# Tela de começo do jogo.
print('-=-'*18)
print('Vou pensar em um número entre 0 a 5, tente adivinhar!')
print(' '*23, '...')
sleep(2)

# Chama a função para escolher um número e armazena-lo em 'a'.
a = randint(0, 5)
print(' '*21, 'Pensei!')
print('-=-'*18)
sleep(2)

# Pede ao usuário um palpite de que número seria 'a'.
b = int(input('Em que número eu pensei? '))

# Tela final.
if b == a:
    sleep(2)
    print('Você acertou!!! Parabéns!') # Se o jogador ganhar.
else:
    sleep(2)
    print(f'Que pena, você errou, eu pensei em {a} e não em {b} mais sorte da próxima vez!') # Se o jogador perder.
