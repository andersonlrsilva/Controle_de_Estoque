from math import prod

from classes import message
from classes.database import Database
from ui.addProd import Ui_AddProd


# CADASTRO DE PRODUTOS
# FUNÇÃO PARA VALIDAÇÃO DO NOME DO PRODUTO

proibidos = ('@', '#', '$', '¨', '&', '*')


def prodName(name):
    text = 'O nome do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    # TESTE SE NOME DO PRODUTO ESTA VAZIO
    if not name:
        message.msgGeneric(title=title, text=text)
        return None
    # TESTA SE PRODUTO POSSUI CARACTERE NÃO PERMITIDO
    for c in name:
        if c in proibidos:
            text2 = f'O nome do produto não pode conter o caracter {c}'
            message.msgGeneric(title=title, text=text2)
            return None
    else:
        return name


# FUNÇÃO PARA VALIDAÇÃO DO NOME COMERCIAL DO PRODUTO
def prodComName(prodName):
    text = 'O nome comercial do produto não pode estar vazio'
    title = 'Erro no Cadastro do Produto'
    if not prodName:
        message.msgGeneric(title=title, text=text)
        return None

    # TESTA SE NOME COMERCIAL PRODUTO POSSUI CARACTERE NÃO PERMITIDO
    for c in prodName:
        if c in proibidos:
            text2 = f'O nome comercial do produto não pode conter o caracter {c}'
            message.msgGeneric(title=title, text=text2)
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

    # INICIA A INSTANCIA DO DATABASE E A CONEXÃO
    db = Database()
    con = db.connect()
    if con is False:
        return
    cursor = con.cursor()
    con.start_transaction()

    # DADOS DA TABELA PRODUTO
    queryProd = ("INSERT INTO PRODUTOS (NOMEPRODUTO, NOMECOMERCIAL,"
                 "MARCA, CODSKU, CODBARRAS, FORNECEDOR, FABRICANTE,"
                 "CODNCM, CODCEST)"
                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    dadosProd = (kwargs['name'], kwargs['prodName'], kwargs['marca'],
                 kwargs['sku'], kwargs['codBarras'], kwargs['fornecedor'],
                 kwargs['fabricante'], kwargs['codncm'], kwargs['codcest'])

    cursor.execute(queryProd, dadosProd)
    id_produto = cursor.lastrowid

    # DADOS DA TABELA FOTOS DO PRODUTO
    queryImage = ("INSERT INTO IMGPRODUTO(FOTO, ID_PRODUTO)"
                  "VALUES(%s, %s)")
    dadosImage = (kwargs['image'], id_produto)
    cursor.execute(queryImage, dadosImage)

    # DADOS DA TABELA DESCRIÇÃO / APLICAÇÃO
    queryDescr = ("INSERT INTO DESCRICAO(DESCRICAO,ID_PRODUTO)"
                  "VALUES(%s,%s)")
    dadosDescr = (kwargs['desc'], id_produto)
    cursor.execute(queryDescr, dadosDescr)

    con.commit()
    con.close()
    return True, kwargs['name']


# ee = prodName('')
# print(ee)
