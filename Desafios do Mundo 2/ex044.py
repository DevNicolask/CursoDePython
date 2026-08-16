"""
Desafio: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- em até 2x no cartão: preço formal.
- 3x ou mais no cartão: 20% de juros.
"""

# Mostra na tela o menú da loja.
print('=-=' * 10)
print('         LOJAS NICK')
print('=-=' * 10)

# Pede o preço do produto
Pproduto = float(input('\033[1;34mQual é o preço do produto: R$'))

# Mostra na tela o menú de condições de compra.
print('[1] - À vista (Dinehiro/Cheque) = 10% de desconto.')
print('[2] - À vista (Cartão) = 5% de desconto.')
print('[3] - Em até 2x no cartão = preço NORMAL.')
print('[4] - 3x ou mais no cartão = 20% de juros.')
print()
Condicao = int(input('Qual a condição de pagamento? '))
if Condicao == 1:
    total = Pproduto * 0.9
elif Condicao == 2:
    total = Pproduto * 0.95
elif Condicao == 3:
    total = Pproduto
elif Condicao == 4:
    parcelas = int(input(f'Você quer pagar em quantas parcelas? '))
    total = (Pproduto * 1.2) / parcelas
    print(f'Sua compra de R${Pproduto:.2f} será dividida em {parcelas}x de R${total:.2f} reais Com JUROS.')
else:
    print(f'Opção inválida de pagamento. Tente novamente!')
print(f'O valor à ser pago pela sua compra de R${Pproduto:.2f} será {total:.2f}R$')
 