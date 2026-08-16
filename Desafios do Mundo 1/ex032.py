# Desafio: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Importa da lib. datetime a função date().year que verifica qual o ano atual.
from datetime import date

ano = int(input('Me diga um ano para analizar se é um ano bissexto.'
              '(Digite 0 para analizar o ano atual) ')) # Pede ao usuário um ano.

# Se a variável ano == 0, importa pela biblioteca o ano atual.
if ano == 0:
    ano = date.today().year

# Testa se as condições para ser um ano bissexto são cumpridas.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO!') # Ano é bissexto.
else:
    print(f'O ano {ano} NÃO É BISSEXTO!') # Ano não é bissexto.
