print('*'* 33)
print('Bem vindo no jogo de Adivinhação!')
print('*'* 33)

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1
for rodada in range( tentativa, total_de_tentativas + 1):
    print(f'Tentativa {tentativa} de {total_de_tentativas}')
    chute = int(input('Digite um número inteiro entre 1 e 100: '))
    print(f'Voce digitou: {chute}')
    if( 1 < chute >  100):
        print('Vc deve digitar um número entre 1 e 100!')
        continue
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acertou):
        print(f'Você acertou o número secreto: {chute}')
        break
    elif(maior):
        print('Você errou, seu palpite foi acima')
    elif(menor):
        print(f'Você errou, seu palpite foi abaixo')
    tentativa += 1 
print('*'* 12)
print('Fim do jogo')
print('*'* 12)
