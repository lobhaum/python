def jogar():
    print('*' * 34)
    print('*** Bem-vindo ao jogo da Forca ***')
    print('*' * 34)

    palavra_secreta = 'banana'
    letras_acertadas = ['_','_','_','_','_','_']
    enforcou = False
    acertou = False
    # imprimir a forca limpa
    print(letras_acertadas)
    # enquanto não enforcou e não acertou:
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip() # tira os possiveis espaços da digitação do usuario
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()): #converte em maiusculo dos dois lados
                letras_acertadas[index] = letra # alimenta letras_acertadas com o conteúdo achado no index
            index += 1 # anda uma posição no index
        print(letras_acertadas)
    print('Fim do jogo')



if(__name__ == '__main__'):
    jogar()
