# Desafio: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

a = int(input('\033[1;35mMe diga um número qualquer. \033[m')) # Pede um número ao usuário.

# Testa as possibilidades de acordo com o resto do número por 2.
if a % 2 == 0:
    print('\033[1;35mSeu número é\033[m \033[1;36mPAR.\033[m') # Se o número for par
else:
    print('\033[1;35mSeu número é\033[m \033[1;36mIMPAR.\033[m') # Se o número for impar
 