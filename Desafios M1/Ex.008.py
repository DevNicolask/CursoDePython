# Código normal.
"""a = float(input('Me fale um número em metros para a conversão '))
print(f'{a} metros é igual a:\n'
      f'Em quilômetros: {a/1000}.\n'
      f'Em hectômetros: {a/100}.\n'
      f'Em decametros: {a/10}.\n'
      f'Em decimetros: {a*10}.\n'
      f'Em centímetros: {a*100}.\n'
      f'Em milímetros: {a*1000}')"""

#Código colorido.
a = float(input('\033[2;94mMe fale um número em metros para a conversão \033[m'))
print(f'\033[1;98m{a} metros é igual a:\n'
      f'\033[1;91mEm quilômetros: {a/1000}.\n'
      f'\033[1;93mEm hectômetros: {a/100}.\n'
      f'\033[1;90mEm decametros: {a/10}.\n'
      f'\033[1;95mEm decimetros: {a*10}.\n'
      f'\033[1;96mEm centímetros: {a*100}.\n'
      f'\033[1;97mEm milímetros: {a*1000}\033[m')