"""
Desafio: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais.
- ISÓSCELES: dois lados iguais, um diferente.
- ESCALENO: todos os lados diferentes.
"""

# Pede o tamanho doslados dos triângulos.  
l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))

# Testa as condições de existência de um triângulo.
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f'Os lados {l1}, {l2} e {l3} PODEM formar um triângulo: ', end='')

# Se formar puder formar um triângulo, testa o tipo de triângulo.
    if l1 == l2 == l3:
        print('EQUILÁTERO, ou seja, todos os lados são iguais.') # Triângulo EQUILÁTERO.
    elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
        print('ISÓCELES, ou seja, dois lados são iguais.') # Triângulo ISÓSCELES.
    elif l1 != l2 != l3:
        print('ESCALENO, ou seja, todos os lados são diferentes.') # Triângulo ESCALENO.
        
# Se não puder formar poder formar um triângulo.
else:
    print(f'Os lados {l1}, {l2} e {l3} NÃO PODEM formar um triângulo.]')
 