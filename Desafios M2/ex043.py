# Desafio: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso.
# - Entre 18,5 e 25: Peso Ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade Mórbida.

print('\033[1;35m=-=\033[m' * 10)
print('\033[1;35m         TESTE DE IMC\033[m')
print('\033[1;35m=-=\033[m' * 10)
peso = float(input('\033[1;36mDigite seu peso:(Quilos) \033[m'))
altura = float(input('\033[1;36mDigite sua altura:(Metros) \033[m'))
IMC = peso / (altura ** 2)
print(f'\033[1;35mSEU IMC: {IMC:.2f}.\033[m')
if IMC < 18.5:
    print('\033[1;35mSTATUS:\033[m \033[1;38mABAIXO DO PESO.\033[m')
elif 18.5 <= IMC < 25:
    print('\033[1;35mSTATUS:\033[m \033[1;36mPESO IDEAL.\033[m')
elif 25 <= IMC < 30:
    print('\033[1;35mSTATUS:\033[m \033[1;33mSOBREPESO.\033[m')
elif 30 <= IMC < 40:
    print('\033[1;35mSTATUS:\033[m \033[1;31mOBESIDADE.\033[m')
elif 40 <= IMC:
    print('\033[1;35mSTATUS:\033[m \033[1;30mOBESIDADE MÓRBIDA.\033[m')