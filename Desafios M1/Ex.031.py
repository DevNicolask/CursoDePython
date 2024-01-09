# Minha Versão. (Colorida)
a = int(input('\033[1;36mMe diga a distância de uma viagem em Km. \033[m'))
if a <= 200:
    print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m '
          f'\033[1;36mirá custar\033[m \033[1;35mR${a * 0.5:.2f} reais.\033[m')
else:
    print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m \033[1;36mirá custar\033[m '
          f'\033[1;35mR${a * 0.45:.2f} reais.\033[m')

# Forma que o Prof.Guanabara fez.
# 'if simpificado' = Em uma única linha é colocado o if e o else
"""
b = a * 0.50 if a <= 200 else a * 0.45
print(f'\033[1;36mSua viagem de\033[m \033[1;35m{a}Km\033[m \033[1;36mirá custar\033[m \033[1;35mR${b:.2f} reais.\33[m')"""
