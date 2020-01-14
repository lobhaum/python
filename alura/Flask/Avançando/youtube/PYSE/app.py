from flask import Flask, render_template, request, redirect, session, flash,\
    url_for, send_from_directory
from random import randint # pumba
from time import sleep # pumba

app = Flask(__name__)

# view
@app.route('/') #  decorate
def index():
    NOMES =  ['FLASK', 'ZIP', 'OLLY', 'BIMBO',
            'ZÉ', 'CHICO', 'CACO', 'PUMBA',
            'MAX', 'TICO', 'OSCAR', 'DJANGO',
            'BARK', 'RINGO', 'BARNEY', 'PANDA',
            'BART', 'MARVIN', 'FIDEL']
    escolha = randint(0, len(NOMES))
    resultado = NOMES[escolha]
    return render_template('index.html', resultado=resultado)



app.run()