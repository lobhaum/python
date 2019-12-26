from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
mysql.config('MYSQL_DATABASE_HOST':'192.168.1.100',
             'MYSQL_DATABASE_PORT': 3306,
             'MYSQL_DATABASE_USER':'programador',
             'MYSQL_DATABASE_PASSWORD':'Brasil2020')
@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)


if __name__ == '__main__':
    app.run(debug=True)
