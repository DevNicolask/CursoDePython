# Pede ao usuário que diggite o seu salário.
a = float(input('\033[1;33mQual é o seu salário? \033[m'))
# Dependendo do valor do salário é dado um valor de aumento.
if a < 1250:
    b = a * 1.15
else:
    b = a * 1.1
print('\033[33m-=-=\033[m' * 20)
# Mostra respectivamente na tela, o salário, o salário com aumento, a quantidade do aumento e a porcentagem do aumento
# do salário.
print(f'\033[1;32mSeu salário de {a:.2f} quando receber o aumento será {b:.2f}.\nOu seja terá um aumento de {b - a:.2f}'
      f' reais, que é {(b / a * 100) - 100:.0f}% do seu salário anterior.\033[m')
print('\033[33m-=-=\033[m' * 20)
