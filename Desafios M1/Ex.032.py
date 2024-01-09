# Minha Versão.(Colorido.)
# Importa uma biblioteca criada de PYTHON com a data atual.
from datetime import date

# Pede ao usuário um ano.
ano = int(input('\033[1;35mMe diga um ano para analizar se é um ano bissexto.\033[m'
              '\033[1;36m(Digite 0 para analizar o ano atual) \033[m'))
# Se ano == 0, importa pela biblioteca o ano atual.
if ano == 0:
    ano = date.today().year
# Testa se as condições para ser um ano bissexto são cumpridas.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;35mO ano\033[m \033[1;35m{ano}\033[m \033[1;36mÉ BISSEXTO!\033[m')
else:
    print(f'\033[1;35mO ano\033[m \033[1;35m{ano}\033[m \033[1;36mNÃO É BISSEXTO!\033[m')
