import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='programador', passwd='Brasil2020',
                       host='192.168.1.100', port=3306)

cursor = conn.cursor()

cursor.execute('SELECT * from jogoteca.jogo')
for user in cursor.fetchall():
    print(f' Jogo: {user[1]} Categoria: {user[2]} Console: {user[3]}')


# commitando senão nada tem efeito
conn.commit()
cursor.close()
