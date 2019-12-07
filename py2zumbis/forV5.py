palavras = ['gato', 'janela', 'qualquer frase sem sentido', 'jabuticaba']
for w in palavras:
    print(w, len(w))
print(f'a lista palavras tem {len(palavras)} item(ns)')
for w in palavras:
    if w in 'aeiou':
        w = w + '*'
    else:
        w = w
    print(w)
