from random import randrange
def jogar():
    print('*' * 34)
    print('*** Bem-vindo ao jogo da Forca ***')
    print('*' * 34)
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)



    arquivo.close()
    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    # palavra_secreta = 'sequoia'.upper() # armazenando o conteuco em maiusculo
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    # imprimir a forca limpa
    print(letras_acertadas)
    # enquanto não enforcou e não acertou:
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip().upper() # tira os possiveis espaços da digitação do usuario
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra): #converte em maiusculo dos dois lados
                    letras_acertadas[index] = letra # alimenta letras_acertadas com o conteúdo achado no index
                index += 1 # anda uma posição no index
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!!!')
    else:
        print('Você perdeu :(')
    print('Fim do jogo')



if(__name__ == '__main__'):
    jogar()
