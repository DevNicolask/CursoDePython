print('=-' * 30)
print(' '*5, 'EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA')
print('=-' * 30)
print()
valor_da_casa = float(input('Digite o valor da casa. R$'))
salario = float(input('Digite seu salário. R$'))
anos = int(input('Em quantos anos você vai pagar? '))
print('=-' * 30)
prestacao = valor_da_casa / (anos*12)
if prestacao > (salario*0.3):
    print(f'O empréstimo não pode ser efetuado, pois a prestação R${prestacao:.2f} da casa é maior que 30% do seu salário que é R${salario}')
else:
    print(f'A sua compra foi efetivada, e você terá que pagar {prestacao:.2f} por {(anos * 12):.0f} mêses')
print('=-' * 30)
