"""
Desafio: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

a = str(input('Digite uma frase. ')).lower().strip()
print('Analisando frase...')
print(f'A letra "A" aparece {a.count('a')} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição {a.find('a'[0]) + 1}.')
print(f'A letra "A" aparece pela ultima vez na posição {a.rfind('a'[0]) + 1}.')
