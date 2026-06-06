from classes import message
from classes.database import Database
from ui.addProd import Ui_AddProd


# CADASTRO DE PRODUTOS
# FUNÇÃO PARA VALIDAÇÃO DO NOME DO PRODUTO


def prodName(name):
    text = 'O nome do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not name:
        # message.msgGeneric(title=title, text=text)
        return None, message.msgGeneric(title=title, text=text)
    else:
        return name


# FUNÇÃO PARA VALIDAÇÃO DO NOME COMERCIAL DO PRODUTO
def prodComName(prodName):
    text = 'O nome comercial do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not prodName:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return prodName


# FUNÇÃO PARA VALIDAÇÃO DA MARCA DO PRODUTO
def prodMarca(marca):
    text = 'A marca do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not marca:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return marca


# FUNÇÃO PARA VALIDAÇÃO DO CODIGO SKU
def prodSku(sku):
    text = 'O código SKU do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not sku:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return sku


# FUNÇÃO PARA VALIDAÇÃO DO CODIGO DE BARRAS
def prodbarcode(barcode):
    text = 'O código de barras do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not barcode:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return barcode


# FUNÇÃO PARA VALIDAÇÃO DO FABRICANTE
def prodFabricante(fabricante):
    text = 'O código de barras do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not fabricante:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return fabricante


# FUNÇÃO PARA VALIDAÇÃO DO FORNECEDOR
def prodFornecedor(fornecedor):
    text = 'O fornecedor do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not fornecedor:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return fornecedor


# FUNÇÃO PARA VALIDAÇÃO DO CODIGO CEST
def prodCest(cest):
    text = 'O fornecedor do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not cest:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return cest


# FUNÇÃO PARA VALIDAÇÃO DO CODIGO NCM
def prodNcm(ncm):
    text = 'O fornecedor do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not ncm:
        message.msgGeneric(title=title, text=text)
        return None
    else:
        return ncm


# ATUALIZAR COMBOBOX FABRICANTE / MARCA / FORNECEDOR
def updateComboBox(args):
    db = Database()
    con = db.connect()
    if con is False:
        return None
    cursor = con.cursor()
    string = f'SELECT {args} FROM {args}'
    cursor.execute(string)
    dados = cursor.fetchall()
    return dados


def gravaProduto(**kwargs):
    # GRAVA OS DADOS DA TABELA PRODUTO
    queryProd = ("INSERT INTO PRODUTOS (NOMEPRODUTO, NOMECOMERCIAL,"
                 "MARCA, CODSKU, CODBARRAS, FORNECEDOR, FABRICANTE,"
                 "CODNCM, CODCEST)"
                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    dadosProd = (kwargs['name'], kwargs['prodName'], kwargs['marca'],
                 kwargs['sku'], kwargs['codBarras'], kwargs['fornecedor'],
                 kwargs['fabricante'], kwargs['codncm'], kwargs['codcest'])
    # INICIA A INSTANCIA DO DATABASE E A CONEXÃO
    db = Database()
    con = db.connect()
    if con is False:
        return
    cursor = con.cursor()
    con.start_transaction()
    cursor.execute(queryProd, dadosProd)
    id_produto = cursor.lastrowid
    con.commit()
    con.close()
    return True, kwargs['name']
