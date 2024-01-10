# Desafio: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do 
# comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Mostra o Menú do Empréstimo bancário.
print('=-' * 30)
print(' '*5, 'EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA')
print('=-' * 30)
print()
valor_da_casa = float(input('Digite o valor da casa. R$')) # Pede ao usuário que digite o valor da casa.
salario = float(input('Digite seu salário. R$')) # Pede ao usuário que digite o seu salário.
anos = int(input('Em quantos anos você vai pagar? ')) # Pede ao usuário que digite a quantidade de anos que o comprador quer pagar.
print('=-' * 30)
prestacao = valor_da_casa / (anos*12) # Calcula o valor da prestação
# Analisa as situações possíveis.
# Prestação ser aprovada.
if prestacao > (salario*0.3):
    print(f'O empréstimo não pode ser efetuado, pois a prestação R${prestacao:.2f} da casa é maior que 30% do seu salário que é R${salario}')
# Prestação não ser aprovada.
else:
    print(f'A sua compra foi efetivada, e você terá que pagar {prestacao:.2f} por {(anos * 12):.0f} mêses')
print('=-' * 30)
