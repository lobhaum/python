# definindo a classe conta:
class Conta:
   
    # definindo função construtora:
    def __init__(self, numero, titular, saldo, limite): 
        print(f'Construindo objeto {self}')
        # tornando os atributos privados com __
        self.__numero = numero 
        self.__titular = titular 
        self.__saldo = saldo 
        self.__limite =  limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
