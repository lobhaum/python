class Conta:

    #definindo construtor da classe
    def __init__(self, numero, titular, saldo, limite):
        # exibindo endereço da memoria do construtor
        print(f'Construindo objeto {self}')
        # passando valores ao construtor
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        # o construtor chama ele próprio
        # devendo passar os parametros ex:
        # conta = Conta(123, 'Nome', 10, 1000)

    def extrato(self):
        print(f'O saldo da conta {self.titular} é de R$ {self.saldo}')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
