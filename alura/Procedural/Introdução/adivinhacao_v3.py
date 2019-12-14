print('*'* 33)
print('Bem vindo no jogo de Adivinhação!')
print('*'* 33)

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1
while (tentativa <= 3):
    print(f'Tentativa {tentativa} de {total_de_tentativas}')
    chute = int(input('Digite um número inteiro exemplo: 14: '))
    print(f'Voce digitou: {chute}')
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acertou):
        print(f'Você acertou o número secreto: {chute}')
    elif(maior):
        print('Você errou, seu palpite foi acima')
    elif(menor):
        print(f'Você errou, seu palpite foi abaixo')
    tentativa += 1 
print('*'* 12)
print('Fim do jogo')
print('*'* 12)
