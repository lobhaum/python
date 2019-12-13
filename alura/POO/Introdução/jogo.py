class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei
        
    def get_jogadas(self):
        return self.__vezes_que_joguei

    def set_jogadas(self, jogada):
        self.__vezes_que_joguei += jogada
    