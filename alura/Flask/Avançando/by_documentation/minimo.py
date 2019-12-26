from flask import Flask  # importando a classe flask
app = Flask(__name__)
'''O primeiro argumento é o nome do módulo ou
pacote do aplicativo. Se você estiver usando um único módulo
(como neste exemplo), use-o __name__porque, dependendo de se ele foi
iniciado como aplicativo ou importado como módulo, o nome será
diferente ( '__main__'versus o nome de importação real). '''


@app.route('/')  # informa qual URL a função será acionada
def hello_world():
    return 'Olá, Mundo'

# if __name__ == '__main__':
#     app.run()
