# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento
s = float(input('Salário atual: R$'))
c = s*1.15
print('Salario Atual: R${} '.format(s))
print('Salario atualizado: R${:.2f}'.format(c))
