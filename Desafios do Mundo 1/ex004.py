# Desafio: Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as 
# informações possíveis sobre ele.

a = input('Digite algo ')
print(f'{a} é de qual tipo primtivo? ', type(a))
print(f'{a} é numérico? ', a.isnumeric())
print(f'{a} é alfabético? ', a.isalpha())
print(f'{a} é alfa numérico? ', a.isalnum())
print(f'{a} é um espaço? ', a.isspace())
print(f'{a} tem apenas letras maiúsculas? ', a.isupper())
print(f'{a} team apenas letras minúsculas? ', a.islower())
print(f'{a} tem a inicial maiúscula?(capitalizated) ', a.istitle())
