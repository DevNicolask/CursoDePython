N1 = float(input('\033[1;36mDigite a primeira nota do aluno: \033[m'))
N2 = float(input('\033[1;36mDigite a segunda nota do aluno: \033[m'))
media = (N1 + N2) / 2
if media < 5:
    print(f'\033[1;31mA média do aluno foi {media} e ele está REPROVADO.\033[m')
elif media >= 7:
    print(f'\033[1;35mA média do aluno foi {media} e ele está APROVADO.\033[m')
else:
    print(f'\033[1;33mA média do aluno foi {media} e ele está de RECUPERAÇÃO.\033[m')
