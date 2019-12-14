import random
def jogar():
    print('*'* 33)
    print('Bem vindo no jogo de Adivinhação!')
    print('*'* 33)

    numero_secreto = random.randint(0, 100)
    total_de_tentativas = 0 
    pontos = 1000
    tentativa = 1
    print('''Escolha o nível:
    [1] - Fácil
    [2] - Médio
    [3] - Difícil
    ''')
    nivel = int(input('>'))
    facil = 20
    medio = 10
    dificil = 5

    if (nivel == 1):
        total_de_tentativas = facil
    elif (nivel == 2):
        total_de_tentativas = medio
    else:
        total_de_tentativas = dificil

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
            print(f'O numero secreto era {numero_secreto}')
            print(f'Total de pontos: {pontos}')
            break
        else: 
            if(maior):
                print('Você errou, seu palpite foi acima')
            elif(menor):
                print(f'Você errou, seu palpite foi abaixo')
        pontos_perdidos = abs(numero_secreto - chute) # busca o valor absoluto da formula
        pontos = pontos - pontos_perdidos
        tentativa += 1 
    print('*'* 12)
    print('Fim do jogo')
    print('*'* 12)
if(__name__ == "__main__"): # verificar se o script esta local ou importado e executa
    jogar()
