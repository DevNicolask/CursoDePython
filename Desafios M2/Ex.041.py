print('\033[1;36m=-=\033[m' * 15)
print('\033[1;36m   CONFEDERAÇÃO NACIONAL DE NATAÇÃO (CNN)\033[m')
print('\033[1;36m=-=\033[m' * 15)
ano = float(input('\033[1;37mDigite o ano de nascimento do atleta: \033[m'))
idade = 2024 - ano
if idade < 9:
    print('\033[1;31mO atleta está no nível MIRIM.\033[m')
elif 9 <= idade < 14:
    print('\033[1;32mO atleta está no nível INFANTIL.\033[m')
elif 14 <= idade < 16:
    print('\033[1;33mO atleta está no nível JÚNIOR.\033[m')
elif 16 <= idade < 20:
    print('\033[1;34mO atleta está no nível SÊNIOR.\033[m')
elif idade > 20:
    print('\033[1;35mO atleta está no nível MASTER.\033[m')
