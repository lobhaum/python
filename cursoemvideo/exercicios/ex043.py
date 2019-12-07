peso = float(input('Peso em Kg: '))
altura = float(input('Altura em metros: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu indice {imc:.2f} está abaixo do peso')
elif imc > 18.5 and imc < 25:
    print(f'Seu indice {imc:.2f} está ideal')
elif imc > 25 and imc < 30:
    print(f'Seu indice {imc:.2f} está com sobrepeso')
elif imc > 30 and imc < 40:
    print(f'Seu indice {imc:.2f} demonstra obesidade')
else:
    print(f'Seu indice {imc:.2f} demonstra obesidade morbida')
