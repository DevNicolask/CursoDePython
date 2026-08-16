# Desafio: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Me diga um número. '))
b = int(input('Me diga mais um número. '))
c = int(input('Me diga mais um ultimo número. '))

# Teste pra saber se todos os valores são iguais.
if a == b == c == a:
    print('Não é possível especificar qual o maior pois todos os valores são iguais.')

# Teste pra saber o menor valor.
else:
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c

# Teste pra saber o maior valor.
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
print(f'O menor valor é {menor} e o maior valor é {maior}')
