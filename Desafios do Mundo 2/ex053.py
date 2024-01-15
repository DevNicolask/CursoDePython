# Desafio: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('\033[1;35mEscreva uma frase: \033[m')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'\033[1;35mO inverso da frase\033[m \033[1;36m{junto}\033[m é \033[1;36m{inverso}.\033[m')
if inverso == junto:
    print(f'\033[1;35mA frase\033[m \033[1;36m{junto}\033[m \033[1;35mÉ UM PALÍNDROMO!\033[m')
else:
    print(f'\033[1;35mA frase\033[m \033[1;36m{junto}\033[m \033[1;31mNÃO É UM PALÍNDROMO!\033[m')
