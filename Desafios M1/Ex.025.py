# Versão Normal.
nome = str(input('Digite seu nome. ')).strip()

# Como o professor Guanabara Fez (Mais fácil!)
print(f'Seu nome tem \"Silva\"? {'silva' in nome.lower()}')

# Como eu fiz:
print(f'Seu nome tem "Silva"? {not (nome.lower().find('silva') == -1)}')

# Versão Colorida.
nome = str(input('\033[1;35mDigite seu name. \033[m')).strip()

# Como o professor Guanabara Fez (Mais fácil!)
print(f'\033[1;35mSeu nome tem \"Silva\"?\033[m \033[1;36m{'silva' in nome.lower()}\033[m')

# Como eu fiz:
print(f'\033[1;35mSeu nome tem "Silva"?\033[m \033[1;36m{not (nome.lower().find('silva') == -1)}\033[m')
