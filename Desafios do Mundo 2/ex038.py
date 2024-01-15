# Desafio: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior.
# - O segundo valor é maior.
# - Não existe valor maior, os dois são iguais.

# Pede os valores para o usuário. 
A = int(input('\033[1;36mDigite um número \033[m'))
B = int(input('\033[1;36mDigite outro número \033[m'))

# Análise de situações possíveis.
if A == B:
    print('\033[1;35mNenhum dos dois números é maior, pois os dois são iguais.\033[m') # Dois números iguais.
elif A > B:
    print(f'\033[1;35mO número {A} é maior que o número {B}.\033[m') # O primeiro é maior.
else:
    print(f'\033[1;35mO número {B} é maior que o número {A}.\033[m') # O segundo é maior. 
