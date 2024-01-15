# Desafio: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto.
# - à vista no cartão: 5% de desconto.
# - em até 2x no cartão: preço formal.
# - 3x ou mais no cartão: 20% de juros.

# Mostra na tela o menú da loja.
print('\033[1;35m=-=\033[m' * 10)
print('\033[1;36m         LOJAS NICK\033[m')
print('\033[1;35m=-=\033[m' * 10)

# Pede o preço do produto
Pproduto = float(input('\033[1;34mQual é o preço do produto: R$\033[m'))

# Mostra na tela o menú de condições de compra.
print('\033[1;35m[1] - À vista (Dinehiro/Cheque) = 10% de desconto.\033[m')
print('\033[1;35m[2] - À vista (Cartão) = 5% de desconto.\033[m')
print('\033[1;35m[3] - Em até 2x no cartão = preço NORMAL.\033[m')
print('\033[1;35m[4] - 3x ou mais no cartão = 20% de juros.\033[m')
print()
Condicao = int(input('\033[1;35mQual a condição de pagamento? \033[m'))
if Condicao == 1:
    total = Pproduto * 0.9
elif Condicao == 2:
    total = Pproduto * 0.95
elif Condicao == 3:
    total = Pproduto
elif Condicao == 4:
    parcelas = int(input(f'\033[1;31mVocê quer pagar em quantas parcelas? \033[m'))
    total = (Pproduto * 1.2) / parcelas
    print(f'\033[1;31mSua compra de R${Pproduto:.2f} será dividida em {parcelas}x de R${total:.2f} reais Com JUROS.\033[m')
else:
    print(f'\033[1;31mOpção inválida de pagamento. Tente novamente!\033[m')
print(f'\033[1;31mO valor à ser pago pela sua compra de R${Pproduto:.2f} será {total:.2f}R$\033[m')
 