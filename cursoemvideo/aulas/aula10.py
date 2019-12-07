nome = str(input('Qual é seu nome? '))
if nome == 'Lobhaum':
    print('Uau! um lobo grande S2 S2 S2 S2')
else:
    print('Logando....')
print(f'Bom dia, {nome}')
# ---------
# validando médias
# ---------
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
n4 = float(input('quarta nota: '))
m = (n1 + n2 + n3 + n4) / 4
print(f'Média final: {m:.1f}')
if m >= 6:
    print('Aluno aprovado!')
else:
    print('Aluno em recuperação')
print('Solicitar transferencia para ano superior'
      if m >= 6 else 'Solicitar vaga no curso de recuperação nas férias')
