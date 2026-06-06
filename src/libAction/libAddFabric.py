from classes.message import msgGeneric
from classes.database import Database

# FUNÇÃO PRA VALIDAR NOME DO FABRICANTE


def nomeFabric(name):
    title = 'Erro no cadastro'
    text = 'O nome do fabricante não pode estar vazio!'
    if not name:
        msgGeneric(title=title, text=text)
        return None
    else:
        return name


def cnpjFabric(cnpj):
    title = 'Erro no cadastro'
    text = 'O CNPJ do fabricante não pode estar vazio!'
    if not cnpj:
        msgGeneric(title=title, text=text)
        return None
    else:
        return cnpj


def emailFabric(email):
    title = 'Erro no cadastro'
    text = 'O email do fabricante não pode estar vazio!'
    if not email:
        msgGeneric(title=title, text=text)
        return None
    else:
        return email


def telefoneFabric(telefone):
    title = 'Erro no cadastro'
    text = 'O telefone do fabricante não pode estar vazio!'
    if not telefone:
        msgGeneric(title=title, text=text)
        return None
    else:
        return telefone


def siteFabric(site):
    title = 'Erro no cadastro'
    text = 'O site do fabricante não pode estar vazio!'
    if not site:
        msgGeneric(title=title, text=text)
        return None
    else:
        return site


def ruaFabric(rua):
    title = 'Erro no cadastro'
    text = 'A rua não pode estar vazio!'
    if not rua:
        msgGeneric(title=title, text=text)
        return None
    else:
        return rua


def numeroFabric(numero):
    title = 'Erro no cadastro'
    text = 'O numero do endereço não pode estar vazio!'
    if not numero:
        msgGeneric(title=title, text=text)
        return None
    else:
        return numero


def estadoFabric(estado):
    title = 'Erro no cadastro'
    text = 'O estado não pode estar vazio!'
    if not estado:
        msgGeneric(title=title, text=text)
        return None
    else:
        return estado


def cepFabric(cep):
    title = 'Erro no cadastro'
    text = 'O CEP do fabricante não pode estar vazio!'
    if not cep:
        msgGeneric(title=title, text=text)
        return None
    else:
        return cep


def bairroFabric(bairro):
    title = 'Erro no cadastro'
    text = 'O bairro do fabricante não pode estar vazio!'
    if not bairro:
        msgGeneric(title=title, text=text)
        return None
    else:
        return bairro


def gravaFabricante(**kwargs):
    query = ("INSERT INTO FABRICANTE ( FABRICANTE, CNPJ, EMAIL, TELEFONE,"
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
