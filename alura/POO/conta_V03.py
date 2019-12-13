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
    
    # iniciando os getters and setters:
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
   
    @limite.setter
    def limite(self, limite):
        self.__limite = limite 

    