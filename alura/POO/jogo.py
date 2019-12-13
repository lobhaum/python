class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei
        
    def vezes_jogadas(self):
        return self.__vezes_que_joguei