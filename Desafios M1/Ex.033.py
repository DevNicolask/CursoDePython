# Desafio de análise de valores, qual o menor e o maior valor.
a = int(input('\033[1;35mMe diga um número. \033[m'))
b = int(input('\033[1;35mMe diga mais um número. \033[m'))
c = int(input('\033[1;35mMe diga mais um ultimo número. \033[m'))
# Teste pra saber se algum valor é igual
if a == b == c:
    print('\033[1;35mNão é possível especificar qual o maior pois todos os valores são iguais.\033[m')
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
    print(f'\033[1;35mO menor valor é\033[m \033[1;36m{menor}\033[m \033[1;35me o maior valor é\033[m \033[1;36m{maior}\033[m')
