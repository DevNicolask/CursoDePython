# Minha versão. (Colorida)
# Importei duas bibliotecas externas; random e Time.
# Random: Vai fazer a função de escolher de forma aleatória um número de 0 a 5.
from random import randint
# Time: Vai fazer a função de dar um determinado "tempo" de delay no código.
from time import sleep

# Tela de começo do jogo.
print('\033[1;35m-=-'*18)
print('\033[1;35mVou pensar em um número entre 0 a 5, tente adivinhar!')
print(' '*23, '\033[1;35m...')
sleep(2)
# Chama a função para escolher um número e armazena-lo em 'a'.
a = randint(0, 5)
print(' '*21, '\033[1;35mPensei!')
print('\033[1;35m-=-'*18)
sleep(2)
# Pede ao usuário um palpite de que número seria 'a'.
b = int(input('\033[1;35mEm que número eu pensei? '))
# Tela final.
# Se o jogador ganhar.
if b == a:
    sleep(2)
    print('\033[1;35mVocê acertou!!!\033[m \033[1;36mParabéns! \033[m')
# Se o jogador perder.
else:
    sleep(2)
    print(f'\033[1;35mQue pena, você errou, eu pensei em\033[m \033[1;33m{a}\033[m \033[1;35me não em\033[m '
          f'\033[1;31m{b}\033[m \033[1;35mmais sorte da próxima vez! \033[m')
