# Minha Versão. (Colorida)
a = float(input('\033[1;35mQual a velocidade do carro ?(Km/h) \033[m'))
if a > 80:
    print(f'\033[1;31mMULTADO!!!\033[m \033[1;35mVocê excedeu o limite de velocidade permitido que é de 80Km/h.\n'
          f'Você deverá pagar uma multa de\033[m \033[1;31mR${(a - 80) * 7:.2f} reais.\033[m')
else:
   print('\033[1;35mVocê está em uma velocidade permitida e não precisará pagar uma multa. '
         'Tenha uma boa viagem!!!\033[m')
print('\033[1;36mTenha um bom dia e dirija com segurança.\033[m')
