# digite numero inteiro entre 0 a 5
# peça pro usuario tentar descobrir q numero o pc escolheru
# confirmar se acertou ou errou
import random

pc = random.randrange(6)
i = int(input('Escolha um numero entre 0 e 5 e veja se acertou: '))
if i == pc:
    print('Você acertou')
else:
    print('Você errou, tente novamente')
    print('Numero escolhido {}'.format(pc))
