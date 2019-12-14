import adivinhacao
import forca
def escolhe_jogo():
    print('''
    ESCOLHA UM JOGO:
    [1] - ADIVINHAÇÃO
    [2] - FORCA
    [0] - SAIR
    ''')
    opcao = int(input('>'))
    if(opcao == 1):
        adivinhacao.jogar()
    elif(opcao == 2):
        forca.jogar()
    elif(opcao == 0):
       quit() 
    else:
        print('Opção inválida')

if(__name__ == '__name__'): escolhe_jogo()
