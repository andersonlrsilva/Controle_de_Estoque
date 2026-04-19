import mysql.connector
import senhadb


# EM PASSWORD SUBISTITUA POR UMA SENHA DE SUA PRFERENCIA
def conectadb():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        user=senhadb.user,
        password=senhadb.senha
    )
    return connection


# FUNÇÃO PARA CRIAR O DATABASE
def criaDB():
    con = conectadb()
    cursor = con.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS DBSISTEMA""")
    con.commit()
    con.close()
    return True


# CRIA A TABELA USER
def createTableUser():
    con = conectadb()
    cursor = con.cursor()
    cursor.execute("""USE DBSISTEMA""")
    cursor.execute("""
                CREATE TABLE USER(
                IDUSER INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                USER VARCHAR(20) NOT NULL,
                PASSWORD VARCHAR(20) NOT NULL,
                USERACCESS ENUM('ADMIN', 'USER') NOT NULL
                )
    """)
    con.commit()
    con.close()
    return True


if __name__ == '__main__':
    cria = criaDB()
    user = createTableUser()
