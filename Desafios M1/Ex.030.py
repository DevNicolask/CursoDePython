a = int(input('\033[1;35mMe diga um número qualquer. \033[m'))
if a % 2 == 0:
    print('\033[1;35mSeu número é\033[m \033[1;36mPAR.\033[m')
else:
    print('\033[1;35mSeu número é\033[m \033[1;36mIMPAR.\033[m')
