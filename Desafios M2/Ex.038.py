A = int(input('\033[1;36mDigite um número \033[m'))
B = int(input('\033[1;36mDigite outro número \033[m'))
if A == B:
    print('\033[1;35mNenhum dos dois números é maior, pois os dois são iguais.\033[m')
elif A > B:
    print(f'\033[1;35mO número {A} é maior que o número {B}.\033[m')
else:
    print(f'\033[1;35mO número {B} é maior que o número {A}.\033[m')
