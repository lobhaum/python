import tweepy

chave_consumidor = 'eY81rAbHIIY5ZBYKle6v71dcA'
segredo_consumidor = 'mIDRdnUSRdKQThW71Xkg7Scpk4UteTJR5pbJ9qNdfJZdN2kL5x'
token_acesso = '3438549358-VGeVLoWLzuWuImkseFoUdl94qXqP7J68XuGPxsf'
token_acesso_segredo = 'i6yXb3miU8BHRma6eaJbIvnQIRdIQVMdLO5kP0n2HBfQd'
# construtor de acesso:
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)
twitter = tweepy.API(autenticacao)
pesquisa = input('Digite o termo: ')
resultados = twitter.search(q=pesquisa, result_type='mixed')
for tweet in resultados:
    print(f'Usuário:{tweet.user.screen_name} - Tweet: {tweet.text}')


