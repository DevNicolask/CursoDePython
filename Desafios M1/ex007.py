# Desafio: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Versão Não colorida.
# Média aritmética entre duas notas de um aluno.
nota1 = int(input('Nota 1 do aluno '))
nota2 = int(input('Nota 2 do aluno '))
print(f'A média aritmética das notas desse aluno é {(nota1+nota2)/2}')

# Versão Colorida.

nota1 = int(input('\033[1;34mNota 1 do aluno \033[m'))
nota2 = int(input('\033[1;34mNota 2 do aluno \033[m'))
print(f'\033[1;35mA média aritmética das notas desse aluno é\033[m \033[1;36m{(nota1+nota2)/2}\033[m')
 