from datetime import date
atual = date.today().year
i = int(input('Ano: '))
idade = atual - i
print(f'Quem nasceu em {i} completa/ou em {atual} {idade} anos.')
if idade == 18:
    print('Você precisa se alistar')
elif idade < 18:
    saldo = 18 - idade
    print(f'Voce ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Você se alistará em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce deveria ter se alistado a {saldo} anos.')
    ano = atual - saldo
    print(f'Voce deveria se alistar em {ano}')