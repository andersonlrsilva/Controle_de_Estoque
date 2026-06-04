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


def test_nome_do_produto_vazio_retorna_erro():
    dado = prod.prodName(name='')
    assert dado == None
