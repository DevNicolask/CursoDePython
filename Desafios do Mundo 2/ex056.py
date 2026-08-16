"""
Desafio: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de
idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

homemmaisvelho = ''
qmulheres = 0
mediaidade = 0
idademaior = 0

for cont in range(0, 4):
    print('=-=' * 7, f'PESSOA {cont + 1}', '=-=' * 7)
    nome = input(f'Digite o nome da {cont + 1}ª pessoa: ').strip()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Digite o sexo de {nome} [M/F]: ').strip().upper()

    mediaidade += idade

    if sexo == 'M' and (homemmaisvelho == '' or idade > idademaior):
        idademaior = idade
        homemmaisvelho = nome

    if sexo == 'F' and idade < 20:
        qmulheres += 1

Midade = mediaidade / 4

print()
print(f'A média de idade do grupo é {Midade:.2f} anos.')
if homemmaisvelho == '':
    print(f'Não tem homens no grupo.')
else:
    print(f'O homem mais velho do grupo é o {homemmaisvelho}.')
if qmulheres == 1:
    print(f'Nesse grupo, {qmulheres} mulher tem menos de 20 anos de idade.')
else:
    print(f'Nesse grupo, {qmulheres} mulheres têm menos de 20 anos de idade.')
