try:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '../src')))
except:
    raise


import pytest
from libAction import prod


def test_nome_do_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodName('oi')
    assert dados == 'oi'


def test_nome_comercial_do_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodComName('oi')
    assert dados == 'oi'


def test_marca_do_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodMarca('oi')
    assert dados == 'oi'


def test_codigo_sku_do_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodSku('oi')
    assert dados == 'oi'


def test_codigo_de_barras_do_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodbarcode('oi')
    assert dados == 'oi'


def test_fabricante_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodFabricante('oi')
    assert dados == 'oi'


def test_fornecedor_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodFornecedor('oi')
    assert dados == 'oi'


def test_codigo_cest_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodCest('oi')
    assert dados == 'oi'


def test_codigo_ncm_produto_nao_esta_vazio_retorna_ok():
    dados = prod.prodNcm('oi')
    assert dados == 'oi'


def test_upadate_Combo_box_fabricante_marca_fornecedor():
    dados = prod.updateComboBox('FABRICANTE')
    assert dados != ''


def test_grava_produto_banco_de_dados():
    dados = prod.gravaProduto(name='nome', prodName='nomeComercial',
                              marca='marca', sku='codSku', codBarras='codBarras',
                              fornecedor='fornecedor', fabricante='fabricante',
                              codncm='codNcm', codcest='codCest')
    assert dados[0] == True
