try:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '../src')))
except:
    raise


from libAction import libdefault

# TESTA VALIDAÇÃO DE NOME


def test_libdefault_namevalidation_vazio_retona_None():
    dados = libdefault.nameValidation('')
    assert dados == None


def test_namevalidation_com_caracteres_proibidos_retona_false():
    dados = libdefault.nameValidation('#')
    assert dados == False


def test_libdefault_namevalidation_correto_retona_o_Nome():
    dados = libdefault.nameValidation('teste')
    assert dados == 'teste'


# TESTE DE CAMPO CPF VAZIO
def test_libdefault_validateDoc_Pfisica_vazio_retorna_False():
    dados = libdefault.validateDoc(dados='', tipo='Fisica')
    assert dados[0] == False  # type:ignore


def test_libdefault_validateDoc_Pfisica_menor_de_11_digitos_retorna_False():
    dados = libdefault.validateDoc(dados='123412', tipo='Fisica')
    assert dados[0] == False  # type:ignore


def test_libdefault_validateDoc_Pfisica_11_digitos_iguais_retorna_False():
    dados = libdefault.validateDoc(dados='22222222222', tipo='Fisica')
    assert dados[0] == False  # type:ignore


def test_libdefault_validateDoc_Pfisica_CPF_incorreto_retorna_False():
    dados = libdefault.validateDoc(dados='13245685688', tipo='Fisica')
    assert dados[0] == False  # type:ignore


def test_libdefault_validateDoc_Pfisica_CPF_correto_retorna_True():
    dados = libdefault.validateDoc(dados='11132685060', tipo='Fisica')
    assert dados[0] == True  # type:ignore
