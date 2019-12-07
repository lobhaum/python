palavras = ['gato', 'janela', 'qualquer frase sem sentido']
for w in palavras[:]:
    if len(w) > 6:
        palavras.insert(0, w)
print(palavras)
