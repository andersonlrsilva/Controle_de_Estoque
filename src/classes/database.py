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

    def executaquery(self, query, dados):
        # db = Database()
        con = self.connect()
        if con is False:
            return
        else:
            cursor = con.cursor()  # type:ignore
            cursor.execute(query, dados)
            dados = cursor.fetchall()
            con.close()
            return dados

    def inserirMarca(self, **kwargs):
        try:
            con = self.connect()
            cursor = con.cursor()  # type:ignore
            dados = (kwargs['marca'], kwargs['site'])
            query = ("""INSERT INTO MARCA(MARCA, SITE)VALUES(%s, %s)""")
            cursor.execute(query, dados)
            con.commit()  # type:ignore
            con.close()  # type:ignore
            return True
        except:
            return False

    def gravaCliente(self, **kwargs):
        try:
            query = ("INSERT INTO CLIENTE (CODECLIENTE, NOMEFANTASIA,"
                     "RAZAOSOCIAL,TIPOCLIENTE, CPF_CNPJ, IE_RG, UF,RAMO,"
                     "DATACLIENTE)"
                     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            dados = (kwargs['code'], kwargs['fantasia'], kwargs['razao'],
                     kwargs['tipocliente'], kwargs['cpf'], kwargs['ierg'],
                     kwargs['uf'], kwargs['ramo'], kwargs["datacliente"])
            con = self.connect()
            cursor = con.cursor()  # type:ignore
            cursor.execute(query, dados)
            con.commit()
            con.close()
        except:
            print('Erro ao salvar')


# if __name__ == "__main__":
#     db = Database()
#     db.gravaCliente(code=123,
#                     fantasia='qweqwe',
#                     razao='wefwefd',
#                     tipocliente='erfgerf',
#                     cpf='12312',
#                     ierg='12312',
#                     uf='uf',
#                     ramo='dddd',
#                     datacliente='2022-01-01'
#                     )
