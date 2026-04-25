try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise


import pytest
from classes import database


def test_conecta_Database():
    db = database.Database()
    con = db.connect()
    assert con is not False


def test_login_user_login_nao_cadastrado_resulta_false():
    db = database.Database()
    var = db.login('login', 'TESTE')
    assert var[0] is False


def test_login_user_password_errada_resulta_false():
    db = database.Database()
    var = db.login('TESTE', '1234')
    assert var[0] is False


def test_login_user_login_password_corretos_retorna_true():
    db = database.Database()
    var = db.login('TESTE', 'TESTE')
    assert var[0] is True
