import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

cursor.execute('SELECT * FROM contatos_categoria')
resultado = cursor.fetchall()
print(len(resultado))

cursor.close()
conexao.close()
