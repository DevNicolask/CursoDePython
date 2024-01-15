# Desafio: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM.
# - Até 14 anos: INFANTIL.
# - Até 19 anos: JÚNIOR.
# - Até 25 anos: SÊNIOR.
# - Acima de 25 anos: MASTER.

from datetime import date

# Menú fictício.
print('\033[1;36m=-=\033[m' * 15)
print('\033[1;36m   CONFEDERAÇÃO NACIONAL DE NATAÇÃO (CNN)\033[m')
print('\033[1;36m=-=\033[m' * 15)
ano = float(input('\033[1;37mDigite o ano de nascimento do atleta: \033[m'))

#  Importa da Lib. datetime a função today().year para armazenar em 'ano_atual' o ano atual.
ano_atual = date.today().year
idade = ano_atual - ano # Calcula a idade do atleta.
print(f'\033[1;35mA idade do atleta é {idade:.0f} anos.\033[m]') # Mostra na tela a idade do atleta.

# Verifica todas as opções possíveis
if idade <= 9:
    print('\033[1;31mO atleta está no nível MIRIM.\033[m') # - Até 9 anos: MIRIM.
elif idade <= 14:
    print('\033[1;32mO atleta está no nível INFANTIL.\033[m') # - Até 14 anos: INFANTIL.
elif idade <= 19:
    print('\033[1;33mO atleta está no nível JÚNIOR.\033[m') # - Até 19 anos: JÚNIOR.
elif idade <= 25:
    print('\033[1;34mO atleta está no nível SÊNIOR.\033[m') # - Até 25 anos: SÊNIOR.
else:
    print('\033[1;35mO atleta está no nível MASTER.\033[m') # - Acima de 25 anos: MASTER.
 