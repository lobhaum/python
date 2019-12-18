from flask import Flask, render_template


app = Flask(__name__)


link_de_apostilas = 'http://www.caelum.com.br/apostilas'


@app.route('/home')
def principal():
    return render_template('home.html', apostilas=link_de_apostilas)


app.run()
