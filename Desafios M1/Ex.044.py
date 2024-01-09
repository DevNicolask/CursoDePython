Pproduto = float(input('\033[1;34mQual é o preço do produto. \033[m'))
print('\033[1;35m1 - À vista (Dinehiro/Cheque) = 10% de desconto.\033[m')
print('\033[1;35m2 - À vista (Cartão) = 5% de desconto.\033[m')
print('\033[1;35m3 - Em até 2x no cartão = preço NORMAL.\033[m')
print('\033[1;35m4 - 3x ou mais no cartão = 20% de juros.\033[m')
print()
Condicao = int(input('\033[1;35mQual a condição de pagamento? \033[m'))
if Condicao == 1:
    total = Pproduto * 0.9
    print(f'\033[1;32mO valor à ser pago pelo produto será {total:.2f}R$')
elif Condicao == 2:
    total = Pproduto * 0.95
    print(f'\033[1;32mO valor à ser pago pelo produto será {total:.2f}R$')
elif Condicao == 3:
    total = Pproduto
    print(f'\033[1;38mO valor à ser pago pelo produto será {total:.2f}R$')
elif Condicao == 4:
    total = Pproduto * 1.2
    print(f'\033[1;31mO valor à ser pago pelo produto será {total:.2f}R$')
