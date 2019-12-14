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

# Criação da classe Filmes, extendendo Programa:
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # super chama a classe mãe:
        super().__init__(nome, ano)
        self.duracao = duracao

    #sem função, apenas ilustrativo: 
    def retorna_cadastro_diferenciado(self):
        pass

# Criação da classe Serie , extendendo Programa:
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
                
# criando e alimentando objeto Filme:
vingadores = Filme('Vingadores', 2019, 180)
#dando like:
vingadores.dar_likes()
#  imprimindo resultado:
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - '
      f'Duração: {vingadores.duracao}'
      f' Likes: {vingadores.likes}')



# criando e alimentando objeto Serie:
atlanta = Serie('Atlanta', 2018,2)
# dando likes:
atlanta.dar_likes()
atlanta.dar_likes()
# imprimindo resultado:
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporada(s):' 
      f' {atlanta.temporadas}'
      f' - Likes: {atlanta.likes}')
