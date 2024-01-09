l1 = float(input('\033[1;36mDigite o tamanho do primeiro lado: \033[m'))
l2 = float(input('\033[1;36mDigite o tamanho do segundo lado: \033[m'))
l3 = float(input('\033[1;36mDigite o tamanho do terceiro lado: \033[m'))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('\033[1;38mO triângulo existe.')
    if l1 == l2 == l3:
        print('\033[1;35mO triângulo é equilátero, ou seja, todos os lados são iguais.\033[m')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
        print('\033[1;35mO triângulo é isóceles, ou seja, dois lados são iguais.\033[m')
    elif l1 != l2 != l3:
        print('\033[1;35mO triângulo é escaleno, ou seja, todos os lados são diferentes.\033[m')
else:
    print('\033[1;31mEsse triângulo não existe.\033[m')
