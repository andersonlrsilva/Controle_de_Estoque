import mysql.connector
from mysql.connector import Error


# CLASSE DATABASE
class Database():
    def __init__(self,
                 host='127.0.0.1',
                 port='3306',
                 database='DBSISTEMA',
                 user='DBUSER',
                 passwd='123456'
                 ):
        self.host = host
        self.port = port
        self.database = database
        self.password = passwd
        self.user = user

# INICIA CONEXÃO COM BANCO DE DADOS
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            return self.connection
        except Error as e:
            print(f'Erro de conexão com o banco de dados: \n{e}')
            return False

        # LOGIN DO USUARIO

    def login(self, user, passwd):
        db = Database()
        con = db.connect()
        if con is False:
            return
        else:
            cursor = con.cursor()  # type:ignore
            cursor.execute("""SELECT * FROM USER""")
            dados = cursor.fetchall()
            con.close()  # type:ignore
            #
            for id, usuario, senha, nivel in dados:
                # VERIFICA SE O NOME DE LOGIN EXSITE NO DATABASE
                if usuario == user:
                    # VERIFICA USER E SENHA, E RETORNA LOGIN TRUE
                    if usuario == user and senha == passwd:
                        return True, id, usuario, nivel
            # VERIFICA SENHA DO USUARIO E RETORNA FALSE, PARA SENHA INVALIDA
                    if usuario == user and senha != passwd:
                        return False, 'L001'
            # RETORNA FALSE SE NAO ENCONTAR O NOME DE LOGIN
            else:
                return False, 'L002'


if __name__ == '__main__':
    db = Database()
    db.login('itallo', 'ggg')
