from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Olá Mundo</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Olá, {name}<h1>' 

@app.route('/cliente')
def cliente():
    user_agent = request.headers.get('User Agent')
    return f'<p> Seu browser é {user_agent}</p>'

@app.route('/')
def index():
    return 'Bad request', 400

if __name__ == '__main__':
    app.run(debug=True)