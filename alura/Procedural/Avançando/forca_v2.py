def jogar():
    print('*' * 34)
    print('*** Bem-vindo ao jogo da Forca ***')
    print('*' * 34)

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False
    # enquanto não enforcou e não acertou:
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip() # tira os possiveis espaços da digitação do usuario
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()): #converte em maiusculo dos dois lados
                print(f'Encontrei a {letra} na {index + 1}.')
            index += 1
        print('Jogando....')
    print('Fim do jogo')



if(__name__ == '__main__'):
    jogar()
