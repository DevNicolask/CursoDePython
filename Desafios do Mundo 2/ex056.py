# Desafio:  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de
# idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homemmaisvelho = ''
qmulheres = 0
mediaidade = 0
idademaior = 0

for cont in range(0, 4):
    print('\033[1;36m=-=\033[m'*7, f'\033[1;36mPESSOA {cont + 1}\033[m', '\033[1;36m=-=\033[m'*7)
    nome = input(f'\033[1;35mDigite o nome da {cont + 1}ª pessoa: \033[m').strip()
    idade = int(input(f'\033[1;35mDigite a idade de {nome}: \033[m'))
    sexo = input(f'\033[1;35mDigite o sexo de {nome} [M/F]: \033[m').strip().upper()

    mediaidade += idade

    if sexo == 'M' and (homemmaisvelho == '' or idade > idademaior):
        idademaior = idade
        homemmaisvelho = nome

    if sexo == 'F' and idade < 20:
        qmulheres += 1

Midade = mediaidade / 4

print()
print(f'\033[1;36mA média de idade do grupo é {Midade:.2f} anos.\033[m')
if homemmaisvelho == '':
    print(f'\033[1;36mNão tem homens no grupo.\033[m')
else:
    print(f'\033[1;36mO homem mais velho do grupo é o {homemmaisvelho}.\033[m')
if qmulheres == 1:
    print(f'\033[1;36mNesse grupo, {qmulheres} mulher tem menos de 20 anos de idade.')
else:
    print(f'\033[1;36mNesse grupo, {qmulheres} mulheres têm menos de 20 anos de idade.')
