i = int(input('Digite o ano: '))
if (i % 4) == 0:
    if (i % 100) == 0:
        if (i % 400) == 0:
            print(f'{i} é bissexto')
        else:
            print(f'{i} não é bissexto')
    else:
        print(f' {i} é bissexto')
else:
    print(f' {i} não é bissexto')
