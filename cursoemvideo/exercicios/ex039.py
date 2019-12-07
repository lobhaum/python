'''Faça um programa que leia o ano de nascimento
de um jovem e informe de acordo com a idade:
se ele ainda vai se alistar ao serviço militar;
se é a hora de se alistar;
se já passou do tempo do alistamento'''

from datetime import date

ano = date.today().year
# construindo a tela do cadastro:
print('\033[1;32m-\033[1;33m=\033[1;32m-\033[m' * 16)
print('\033[1;32;40mCONTROLE DE ALISTAMENTO MILITAR\033[m')
print('\033[33mBrasil acima de tudo e Deus acima de Todos.\033[m')
print('\033[7;32mVersão 20191110\033[m')
print('\033[1;32m-\033[1;33m=\033[1;32m-\033[m' * 16)
nome = str(input('\033[mNome Completo: \033[33m'))
sexo = str(
    input(
        '\033[m\033[1mM\033[m para Masculino ou \033[1mF \033[m para Feminino: \033[33m'
    ))
i = int(input('\033[mDigite seu ano de nascimento:\033[33m '))
if sexo == 'F' or sexo == 'f':
    print(f'V.Sa. {nome}:')
    print(
        '''\033[31mConforme legislação vigente, pessoas do sexo feminino estão
isentas do Serviço Militar Obrigatório, na forma prevista
pela Constituição. Todavia é permitida a prestação do Serviço
Militar que forem voluntárias, segundo critérios de conveniência
e oportunidade de cada Força Armada.\033[m''')
elif sexo == 'M' or sexo == 'm':
    if ano < i:
        tempo = ano - i
        print(f'Faltam {tempo} para você efetuar o alistamento obrigatório')
    elif ano == i:
        tempo = ano + 18
        print(f'{nome} seu alistamento obrigatório ocorrerá no ano {tempo}')
    elif ano > i:
        tempo = i + 18
        print(
            f'{nome} \033[31mprocure o centro de reserva para verificar o procedimento\nde alistamento pós período obrigatório\033[33m'
        )
        print(f'Você deveria ter se alistado em \033[31m{tempo}\033[33m.')
