# Desafio: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem 
# dizendo que ele foi multado. A multa deverá custar R$7,00 por cada Km acima do limite.

# Minha Versão. (Colorida)
a = float(input('Qual a velocidade do carro ?(Km/h). '))

# Análise de possíbilidades possiveis.
if a > 80:
    print(f'MULTADO!!! Você excedeu o limite de velocidade permitido que é de 80Km/h.\n'
          f'Você deverá pagar uma multa de R${(a - 80) * 7:.2f} reais.') # Ultrapassou 80Km/h.
else:
   print('Você está em uma velocidade permitida e não precisará pagar uma multa. '
         'Tenha uma boa viagem!!!') # Não Ultrapassou 80Km/h.
   
# Tela final padrão.
print('Tenha um bom dia e dirija com segurança.')
