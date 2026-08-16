"""
Desafio: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""

# Pede os valores para o usuário. 
A = int(input('Digite um número '))
B = int(input('Digite outro número '))

# Análise de situações possíveis.
if A == B:
    print('Nenhum dos dois números é maior, pois os dois são iguais.') # Dois números iguais.
elif A > B:
    print(f'O número {A} é maior que o número {B}.') # O primeiro é maior.
else:
    print(f'O número {B} é maior que o número {A}.') # O segundo é maior. 
