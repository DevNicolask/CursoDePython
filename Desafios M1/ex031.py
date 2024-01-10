# Desafio: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

a = int(input('\033[1;36mMe diga a distância de uma viagem em Km. \033[m')) # Pede uma distância ao usuário.
if a <= 200:
# Pede um número ao usuário.
    print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m '
          f'\033[1;36mirá custar\033[m \033[1;35mR${a * 0.5:.2f} reais.\033[m') # Para viagens de até 200Km
else:
    print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m \033[1;36mirá custar\033[m '
          f'\033[1;35mR${a * 0.45:.2f} reais.\033[m') # Para viagens de mais de 200Km

# Forma que o Prof.Guanabara fez.
# 'if simpificado' = Em uma única linha é colocado o if e o else
"""b = a * 0.50 if a <= 200 else a * 0.45
print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m \033[1;36mirá custar\033[m \033[1;35mR${b:.2f} reais.\33[m')"""
 