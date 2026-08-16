# Desafio: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários 
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Pede ao usuário que digite o seu salário.
a = float(input('Qual é o seu salário? '))

# Dependendo do valor do salário é dado um valor de aumento.
if a > 1250:
    b = a * 1.15 # Mais 15% de aumeneto.
else:
    b = a * 1.1 # Mais 10% de aumeneto.
print('-=-=' * 20)

# Mostra respectivamente na tela, o salário, o salário com aumento, a quantidade do aumento e a porcentagem do aumento do salário.
print(f'Seu salário de {a:.2f} quando receber o aumento será {b:.2f}.\nOu seja terá um aumento de {b - a:.2f}'
f' reais, que é {(b / a * 100) - 100:.0f}% do seu salário anterior.')
print('-=-=' * 20)
