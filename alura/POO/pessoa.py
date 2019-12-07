class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def exibe_nome_e_sobrenome(self):
        print(f'O nome é {self.nome} e o sobrenome é {self.sobrenome}')

pessoa = Pessoa('Edu', 'Luciano')
pessoa.exibe_nome_e_sobrenome()

