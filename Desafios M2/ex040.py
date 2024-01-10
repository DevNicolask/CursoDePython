# Desafio: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO.
# - Média entre 5.0 e 6.9: RECUPERAÇÃO.
# - Média 7.0 ou superior: APROVADO.

# Solicita as notas do aluno ao usuário.
N1 = float(input('\033[1;36mDigite a primeira nota do aluno: \033[m'))
N2 = float(input('\033[1;36mDigite a segunda nota do aluno: \033[m'))
# Calcula a média das duas notas.
media = (N1 + N2) / 2
# Análise de situações possíveis.
# Verifica se a média é menor que 5, Se for, o aluno está REPROVADO.
if media < 5:
    print(f'\033[1;31mA média do aluno foi {media:.1f} e ele está REPROVADO.\033[m')
# Verifica se a média é maior ou igual a 7, Se for, o aluno está APROVADO.
elif media >= 7:
    print(f'\033[1;35mA média do aluno foi {media:.1f} e ele está APROVADO.\033[m')
# Se a média não for menor que 5 nem maior ou igual a 7,se for, o aluno está DE RECUPERAÇÃO.
else:
    print(f'\033[1;33mA média do aluno foi {media:.1f} e ele está de RECUPERAÇÃO.\033[m')
