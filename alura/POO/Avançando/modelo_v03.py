# criação da classe Programa (herança)
class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # criando property para não quebrar codigo abaixo
    @property
    def nome(self):
        return self._nome 

    @property
    def likes(self):
        return self._likes
    
    # criando setter para poder modificar o nome com atributo privado
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def dar_likes(self):
        self._likes += 1

    # tornando a classe coesa, colocando para a classe Programa
    # imprimir seus atributos:
    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}')


# Criação da classe Filmes, extendendo Programa:
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # super chama a classe mãe:
        super().__init__(nome, ano)
        self.duracao = duracao

    # sobrescrevendo o método Programa.imprime()
    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano}'
              f' Duração: {self.duracao} minutos - Likes: {self._likes}')


# Criação da classe Serie , extendendo Programa:
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
                
    # sobrescrevendo o método Programa.imprime()
    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano}'
              f' Temporada: {self.temporadas}'
              f' - Likes: {self._likes}')


# criando e alimentando objeto Filme:
vingadores = Filme('Vingadores', 2019, 180)
# dando like:
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
#  imprimindo resultado:
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - '
#      f'Duração: {vingadores.duracao}'
#      f' Likes: {vingadores.likes}')

# criando e alimentando objeto Serie:
atlanta = Serie('Atlanta', 2018, 2)
# dando likes:
atlanta.dar_likes()
atlanta.dar_likes()
# imprimindo resultado:
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporada(s):' 
#      f' {atlanta.temporadas}'
#      f' - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    # detalhes chama o objeto programa e a propriedade duracao,
    # verifica se existe 'duração' através de 'hasattr' has attribute
    # usando if caso tenha, imprime o atributo duração 
    # caso não tenha imprime o atributo temporadas
    # cancelando o algoritmo de verificação detalhes pela criaçãodo metodo
    # Programa.imprime()
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else
    # programa.temporadas
    programa.imprime()  # polimorfismo interpreta quando o metodo sera de
    # filmes ou series automaticamente
    # print(f'Programa: {programa.nome} - Detalhes: {detalhes}' 
    # f'Likes: {programa.likes}')
