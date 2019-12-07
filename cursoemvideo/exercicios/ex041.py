'''A confederação nacional de natação precisa
de um programa que leia o ano de nascimento
de um atleta e moste sua categoria de acordo
com a idade
- até 9 anos: Mirim
- ate 14 anos: Infantil
- até 19 anos: Junior
- até 20 anos: Sênior
- Acima: Master '''
# desenhando a tela de verificação:
print('\033[36m¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> ' * 2)
print(
    '´¯`·..´¯`·.¸\033[37mPROGRAMA JOVENS NADADORES DO BRASIL\033[36m.·´¯`·..·´¯`'
)
print('\033[36m¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> ' * 2)
nome = str(input('\033[36mNome completo:\033[33m '))
i = int(input('\033[36mIdade completa:\033[33m  '))
if i <= 9:
    print(f'{nome} \033[36miniciará no \033[35mMirim')
elif i <= 14:
    print(f'{nome} \033[36miniciará no \033[35mInfantil')
elif i <= 19:
    print(f'{nome} \033[36miniciará no \033[35mJunior')
elif i <= 20:
    print(f'{nome} \033[36miniciará no \033[35mSênior')
else:
    print(f'{nome} \033[36miniciará no \033[35mMaster')
