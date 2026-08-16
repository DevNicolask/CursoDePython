# Desafio: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Obs.: depois tente fazer a conversão para todas as subunidades principais do metro.

a = float(input('Me fale um número em metros para a conversão '))
print(f'{a} metros é igual a:\n'
      f'Em quilômetros: {a/1000}.\n'
      f'Em hectômetros: {a/100}.\n'
      f'Em decametros: {a/10}.\n'
      f'Em decimetros: {a*10}.\n'
      f'Em centímetros: {a*100}.\n'
      f'Em milímetros: {a*1000}')
