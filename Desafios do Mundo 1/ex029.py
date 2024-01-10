# Desafio: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem 
# dizendo que ele foi multado. A multa deverá custar R$7,00 por cada Km acima do limite.

# Minha Versão. (Colorida)
a = float(input('\033[1;35mQual a velocidade do carro ?(Km/h) \033[m'))

# Análise de possíbilidades possiveis.
if a > 80:
    print(f'\033[1;31mMULTADO!!!\033[m \033[1;35mVocê excedeu o limite de velocidade permitido que é de 80Km/h.\n'
          f'Você deverá pagar uma multa de\033[m \033[1;31mR${(a - 80) * 7:.2f} reais.\033[m') # Ultrapassou 80Km/h.
else:
   print('\033[1;35mVocê está em uma velocidade permitida e não precisará pagar uma multa. '
         'Tenha uma boa viagem!!!\033[m') # Não Ultrapassou 80Km/h.
   
# Tela final padrão.
print('\033[1;36mTenha um bom dia e dirija com segurança.\033[m')
 