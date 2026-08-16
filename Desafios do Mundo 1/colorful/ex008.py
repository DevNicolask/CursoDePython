# Desafio: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Obs.: depois tente fazer a conversão para todas as subunidades principais do metro.

a = float(input('\033[2;94mMe fale um número em metros para a conversão \033[m'))
print(f'\033[1;98m{a} metros é igual a:\n'
      f'\033[1;91mEm quilômetros: {a/1000}.\n'
      f'\033[1;93mEm hectômetros: {a/100}.\n'
      f'\033[1;90mEm decametros: {a/10}.\n'
      f'\033[1;95mEm decimetros: {a*10}.\n'
      f'\033[1;96mEm centímetros: {a*100}.\n'
      f'\033[1;97mEm milímetros: {a*1000}\033[m')
