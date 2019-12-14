idade = int(input('Digite sua idade: '))
if( idade > 18 ):
    print('Parabéns, você é maior de idade.')
else:
    if (idade < 12):
        print('Você é uma criança')
    elif (idade > 12):
        print('Você é um adolescente') # Não será mostrado nada se ele(a) tiver 12 anos
