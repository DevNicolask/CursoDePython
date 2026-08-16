"""
Desafio: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso.
- Entre 18,5 e 25: Peso Ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade Mórbida.
"""

# Menú do 'Teste de IMC'.
print('=-=' * 10)
print('         TESTE DE IMC')
print('=-=' * 10)

# Pede o peso e a altura da pessoa no S.I.
peso = float(input('Digite seu peso:(Kg) '))
altura = float(input('Digite sua altura:(m) '))

# Faz o calculo do IMC.
IMC = peso / (altura ** 2)

# Mostra na tela o IMC do indivíduo.
print(f'SEU IMC: {IMC:.1f}.')

# Condições de pesos possíveis.
if IMC < 18.5:
    print('STATUS: Você está ABAIXO DO PESO normal.') # Abaixo do Peso.
elif 18.5 <= IMC < 25:
    print('STATUS: Você está no PESO IDEAL. Parabéns!!!') # Peso Ideal.
elif 25 <= IMC < 30:
    print('STATUS: Você está em SOBREPESO.') # Sobrepeso.
elif 30 <= IMC < 40:
    print('STATUS: Você está em OBESIDADE.') # Obesidade.
elif 40 <= IMC:
    print('STATUS: Você está em OBESIDADE MÓRBIDA, cuidado!')  # Obesidade Mórbida.
 