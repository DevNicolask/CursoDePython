# Desafio: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

a = int(input('Me diga a distância de uma viagem em Km.')) # Pede uma distância ao usuário.
if a <= 200:
# Pede um número ao usuário.
    print(f'Sua viagem de {a}Km '
          f'irá custar R${a * 0.5:.2f} reais.') # Para viagens de até 200Km
else:
    print(f'Sua viagem de {a}Km irá custar '
          f'R${a * 0.45:.2f} reais.') # Para viagens de mais de 200Km
