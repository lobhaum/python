class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao 
        self.__likes = 0

    # criando property para não quebrar codigo abaixo
    @property
    def nome(self):
        return self.__nome 

    @property
    def likes(self):
        return self.__likes
    
    # criando setter para poder modificar o nome com atributo privado
    @nome.setter
    def nome(self, novo_nome):
        self.__nome =novo_nome.title()
    
    def dar_likes(self):
        self.__likes += 1

# Criação da classe Serie:
class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
                
    # criando property para não quebrar codigo abaixo
    @property
    def nome(self):
        return self.__nome 

    @property
    def likes(self):
        return self.__likes
    
    # criando setter para poder modificar o nome com atributo privado
    @nome.setter
    def nome(self, novo_nome):
        self.__nome =novo_nome.title()
    
    def dar_likes(self):
        self.__likes += 1

# criandoe alimentando objeto Filme:
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
