# Desafio: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais.
# - ISÓSCELES: dois lados iguais, um diferente.
# - ESCALENO: todos os lados diferentes.

# Pede o tamanho doslados dos triângulos.  
l1 = float(input('\033[1;36mDigite o tamanho do primeiro lado: \033[m'))
l2 = float(input('\033[1;36mDigite o tamanho do segundo lado: \033[m'))
l3 = float(input('\033[1;36mDigite o tamanho do terceiro lado: \033[m'))

# Testa as condições de existência de um triângulo.
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f'\033[1;36mOs lados {l1}, {l2} e {l3} PODEM formar um triângulo: \033[m', end='')

# Se formar puder formar um triângulo, testa o tipo de triângulo.
    if l1 == l2 == l3:
        print('\033[1;35mEQUILÁTERO, ou seja, todos os lados são iguais.\033[m') # Triângulo EQUILÁTERO.
    elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
        print('\033[1;35mISÓCELES, ou seja, dois lados são iguais.\033[m') # Triângulo ISÓSCELES.
    elif l1 != l2 != l3:
        print('\033[1;35mESCALENO, ou seja, todos os lados são diferentes.\033[m') # Triângulo ESCALENO.
        
# Se não puder formar poder formar um triângulo.
else:
    print(f'\033[1;36mOs lados {l1}, {l2} e {l3} NÃO PODEM formar um triângulo.\033[m]')
