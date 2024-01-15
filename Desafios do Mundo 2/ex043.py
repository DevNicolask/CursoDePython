# Desafio: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso.
# - Entre 18,5 e 25: Peso Ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade Mórbida.

# Menú do 'Teste de IMC'.
print('\033[1;35m=-=\033[m' * 10)
print('\033[1;35m         TESTE DE IMC\033[m')
print('\033[1;35m=-=\033[m' * 10)

# Pede o peso e a altura da pessoa no S.I.
peso = float(input('\033[1;36mDigite seu peso:(Kg) \033[m'))
altura = float(input('\033[1;36mDigite sua altura:(m) \033[m'))

# Faz o calculo do IMC.
IMC = peso / (altura ** 2)

# Mostra na tela o IMC do indivíduo.
print(f'\033[1;35mSEU IMC:\033[m \033[1;38m{IMC:.1f}.\033[m')

# Condições de pesos possíveis.
if IMC < 18.5:
    print('\033[1;35mSTATUS:\033[m \033[1;38mVocê está ABAIXO DO PESO normal.\033[m') # Abaixo do Peso.
elif 18.5 <= IMC < 25:
    print('\033[1;35mSTATUS:\033[m \033[1;36mVocê está no PESO IDEAL. Parabéns!!!\033[m') # Peso Ideal.
elif 25 <= IMC < 30:
    print('\033[1;35mSTATUS:\033[m \033[1;33mVocê está em SOBREPESO.\033[m') # Sobrepeso.
elif 30 <= IMC < 40:
    print('\033[1;35mSTATUS:\033[m \033[1;31mVocê está em OBESIDADE.\033[m') # Obesidade.
elif 40 <= IMC:
    print('\033[1;35mSTATUS:\033[m \033[1;30mVocê está em OBESIDADE MÓRBIDA, cuidado!\033[m')  # Obesidade Mórbida.
 