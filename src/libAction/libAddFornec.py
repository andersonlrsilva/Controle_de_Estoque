from classes.message import msgGeneric
from classes.database import Database


def nomeFornec(name):
    title = 'Erro no cadastro'
    text = 'O nome do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def cnpjFornec(name):
    title = 'Erro no cadastro'
    text = 'O CNPJ do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def emailFornec(name):
    title = 'Erro no cadastro'
    text = 'O EMAIL do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def telefoneFornec(name):
    title = 'Erro no cadastro'
    text = 'O telefone do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def siteFornec(name):
    title = 'Erro no cadastro'
    text = 'O Site do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def ruaFornec(name):
    title = 'Erro no cadastro'
    text = 'O Rua do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def numeroFornec(name):
    title = 'Erro no cadastro'
    text = 'O Numero do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def estadoFornec(name):
    title = 'Erro no cadastro'
    text = 'O Estado do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def cepFornec(name):
    title = 'Erro no cadastro'
    text = 'O CEP do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def bairroFornec(name):
    title = 'Erro no cadastro'
    text = 'O Fornecedor do fornecedor não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def gravaFornecedor(**kwargs):
    query = ("INSERT INTO FORNECEDOR ( FORNECEDOR, CNPJ, EMAIL, TELEFONE,"
             "TELEFONE2, WEBSITE, RUA, NUMERO, ESTADO, CEP, BAIRRO, FRETE)"
             "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    dados = (kwargs['nome'], kwargs['cnpj'], kwargs['email'],
             kwargs['telefone'], kwargs['telefone2'], kwargs['site'],
             kwargs['rua'], kwargs['numero'], kwargs['estado'], kwargs['cep'],
             kwargs['bairro'], kwargs['frete'])
    db = Database()
    con = db.connect()
    if con is False:
        return
    cursor = con.cursor()
    con.start_transaction()
    cursor.execute(query, dados)
    con.commit()
    con.close()
    return True, kwargs['nome']
