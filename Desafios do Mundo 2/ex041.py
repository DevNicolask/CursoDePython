"""
Desafio: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JÚNIOR.
- Até 25 anos: SÊNIOR.
- Acima de 25 anos: MASTER.
"""

from datetime import date

# Menú fictício.
print('=-=' * 15)
print('   CONFEDERAÇÃO NACIONAL DE NATAÇÃO (CNN)')
print('=-=' * 15)
ano = float(input('Digite o ano de nascimento do atleta: '))

#  Importa da Lib. datetime a função today().year para armazenar em 'ano_atual' o ano atual.
ano_atual = date.today().year
idade = ano_atual - ano # Calcula a idade do atleta.
print(f'A idade do atleta é {idade:.0f} anos.]') # Mostra na tela a idade do atleta.

# Verifica todas as opções possíveis
if idade <= 9:
    print('O atleta está no nível MIRIM.') # - Até 9 anos: MIRIM.
elif idade <= 14:
    print('O atleta está no nível INFANTIL.') # - Até 14 anos: INFANTIL.
elif idade <= 19:
    print('O atleta está no nível JÚNIOR.') # - Até 19 anos: JÚNIOR.
elif idade <= 25:
    print('O atleta está no nível SÊNIOR.') # - Até 25 anos: SÊNIOR.
else:
    print('O atleta está no nível MASTER.') # - Acima de 25 anos: MASTER.
 