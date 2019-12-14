class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao 
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

# Criação da classe Serie:
class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0
                
    def dar_likes(self):
        self.likes += 1

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
