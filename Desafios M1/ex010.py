# Desafio: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Versão Não colorida.
a = float(input('Quanto de dinheiro você tem? R$ '))
print(f'Você pode receber {a/4.93:.2f} dólares, ou você pode receber {a/5.32:.2f} euros.')

# Versão Colorida.
"""
a = float(input('\033[1;34mQuanto de dinheiro você tem? R$ \033[m')) print(f'\033[1;35mVocê pode receber\033[m 
\033[1;32m{a/4.93:.2f} dólares\033[m \033[1;35m, ou você pode receber\033[m \033[1;32m{a/5.32:.2f} euros.\033[m')"""
