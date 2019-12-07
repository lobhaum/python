# ANSI
# \033[m]
# \033[style - text - back m]
# \033[0;33;44m]
# Style         Text        Back
# 0 none        30 branco   40
# 1 bold        31 vermelho 41
# 4 underline   32 verde    42
# 7 Negative    33 amarelo  43
#               34 azul     44
#               35 roxo     45
#               36 cian     46
#               37 cinza    47

print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[0;30;42mTeste')
print('\033[mTeste')
print('\033[7;30mTeste')