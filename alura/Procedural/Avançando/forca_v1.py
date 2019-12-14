def jogar():
    print('*' * 34)
    print('*** Bem-vindo ao jogo da Forca ***')
    print('*' * 34)

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False
    # enquanto não enforcou e não acertou:
    while(not enforcou and not acertou):
        print('Jogando....')
    print('Fim do jogo')



if(__name__ == '__main__'):
    jogar()
